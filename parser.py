# TODO Create GUI

import api

# @Params: String = File
def fetch_headers(mFile):
    # mFile = "NDA1.docx"
    # mFile = "Test Co Letter.DOC"
    # Docuement / DocX as String

    text = api.import_document(mFile)
    # Take Document; Import is as JSON 
    mJson = api.JSON_convert(text)
    population = api.fitness_function(mJson)

    population.sort(key=lambda x: x["score"])
    for p in population:
        if p["score"] > 0:
            print (p)
        

    



