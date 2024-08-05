# Django TODO Application

This is a Django-based TODO application that allows users to register, log in, and manage their tasks. The project includes user authentication, task management, and a base HTML template with customizable blocks for title, links, and content.

## Features

- **User Registration**: Users can register for an account using the registration form.
- **User Authentication**: Users can log in and log out securely.
- **Task Management**: Users can create, update, and delete tasks.
- **Responsive Design**: The application is designed to be responsive and user-friendly.
- **Template Inheritance**: Uses Django's template inheritance to create a consistent layout across pages.
- **Form Handling**: Includes forms for user registration and task management.
- **Database Models**: Uses Django's ORM to define and interact with the database models.

## Project Structure

- `views.py`: Contains the view functions for handling requests.
  - `register(request)`: Handles user registration.
  - `login(request)`: Handles user login.
  - `logout(request)`: Handles user logout.
  - `task_list(request)`: Displays the list of tasks.
  - `task_create(request)`: Handles the creation of new tasks.
  - `task_update(request, id)`: Handles the updating of existing tasks.
  - `task_delete(request, id)`: Handles the deletion of tasks.
- `models.py`: Contains the database models.
  - `Task`: Represents a task with fields for title, description, and completion status.
- `forms.py`: Contains the forms used in the application.
  - `TaskForm`: Form for creating and updating tasks.
  - `UserRegistrationForm`: Form for user registration.
- `templates/`: Contains the HTML templates.
  - `base.html`: The base template file that includes the basic structure of the HTML document.
  - `register.html`: Template for the user registration page.
  - `login.html`: Template for the user login page.
  - `task_list.html`: Template for displaying the list of tasks.
  - `task_form.html`: Template for creating and updating tasks.

