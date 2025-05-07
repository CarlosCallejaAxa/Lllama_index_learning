#Import the updated function to load the documents
from functions import load_documents_updated as load_data
#Create the directory
dir= "./Data"
#Create a list of the excluded the metadata
excluded_metadata=['file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date','file_path']
#Create the text template to pass the document to the embedings model and the llm model
text_template= "Metadata:\n{metadata_str}\n---\nContent:\n{content}"
#Load the documents
docs= load_data(dir=dir,text_template=text_template,excluded_embed_keys=excluded_metadata, excluded_llm_keys=excluded_metadata)

print(docs[0].__dict__)