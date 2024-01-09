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
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Set your Pinecone API key and environment
pinecone_api = "cd4f4df8-d7ee-405e-86de-1f2c37485a14"
pinecone_env = "us-west4-gcp-free"

# Set your OpenAI API key
openai_api = "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"
# Initialize Pinecone
pinecone.init(api_key=pinecone_api, environment=pinecone_env)

# Define the index name
index_name = "rewind"
# Check if the index already exists, if not, create it
if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, metric="cosine", dimension=1536)

# Load the documents using TextLoader
loader = TextLoader("/Users/dontizi/Documents/Rewind/Database_management/all_texts.txt")
documents = loader.load()
# Split the documents into chunks using CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Initialize the OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=openai_api)

# Create or load the Pinecone index
docsearch = Pinecone.from_existing_index(index_name, embeddings)

# Perform similarity search
query = sys.argv[1] if len(sys.argv) > 1 else "quels musiques jecoute quotidiennement sur apple music?"
docs = docsearch.similarity_search(query)
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Load the question answering chain
chain = load_qa_chain(OpenAI(), chain_type="stuff")

# the rest of your code to perform the search and get answers
results = docsearch.similarity_search(query)
answers = chain.run(input_documents=results, question=f"Hello! Based on the extensive context provided by the transcriptions of your daily laptop activity, I am here to analyze and answer your questions with a high degree of specificity and relevance. I will sift through the data {results}, ignoring unrelated details such as browser bookmarks, to focus on the pertinent activities related to your query.Please proceed to ask your question, and I will provide insights and answers based on the activities documented in the transcriptions of your laptop usage. Remember, the more specific your question, the more accurately I can assist you using the context available.Now, let's dive into your query: "+query)
print(answers)
