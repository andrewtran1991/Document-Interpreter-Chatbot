# Document Interpreter Chatbot

Welcome to the Document Interpreter Chatbot! This chatbot uses OpenAI's language models to provide insights and information from your uploaded documents. Below, you'll find instructions on setting up and using the chatbot.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Functions](#functions)
5. [Gradio Interface](#gradio-interface)
6. [License](#license)

## Requirements

- Python 3.7 or higher
- OpenAI API key
- Required Python packages:
  - numpy
  - pandas
  - openai
  - langchain_openai
  - langchain_community
  - llama_index
  - gradio

## Installation
### Setting Up a Virtual Environment

1. **Open Command Prompt or Terminal:**
    - Press `Win + R`, type `cmd`, and press `Enter`. Or open your terminal.

2. **Navigate to Your Project Directory:**
    ```bash
    cd path\to\your\project
    ```

3. **Install Virtual Environment Tool (Optional):**
    If you haven't installed the virtual environment package (`virtualenv`) yet, you can install it using pip:
    ```bash
    pip install virtualenv
    ```

4. **Create a Virtual Environment:**
    ```bash
    virtualenv chatbot_env
    ```

5. **Activate the Virtual Environment:**
    ```bash
    chatbot_env\Scripts\activate
    ```
    You should see `(chatbot_env)` appear at the beginning of your command line prompt, indicating that the virtual environment is activated.

6. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Clone the Repository and Install Requirements

1. **Clone this repository:**
    ```bash
    git clone https://github.com/andrewtran1991/document-interpreter-chatbot.git
    cd document-interpreter-chatbot
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Set up the OpenAI API key:**
   - Ensure you have an OpenAI API key. You can get one from [OpenAI](https://beta.openai.com/signup/).
   - Enter your API key when prompted by the chatbot interface.

2. **Start the chatbot:**
    ```bash
    python chatbot.py
    ```
   - This will launch a Gradio interface in your browser where you can interact with the chatbot.

3. **Upload Documents:**
   - Use the upload button in the interface to add documents. The documents will be processed, and the index will be updated.

4. **Interact with the Chatbot:**
   - Enter your queries in the chatbot, and it will respond based on the content of the uploaded documents.

## Functions

### `load_documents(directory_path)`
- **Description:** Loads documents from the specified directory.
- **Parameters:**
  - `directory_path` (str): Path to the directory containing the documents.
- **Returns:** List of loaded documents.

### `create_or_update_index(documents, service_context)`
- **Description:** Creates or updates the index with the provided documents.
- **Parameters:**
  - `documents` (list): List of documents to be indexed.
  - `service_context` (ServiceContext): The service context for the language model.
- **Returns:** Updated index.

### `setup_api_key(api_key)`
- **Description:** Sets up the OpenAI API key.
- **Parameters:**
  - `api_key` (str): OpenAI API key.

### `setup_service_context_and_index(api_key)`
- **Description:** Sets up the service context and index with the provided API key.
- **Parameters:**
  - `api_key` (str): OpenAI API key.
- **Returns:** Tuple containing the service context and the index.

### `chatbot(input_text, chat_history=[], api_key=None, index=None)`
- **Description:** Handles the chatbot response generation.
- **Parameters:**
  - `input_text` (str): User input text.
  - `chat_history` (list): Chat history.
  - `api_key` (str): OpenAI API key.
  - `index` (Index): Index of documents.
- **Returns:** Tuple containing an empty string and the updated chat history.

### `handle_upload(files, index, service_context, api_key)`
- **Description:** Handles document uploads and updates the index.
- **Parameters:**
  - `files` (list): List of uploaded files.
  - `index` (Index): Current index.
  - `service_context` (ServiceContext): The service context for the language model.
  - `api_key` (str): OpenAI API key.
- **Returns:** Updated index.

## Gradio Interface

The Gradio interface provides an interactive platform to use the chatbot. It includes:

- **API Key Input:** Textbox to enter the OpenAI API key.
- **Upload Button:** Button to upload multiple documents.
- **Chatbot Interface:** Chatbox to interact with the chatbot.
- **Message Input:** Textbox to enter messages.
- **Clear Button:** Button to clear the chat history.

### How to Use the Gradio Interface

1. **Enter the API Key:** Input your OpenAI API key in the provided textbox and press Enter.
2. **Upload Documents:** Use the upload button to select and upload your documents.
3. **Chat:** Enter your queries in the message textbox and interact with the chatbot.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the Document Interpreter Chatbot! If you have any questions or need further assistance, please reach out to us at [anhltran91@gmail.com](mailto:anhltran91@gmail.com).
