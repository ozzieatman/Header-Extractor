import docx2txt
import textract
import json

def import_document(mFile):
    file_type = mFile.split(".")[1].lower()
    text = ""
    if file_type == "docx":
         return docx2txt.process(mFile)
    elif file_type == "doc":
        # DOC Needs to be converted to String
        text = textract.process(mFile, encoding='ascii')
        return text.decode()
    else:
        print("Invalid File. File needs to be Doc or Docx")

def JSON_convert(text_to_convert):
    lines = text_to_convert.splitlines()
    json_array = []
    for index, l in enumerate(lines):
        mDict = {}
        mDict["p_id"] = index
        mDict["p_text"] = l
        json_array.append(json.dumps(mDict))
    return json_array

# Fitness Function that assess's each line in the JSON list and assigns a score depending on how many Header patterns it matches.
# @Param: Strings[] mList
def fitness_function(mList):
    # JSON to List of Dictionaries. [ {line: 2) THIS IS A HEADING:, score: 2}]
    dictList = []
    for l in mList:
        dictItem = json.loads(l)
        mDict = {
            "name": dictItem["p_text"], 
            "score": 0
        }    
        dictList.append(mDict)
    # print(dictList[3]["name"])

    # Go through List and assess against Header Patterns. Assigning a fitness. 
    # If all Caps
    dictList = all_caps(dictList)
    # Has Colon : as last char
    dictList = has_colon(dictList)

    # Has number as first character
    dictList = num_as_first_char(dictList)

    

    return dictList


    # Remove Definet non Headers
def all_caps(mList):
    for items in mList:
        if items["name"].isupper():
            items["score"] +=1
    return mList

    # Has Colon : as last char
def has_colon(mList):
    for l in mList:
        if len(l["name"]) > 0:
            stripped = l["name"].replace(" ", "")
            # print(stripped)
            last_char = len(stripped)-1
            if stripped[last_char] == ":":
                l["score"] +=1
    return mList

# Has number as first character
def num_as_first_char(mList):
    for l in mList:
        if len(l["name"]) > 0:
            stripped = l["name"].replace(" ", "")
            # print(stripped)
            first_char = stripped[0]
            # print(l["name"],first_char)
            if first_char.isdigit():
                # print(l["name"],first_char, "IS FIRST")
                l["score"] +=1
    return mList


    
