# Scraping Server

#### Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [BOOTSTRAP](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

  

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.11 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
   
4. Start project:
    ```bash
   python manage.py runserver
   ```
