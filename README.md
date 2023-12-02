# diabetes-chatbot or DSelect

## Description

DSelect is an AI-powered chatbot designed to generate responses to diabetes mellitus questions. It utilizes generative AI, Langchain, and the Pinecon vector database. Users can interact with the chatbot through a django backend.

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
3. [API Endpoints](#api-endpoints)
4. [Future Improvements](#future-improvements)

## Installation

To set up the "diabetes-chatbot" project, follow these steps:

1. Clone the repository:
  ```
  git clone https://github.com/assanbayg/diabetes-chatbot.git
  ```

2. Navigate to the project directory
  ```
  cd diabetes-chatbot
  ```
3. Create a virtual environment (recommended):
  ```
  pipenv install django
  ```
4. Activate the virtual environment:
  ```
  pipenv shell
  ```

5. Start the Django backend:
  ```
  python manage.py runserver
  ```

Dont' forget to set up following env variables:
  - OPENAI_API_KEY
  - PINECONE_API_KEY
  - PINECONE_API_ENV

Now, the "diabetes-chatbot" should be up and running on your local environment.

## Features

- Integrated generative AI
- Backend server built with Django for user interaction.
- I am too lazy to write it right now.

## [API Endpoints](ENDPOINTS.md)

## Future Improvements

In the future, I plan to make the following improvements to the "diabetes-chatbot" project:

- Enhance the quality and accuracy of answers.
