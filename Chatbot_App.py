import numpy as np
import pandas as pd
import openai
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from llama_index.core import ServiceContext, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
import os
import time
import random
import warnings
import gradio as gr
warnings.filterwarnings('ignore')

# Function to load documents from the directory
def load_documents(directory_path):
    return SimpleDirectoryReader(directory_path).load_data()

# Function to create or update the index
def create_or_update_index(documents, service_context):
    return VectorStoreIndex.from_documents(documents, service_context=service_context)

# Initial setup for the API key input
def setup_api_key(api_key):
    openai.api_key = api_key

# Directory path for your data
directory_path = "./textdata"

# Initial documents loading
documents = load_documents(directory_path)

# Define a function to set up the service context and index
def setup_service_context_and_index(api_key):
    setup_api_key(api_key)  # Ensure the API key is set
    llm = ChatOpenAI(api_key=api_key,
                     temperature=0, 
                     model_name="gpt-3.5-turbo",
                     max_tokens=1000)

    service_context = ServiceContext.from_defaults(
        llm=llm, 
        chunk_size=1000, 
        chunk_overlap=30, 
        context_window=5000, 
        num_output=300)

    index = create_or_update_index(documents, service_context)

    # Persist the index
    index.storage_context.persist()

    return service_context, index

# Function to handle the chatbot response
def chatbot(input_text, chat_history=[], api_key=None, index=None):
    if api_key and index:
        query_engine = index.as_query_engine()
        response = query_engine.query(input_text)
        
        if not response:
            response = "Sorry! I do not have information for this question. Please reach out to abc@inteleos.org for further assistance."
        
        chat_history.append((input_text, str(response)))
        time.sleep(random.randint(0, 5))
        return '', chat_history
    else:
        return "API key or index not set.", chat_history

# Function to handle file uploads
def handle_upload(files, index, service_context, api_key):
    setup_api_key(api_key)  # Ensure the API key is set before updating the index
    for file in files:
        file_path = file.name
        dest_path = os.path.join(directory_path, os.path.basename(file_path))
        os.rename(file_path, dest_path)
    
    # Load new documents
    new_documents = load_documents(directory_path)
    
    # Update the index with new documents
    index = create_or_update_index(new_documents, service_context)
    index.storage_context.persist()
    
    return index

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Document Interpreter Chatbot")
    api_key_input = gr.Textbox(label="Enter your OpenAI API key and Click Enter")
    upload_button = gr.File(label="Upload Documents", file_count="multiple", type="filepath")
    chatbot_interface = gr.Chatbot(label='Document Interpreter Chatbot', height=400)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot_interface])
    
    # Outputs for API key submission
    index_output = gr.State()
    service_context_output = gr.State()
    api_key_output = gr.State()

    # Set up service context and index on API key input
    def on_api_key_submit(api_key):
        service_context, index = setup_service_context_and_index(api_key)
        return index, service_context, api_key

    # Handle API key input
    api_key_input.submit(on_api_key_submit, inputs=api_key_input, outputs=[index_output, service_context_output, api_key_output])

    # Handle document upload
    upload_button.change(handle_upload, inputs=[upload_button, index_output, service_context_output, api_key_output], outputs=index_output)

    # Chatbot interaction
    msg.submit(chatbot, [msg, chatbot_interface, api_key_output, index_output], [msg, chatbot_interface])

demo.launch(share=True)
