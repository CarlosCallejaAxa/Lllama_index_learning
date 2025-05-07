#This module has all the functions we are going to use across programs

#We import SimpleDirectoryReader to load all the pdfs
from llama_index.core import SimpleDirectoryReader
#Define a function to extract the data given a directory
def load_documents(dir:str):
    docs=SimpleDirectoryReader(input_dir=dir).load_data()
    return docs

#Updated loading function
def load_documents_updated(dir:str,text_template:str,excluded_embed_keys:list, excluded_llm_keys:list):
    #Load the data
    docs=SimpleDirectoryReader(input_dir=dir).load_data()
    #Edits how the information and metadata is passed to the embeding model and llm model
    for doc in docs:
        doc.text_template= text_template
        #The keys that are excluded for the embeding model
        doc.excluded_embed_metadata_keys= excluded_embed_keys
        #The keys that are excluded for the llm model
        doc.excluded_llm_metadata_keys= excluded_llm_keys
    return docs