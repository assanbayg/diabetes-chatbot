# Django REST API Documentation

This Django project provides several API endpoints for managing different entities. Below are the details for each set of endpoints.

## Blood Level API

### Blood Level Entries

- **List Blood Level Entries**
  - **URL:** `/blood_level/entries/`
  - **HTTP Method:** `GET`
  - **Description:** Retrieve a list of all blood level entries in the database.

- **Create Blood Level Entry**
  - **URL:** `/blood_level/entries/`
  - **HTTP Method:** `POST`
  - **Description:** Create a new blood level entry in the database.

- **Retrieve, Update, or Delete Blood Level Entry**
  - **URL:** `/blood_level/entries/<int:pk>/`
  - **HTTP Methods:** `GET`, `PUT`, `DELETE`
  - **Description:** Retrieve, update, or delete a specific blood level entry identified by its primary key (`pk`).

## Meals and Nutrition History API

### Meals

- **List Meals**
  - **URL:** `/meals/`
  - **HTTP Method:** `GET`
  - **Description:** Retrieve a list of all meals in the database.

- **Create Meal**
  - **URL:** `/meals/`
  - **HTTP Method:** `POST`
  - **Description:** Create a new meal entry in the database.

- **Retrieve, Update, or Delete Meal**
  - **URL:** `/meals/<int:pk>/`
  - **HTTP Methods:** `GET`, `PUT`, `DELETE`
  - **Description:** Retrieve, update, or delete a specific meal identified by its primary key (`pk`).

### Nutrition History

- **List Nutrition History Entries**
  - **URL:** `/nutrition_history/`
  - **HTTP Method:** `GET`
  - **Description:** Retrieve a list of all nutrition history entries in the database.

- **Create Nutrition History Entry**
  - **URL:** `/nutrition_history/`
  - **HTTP Method:** `POST`
  - **Description:** Create a new nutrition history entry in the database.

- **Retrieve, Update, or Delete Nutrition History Entry**
  - **URL:** `/nutrition_history/<int:pk>/`
  - **HTTP Methods:** `GET`, `PUT`, `DELETE`
  - **Description:** Retrieve, update, or delete a specific nutrition history entry identified by its primary key (`pk`).

## Insulin API

### Insulin Types

- **List Insulin Types**
  - **URL:** `/insulin/types/`
  - **HTTP Method:** `GET`
  - **Description:** Retrieve a list of all insulin types in the database.

### Insulin Takes

- **List Insulin Takes**
  - **URL:** `/insulin/takes/`
  - **HTTP Method:** `GET`
  - **Description:** Retrieve a list of all insulin takes in the database.

- **Create Insulin Take**
  - **URL:** `/insulin/takes/`
  - **HTTP Method:** `POST`
  - **Description:** Create a new insulin take entry in the database.

- **Retrieve, Update, or Delete Insulin Take**
  - **URL:** `/insulin/takes/<int:pk>/`
  - **HTTP Methods:** `GET`, `PUT`, `DELETE`
  - **Description:** Retrieve, update, or delete a specific insulin take identified by its primary key (`pk`).

## Custom User API

### Users

- **List Users**
  - **URL:** `/users/`
  - **HTTP Method:** `GET`
  - **Description:** Retrieve a list of all custom users in the database.

- **Create User**
  - **URL:** `/users/`
  - **HTTP Method:** `POST`
  - **Description:** Create a new custom user entry in the database.

- **Retrieve, Update, or Delete User**
  - **URL:** `/users/<int:pk>/`
  - **HTTP Methods:** `GET`, `PUT`, `DELETE`
  - **Description:** Retrieve, update, or delete a specific custom user identified by its primary key (`pk`).
    
