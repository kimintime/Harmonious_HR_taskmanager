# Harmonious HR App

## Instructions to run locally
- Remember to rename your example_settings.py file to settings.py, and to add your own secret key and host.
- Be sure that settings.py is included in the .gitignore
- Download and install the latest version of Python
- Download and install the latest version of Django

- Run 
```python3 -m django --version```
To verify the installation -or- 
```python -m -django --version```

### Configuring the Environment

- Navigate to the project directory in your terminal or command prompt and create a virtual environment. This isolates the project's dependencies from your global Python environment: 

```
python -m venv venv

```

#### Activate the virtual environment
##### On Mac and Linux:
```
source venv/bin/activate

```

##### On Windows:
```
venv\Scripts\activate

```
### Install Dependencies
- With the virtual environment activated, use pip to install the project dependencies listed in the requirements.txt file:

```
pip install -r requirements.txt 

```

### Run the Server

- Run 
```python3 manage.py runserver```
and open the address to run the project locally -or- 
```python manage.py runserver```

## Setting up the database
- In your settings.py, find or add  this to the `DATABASES`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Or your database host
        'PORT': '',           # Default PostgreSQL port
    }
}

```

- Replace 'your_db_name', 'your_db_user', and 'your_db_password' with your PostgreSQL database name, username, and password respectively.

- Create a database in PostgreSQL that matches the name specified in your Django settings ('NAME': 'your_db_name'). You can do this through the PostgreSQL command line, a GUI tool like pgAdmin, or via Django management commands.

```
psql -U your_username -h your_host #leave out -h if it's localhost

```

```
CREATE DATABASE your_db_name;

```

- If using VS Code, then the PSQL Explorer extension will be your friend.

- Now, you can run Django's `makemigrations` and `migrate` commands to create the necessary tables in your PostgreSQL database:

```
python manage.py makemigrations
python manage.py migrate

```
