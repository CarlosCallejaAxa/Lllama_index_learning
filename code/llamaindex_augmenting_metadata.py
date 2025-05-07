#Import the updated function to load the documents
from functions import load_documents_updated as load_data
#Import llamaindex text extractors
from llama_index.core.extractors import (TitleExtractor, KeywordExtractor)
#Import the text splitter
from llama_index.core.node_parser import SentenceSplitter
#Import the ingestion pipeline
from llama_index.core.ingestion import IngestionPipeline
#Import the necessary modules
import os
import getpass
#Create the directory
dir= "./Data"
#Create a list of the excluded the metadata
excluded_metadata=['file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date','file_path']
#Create the text template to pass the document to the embedings model and the llm model
text_template= "Metadata:\n{metadata_str}\n---\nContent:\n{content}"
#Load the documents
docs= load_data(dir=dir,text_template=text_template,excluded_embed_keys=excluded_metadata, excluded_llm_keys=excluded_metadata)

#Get the secure gpt api key
os.environ['SECURE_GPT_KEY']= getpass.getpass('Enter your Secure GPT API Key:')

#TO DO:
#Import the secure gpt connections and models
#Acesss a model from secure gpt
llm_transformation= None
text_splitter= SentenceSplitter(separator=" ", chunk_size=1024, chunk_overlap=128)
title_Extractor= TitleExtractor(llm=llm_transformation, nodes=5)
Keyword_extractor= KeywordExtractor(llm=llm_transformation, keywords=5)

pipeline= IngestionPipeline(transformations=[
    text_splitter,
    title_Extractor,
    Keyword_extractor
    ]
)

nodes= pipeline.run(documents=docs, in_place= True, show_progress= True)

len(nodes)

print(nodes[0])