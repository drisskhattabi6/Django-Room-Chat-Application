# Django Room Chat Application

## Overview
A real-time chat application built with Django and WebSockets (Channels) that allows users to create chat rooms, join existing rooms, and communicate in real-time. The application leverages Django Channels for handling WebSocket connections and Redis as a channel layer for message broadcasting.

## Features
- User authentication and registration
- Create and join chat rooms
- Real-time message updates
- Message history persistence

## Run Project : 

Download the project first using this cmd :

```
git clone https://github.com/drisskhattabi6/Django-Room-Chat-Application.git
```

Once the project is downloaded, navigate into the project directory:

```
cd Django-Room-Chat-Application
```

Creating static folder:

```
python manage.py collectstatic
```

By default you will find the database contains products with two user created.
So, It's optionel to apply migrations to set up the database (You will make an empty database):

```
python manage.py migrate
```

After the migrations are applied successfully, you can start the development server:

```
python manage.py runserver
```

The development server will start, and you can access the Blog Project by navigating to `http://127.0.0.1:8000/` in your web browser.

## Importent Configuration : 

Add an email with password in **setting.py** file, this email will be the sender of the reset password link to the users.

```
EMAIL_HOST_USER = 'Write Your Email Here'
EMAIL_HOST_PASSWORD = 'Your Email PASSWORD Here'
```

## Contributing to the Project

You're welcome to contribute to this project! If you'd like to make changes or improvements, here's how you can do it:

1. **Fork the Repository:** Start by forking this repository to create your own copy.

2. **Make Your Changes:** Edit the project as needed. Whether it's fixing a bug, adding a feature, or improving documentation, your contributions are appreciated!

3. **Create a Pull Request:** Once you've made your changes, submit a pull request to merge your modifications into the main project. Please provide a brief description of what you've changed.

4. **Review and Merge:** After reviewing the pull request, it can be merged into the main project.

----

Feel free to explore the project and customize it according to your requirements. If you encounter any issues or have any questions, don't hesitate to reach out!
