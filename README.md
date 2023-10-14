# Social Media Post Generator

## Introduction

This Python application uses OpenAI's GPT-3.5 Turbo to generate social media posts and accompanying images. It provides the ability to create posts in various languages and for different social media platforms.

## Prerequisites

Before you can run this application, you need to set up the following prerequisites:

- **Python**: Make sure you have Python installed on your system.

- **OpenAI API Key**: You need an OpenAI API key to use this application. You can obtain one by signing up on the [OpenAI platform](https://beta.openai.com/signup/). Replace `YOUR_OPEN_AI_API_KEY` in the code with your actual API key.

- **Streamlit**: Streamlit is a Python library for creating web apps with minimal code. You can install it using pip:

   ```bash
   pip install streamlit
   ```
## Getting Started

- Clone the repository or save the code to a Python file.

- Replace YOUR_OPEN_AI_API_KEY in the code with your actual OpenAI API key.

- Install the required libraries as mentioned in the prerequisites, i.e.
  ```bash
  pip install openai streamlit
  ```
  If you are using pip.

- Run the application using the following command:
  ```bash
  streamlit run your_app_file.py
  ```
  Replace your_app_file.py with the actual name of the Python file containing the code.

- The application will open in your web browser.

## Usage

- Select the desired language for the social media post from the dropdown menu.

- Enter a prompt for the post in the provided text area.

- Optionally, specify a social media platform for the post.

- Click the "Generate" button to create a social media post and an accompanying image.

- The generated post and image will be displayed on the web page.

## How it Works
The application utilizes OpenAI's GPT-3.5 Turbo model to generate text and images based on the provided prompts. You can customize the prompts to generate content for different languages and social media platforms.

## Credits
This application was created by Team Corazon.

*Note: This readme assumes that you have already obtained the necessary API key from OpenAI and installed the required libraries. Make sure to keep your API key secure and do not share it in public repositories.*
