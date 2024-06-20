# Task Manager Application

## Overview

The Task Manager Application is a comprehensive tool designed to help full stack web developers, hobbyists, and professionals organize their tasks efficiently. This project focuses on tasks management with features such as user authentication, task creation, prioritization, and task completion. The application is built using Flask, a lightweight web framework for Python, and utilizes SQLite for database management.

## Features

### User Authentication

- **Registration**: Users can create an account by providing an email and password.
- **Login**: Registered users can log in using their email and password.
- **Logout**: Users can securely log out of their account.

### Task Management

- **Create Task**: Users can create new tasks with a title, description, and priority level (Low, Normal, High).
- **View Tasks**: Users can view a list of all their tasks.
- **Update Task**: Users can update the title, description, and priority of their tasks.
- **Delete Task**: Users can delete tasks that are no longer needed.
- **Complete Task**: Users can mark tasks as completed.
- **Sort Tasks**: Tasks can be sorted by creation date or priority in both ascending and descending order.

### Priority Levels

Tasks can be assigned one of three priority levels:
- **Low Priority**: For tasks that are not urgent.
- **Normal Priority**: For regular tasks.
- **High Priority**: For tasks that require immediate attention.

### Sidebar Navigation

The sidebar provides easy navigation and quick access to task creation and filtering functions. It includes:
- **Create Task Button**: A button to open a form for creating new tasks.
- **Priority Filters**: Buttons to filter tasks by priority (Low, Normal, High).
- **Completion Filters**: Buttons to filter tasks by their completion status (Active, Completed).
- **Logout Button**: A button to log out of the application.

### Footer

A footer is displayed at the bottom of the task list, providing a clean and consistent user experience.

## Next Steps

The following features are planned for future development:

1. **Task Timestamps**: Add the ability to record the creation timestamp and set a due date for each task.
2. **Advanced Sorting**: Enhance sorting functionality to include sorting by due date and other criteria.
3. **Sidebar Improvements**: Add filtering options in the sidebar to view active and completed tasks separately. Ensure all buttons in the sidebar are well-styled and user-friendly.

## Technologies Used

### Flask

Flask is a lightweight WSGI web application framework in Python. We chose Flask for its simplicity and flexibility, allowing for quick development and easy integration with other tools.

### SQLite

SQLite is a C-language library that provides a lightweight, disk-based database. It is a popular choice for applications where simplicity, ease of use, and low resource usage are key requirements.

### Flask-Login

Flask-Login is a user session management library for Flask. It provides user session management capabilities, such as login, logout, and session tracking.

### Flask-WTF

Flask-WTF is an extension of Flask that integrates WTForms, allowing for the creation and management of web forms in a clean and simple manner.

### Jinja2

Jinja2 is a modern and designer-friendly templating engine for Python. It is used in this project to create dynamic HTML pages.

### Bootstrap

Bootstrap is a powerful front-end framework for faster and easier web development. It provides a responsive, mobile-first layout and reusable CSS components.

## Installation and Usage

To get the Task Manager Application running locally on your PC, follow these steps:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Anastasios3/Task-Managment-App-Mk-I--lightweight.git
   cd Task-Managment-App-Mk-I--lightweight
   ```

2. **Create a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   ```sh
   python
   ```

   Inside the Python shell, run:

   ```python
   from app import app
   from extensions import db

   with app.app_context():
       db.create_all()
   exit()
   ```

5. **Run the Application**

   ```sh
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Conclusion

The Task Manager Application is designed to be an efficient and user-friendly tool for managing tasks. With features like user authentication, task prioritization, and completion tracking, it serves as a comprehensive solution for personal and professional task management. Future enhancements will focus on adding timestamps, advanced sorting, and improving the sidebar functionality to provide an even better user experience.
