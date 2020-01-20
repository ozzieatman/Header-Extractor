# Header-Extractor
Using AI / NLP / ML to extract headers from legal documents. 

# @Params: String = file to open.
parser.fetch_headers("NDA1.docx")


# Limitations 
# Could Add some of these as factors. However they are less efficient. All lines have /n preceeding or suceeding it. 
        # If it has [ as first char or ] as last char
        # If the next line is a newline
        # If the Preceeding Line is a newline 

# DOC files do not show the appropriate numbers. So using them as a ranking indicator was not successful.

# Initial plan was to create a fitness function then use a rand number generator to pick elements statistically based on score. This was inspired by the model
# We used to predict food preferences with Genetic Algorithms. However it seemed it might be an over usage here.


