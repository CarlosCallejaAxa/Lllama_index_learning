#Import the function to load the documents
from functions import load_documents as load_data
#import MetadataMode to edit the metadata that is passed to the embedings and the LLM model
from llama_index.core.schema import MetadataMode

#Load the documents
docs= load_data("./Data")
#confirm its been loaded properly


for doc in docs:
    doc.text_template="Metadata:\n{metadata_str}\n---\nContent:\n{content}"
    doc.metadata_separator="\n"
    doc.excluded_embed_metadata_keys= ['file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date','file_path']
    doc.excluded_llm_metadata_keys= ['file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date','file_path']


#print(docs[0].get_content(metadata_mode=MetadataMode.EMBED))
print(docs[0].get_content(metadata_mode=MetadataMode.LLM))