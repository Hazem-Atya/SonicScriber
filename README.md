# SonicScriber

This is a mini project for manually transcripting audio data.

![image](https://github.com/Hazem-Atya/SonicScriber/assets/53778545/0bddbe09-0349-4897-89ae-abb0e2200e34)

## Project Overview

### Technologies:
- Vue.js frontend
- Restful API with Django Rest Framework
- PostgreSQL Database
- Azure Blob storage for storing the audio files.

### Run the Django project
* Create a .env inside the backend directory and fill it with your variables
```env
DB_NAME = 
DB_USER = 
DB_PASSWORD = 
DB_HOST = 
DB_PORT = 

# Azure Storage account variables
STORAGE_ACCOUNT_NAME = 
STORAGE_ACCOUNT_KEY =  
CONTAINER_NAME = 
```
* Create a virtual environment then activate it
```bash
python -m venv venv 
# windows machine
venv\Scripts\activate.bat

#mac/linux
source venv/bin/activate
```
* Install the dependencies
```bash
 pip install -r requirements.txt
```
* Run these commands for the django project
```bash
python manage.py migrate
python manage.py save_character_set
# To upload the files run this command inside the django project:
python manage.py upload_audios
```
* Run the server
```bash
python manage.py runserver

```

### Run the Vue.js project

```bash
npm i 
npm run server
```
