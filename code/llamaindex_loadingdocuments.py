#First we will ingest the data 

#We import SimpleDirectoryReader to load all the pdfs
from llama_index.core import SimpleDirectoryReader
#To calculate the time it takes for the documents to load we load time 
import time

start_time= time.time()
#We load the documents 
documents=SimpleDirectoryReader(input_dir="./Data").load_data()
end_time=time.time()
#Print the time
print('Loading time {}'.format(end_time-start_time))
#Print the length of the documents to check how many are created
print(len(documents))
#See the data that it stores in one document
print(documents[0].__dict__)
 
