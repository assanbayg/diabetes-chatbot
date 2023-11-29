# diabetes-chatbot or DSelect

## Description

DSelect is an AI-powered chatbot designed to generate responses to diabetes mellitus questions. It utilizes generative AI, Langchain, and the Pinecon vector database. Users can interact with the chatbot through a django backend.

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
3. [Future Improvements](#future-improvements)

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

5. Install the project dependencies from the requirements.txt file:
  ```
  pipenv install -r requirements.txt
  ```

6. Start the Django backend:
  ```
  python manage.py runserver
  ```


Now, the "diabetes-chatbot" should be up and running on your local environment.

## Features

- Integrated generative AI
- Backend server built with Django for user interaction.
- I am too lazy to write it right now.

## API Endpoints

The "diabetes-chatbot" project exposes the following API endpoints for interaction:

### 1. `/blood_level/entries`

- **Method:** GET
- **Description:** Receive  all entries from the database

- **Method:** POST
- **Description:** Add a new entry to the database
- **Request Format:**
  ```json
  {
    "level": 5.2
  }

  `

### 2. `"entries/<int:pk>/"`

- **Method:** GET
- **Description:** Receive specific entry from the database

- **Method:** PUT
- **Description:** Add a new entry to the database
- **Request Format:**
  ```json
  {
    "level": 3.2
  }

  `
- **Method:** DELETE
- **Description:** Delete the entry from the database

### 3. `/meals/meals`

- **Method:** GET
- **Description:** Receive  all meals from the database

- **Method:** POST
- **Description:** Add a new meal to the database
- **Request Format:**
  ```json
  {
    "name": "meal_name",
    "portion_size": 144,
    "kcal" : 1,
    "carbs" : 1,
    "proteins": 1,
    "fats": 1,
  }
  `

### 4. `/meals/nutirion_history`

- **Method:** GET
- **Description:** Receive  all meals from the database

- **Method:** POST
- **Description:** Add a new meal to the database
- **Request Format:**
  ```json
  {
    "name": "meal_name",
    "portion_size": 144,
    "kcal" : 1,
    "carbs" : 1,
    "proteins": 1,
    "fats": 1,
  }
  `
  

## Future Improvements

In the future, I plan to make the following improvements to the "diabetes-chatbot" project:

- Enhance the quality and accuracy of answers.
- Completely migrate from Firebase to Django with PostgreSQL
- Write better README
