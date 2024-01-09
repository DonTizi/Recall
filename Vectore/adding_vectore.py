import getpass
import os
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain_community.vectorstores import Pinecone
from langchain_community.embeddings.openai import OpenAIEmbeddings
import pinecone
import sys



# Set your Pinecone API key and environment
pinecone_api = "APIKEY"
pinecone_env = "ENV"

# Set your OpenAI API key
openai_api = "APIKEY"

# Initialize Pinecone
pinecone.init(api_key=pinecone_api, environment=pinecone_env)

# Define the index name
index_name = "rewind"

# Check if the index already exists, if not, create it
if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, metric="cosine", dimension=1536)

# Load the documents using TextLoader
loader = TextLoader("/Users/dontizi/Documents/Rewind/new_texts.txt")
documents = loader.load()
# Split the documents into chunks using CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Initialize the OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=openai_api)

# Create or load the Pinecone index
docsearch = Pinecone.from_existing_index(index_name, embeddings)
docsearch.add_documents(docs)
