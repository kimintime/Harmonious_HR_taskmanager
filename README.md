# Harmonious HR App
![Static Badge](https://img.shields.io/badge/-%20?logo=python&label=Python) ![Static Badge](https://img.shields.io/badge/-%20?logo=django&label=Django) ![Static Badge](https://img.shields.io/badge/-%20?logo=javascript&label=JavaScript) ![Static Badge](https://img.shields.io/badge/v5%20-%20?logo=html5&label=HTML) ![Static Badge](https://img.shields.io/badge/v3%20-%20?logo=css3&label=CSS) ![Static Badge](https://img.shields.io/badge/SQL-%20%20?logo=postgresql&label=Postgre)

## Table of Contents
- [Quickstart](#quickstart)
- [About](#about)
    - [About the App](#about-the-app)
        - [Features](#features)
        - [Future Additions](#future-additions)
- [How to Use](#how-to-use)
    - [Harmonious Demo](#harmious-demo)
    - [Navigation Bar](#navigation-bar)
    - [Task List](#task-list)
    - [Adding and Editing Tasks](#adding-and-editing-tasks)
- [Instructions to Run Locally](#instructions-to-run-locally)
    - [Configuring the Environment](#configuring-the-environment)
        - [Activate the Virtual Environment](#activate-the-virtual-environment)
            - [On Mac and Linux](#on-mac-and-linux)
            - [On Windows](#on-windows)
    - [Install Dependencies](#install-dependencies)
    - [Run the Server](#run-the-server)
- [Setting up the Database](#setting-up-the-database)

## Quickstart
Welcome to the [Harmonious HR App demo](https://harmonioushr.azurewebsites.net). To use the demo, it's recommended to log directly into the Admin user account:
- Username 
```
admin
```
- Password
```
admin123
```

Once logged in, you can add and manage admin tasks, and view the demo for onboarding.

Alternatively, the app features secure login, so feel free to register and play around with the task manager features of the app.

[Back](#harmonious-hr-app)

## About
The Harmonious HR Task Manager App is our entry to the 2023 Mimmit Koodaa Ultrahack Hackathon. Our team consists of:  
  
- [Noona Wilskman](https://www.linkedin.com/in/wilskman/) : Team Leader, HR Expert
- [Marika Luostarinen](https://www.linkedin.com/in/marikaluostarinen/) : Creative Media Expert, Content Creator
- [Kimberly Ruohio](https://www.linkedin.com/in/kimberly-ruohio-1200/) : Software Developer
- [Nina Tulilahti](https://www.linkedin.com/in/ninatulilahti/) : Software Developer

### About the App
See the demo video for more information. Harmonious Task Manager aims to help automate common tasks for HR professionals, such as launching all tasks related to onboarding a new employee. The demo runs through the task of onboarding an employee, but all tasks would be able to launch their automated subtasks, the views and tasks differing between user roles.

[See the demo video here](https://youtu.be/CnMU3AfcVCA)

#### Features
- Secure registration and login
- Users see their own tasks and tasks are remembered
- Basic todo list functions of adding, editing, and deleting tasks
- Uploading user profile image

#### Future Additions
- User profile updating

[Back](#harmonious-hr-app)

## How to use
In order to use the app, you'll have to login. Registering a new user is free and secure, but you'll only see the todo list features of the app.

<img width="1461" alt="login" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/f26b791d-c2db-4796-96d6-4f2585a7a180">

<img width="1470" alt="register" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/656bd44a-a020-4265-8f71-cff52eacc06d">

[Back](#harmonious-hr-app)

### Harmious Demo
Logged into Admin, you'll see the tasks associated with that account, you can click on any of them to view or edit, or select `ADD+` to add a task. For the demo, select the `Onboarding` task.

<img width="1470" alt="tasks" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/fde74b7b-4c97-4025-8260-ffcd34de7c69">

<img width="1470" alt="onboardingTask" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/2465e06d-10bd-4a19-a6df-213acb818116">

Note that the task bar shows who the task was assigned to, when it was created, and it's status. You can edit the due date, select to complete the task, as well as edit it's name and description.

Click the `Launch` button to launch all automations associated with this task.

<img width="1470" alt="admin" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/539e0edb-b116-4a7d-828a-02f3fab11f6f">

Under the Admin's profile page, you can see all those tasks associated with onboarding. This is just a demo of the idea of Harmonious. These automated tasks automatically change with the task type. Select `Activate` to check off all tasks. When all tasks are selected, `New Hire Process` turns green, indicating that all the automated tasks have launched. Select `Deactivate` turn cancel launching tasks. Note that this is a demo, and nothing actually happens.

<img width="1470" alt="activatedTasks" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/b4ee0efc-fc50-47c1-b628-7a12693f98ac">

[Back](#harmonious-hr-app)

### Navigation Bar
- From the top navigation bar, you can navigate `Back` to previous page, `Home` to your task list, `Profile` to your account profile, or `Log out` to log out of the app.  `Help` brings you to this page.

### Task List
- The title bar welcomes you to the task list, showing you how many incomplete tasks you currently have. The search bar is case sensitive, and shows results once you hit enter or the `Search` button. Remove the search input and hit enter or `Search` again to see your entire task list.  
  
- The button icon to the left of each task represents its status as complete (green) or incomplete (grey). For each task you can see the title, who it is assigned to, its status, and the option to delete. Deleting a task takes you to a final confirmation screen.

<img width="1470" alt="delete" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/6f7cd52d-510e-4069-affd-4c2131ad8eea">

Either confirm the deletion or click `Back` to go back to the tasks page.

- Select the task's title to view or edit that task.

[Back](#harmonious-hr-app)

### Adding and Editing Tasks
The add and edit tasks forms are exactly the same, as shown in the demo section above. You may view, add, or edit information, and select `Submit` to save all changes, or go `Back` to discard.

### Profile page
Currently new users have a default profile image, and may update the image to a new one. Click on `Change Profile Picture` to select a new profile picture. Click on `Upload` to apply the new image or `Cancel` to exit without saving.

<img width="1470" alt="imageUpload" src="https://github.com/kimintime/Harmonious_HR_taskmanager/assets/40215472/a56bc0df-d8ca-4397-b245-ad6d31c0ea21">

---

## Instructions to run locally
- Remember to rename your example_settings.py file to settings.py, and to add your own secret key and host.
- Be sure that settings.py is included in the .gitignore
- Download and install the latest version of Python
- Download and install the latest version of Django

- Run 
```
python3 -m django --version
```
To verify the installation -or- 
```
python -m -django --version
```

[Back](#harmonious-hr-app)

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

[Back](#harmonious-hr-app)

### Install Dependencies
- With the virtual environment activated, use pip to install the project dependencies listed in the requirements.txt file:

```
pip install -r requirements.txt 

```

### Run the Server

- Run 
```
python3 manage.py runserver
```
and open the address to run the project locally -or- 
```
python manage.py runserver
```

[Back](#harmonious-hr-app)

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

[Back](#harmonious-hr-app)
