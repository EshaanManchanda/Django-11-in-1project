
#  Django 11 in 1 project

this is a project where it include 11 projects
## Requirements
`api_key` is required to run this project, to get `api_key` follow the below steps
maka an .env file in your Directory and add all the api keys and other requirements
`MAP_API_KEY`
`CALORIES_API_KEY`
`DEBUG=true`
`SECRET_KEY`
`TIMEZONE=Asia/Kolkata`

* Create an account in **[openweathermap.org](https://openweathermap.org/)**
* After creating account **[click here](https://home.openweathermap.org/api_keys)** to go to openweathermap api_keys section here you can generate a new `api_key` or stick with default `api_key`

* Create an account in **[api-ninjas.com](https://api-ninjas.com/api/nutrition)**
## Run Locally

Clone the project

```bash
  git clone https://github.com/EshaanManchanda/Django-11-in-1project.git .

Install dependencies

  pip install -r requirements.txt
```

* Now open `settings.py` file which is in `django_project/settings.py` and enter your **openweathermap** `api_key` in `api_key = "your api_key"` section and save the file

Run the below commands
```bash 
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

It will run the application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**Yeah!** Now the application is ready to use  
Open your browser and go to **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** and enjoy the application
