# RecallAI - Documentation
Overview
RecallAI is a powerful application that integrates multiple APIs, including OpenAI and Pinecone, to offer real-time data processing and querying capabilities. This document provides a step-by-step guide to set up and run RecallAI on your system.

## Prerequisites
Before you begin, ensure you have API keys for the following services:

OPENAI
Pinecone
These keys are essential for the functioning of RecallAI.

## Setup Instructions
### API Keys Configuration:

Insert your API keys in the respective places within the following files:
/vectore/adding_vectore.py
indexing.py
### File Replacement:

Replace the following files in your project directory:
all_texts.txt
new_texts.txt
Note: The 'regular_db' file will be created automatically at launch.
### Install Required Packages:

Install all the necessary packages that RecallAI depends on. The list of these packages can be found in the requirements.txt file.
## Running the Program
### Starting the Program:

Execute main.py to start RecallAI.
The program will process information in real-time.
### Data Availability:

Processed data will be available in Pinecone's vector database within minutes after the program starts.
### User Interface:

Interact with the model and query about the computer's activity using the UI_Rewind.py file.
