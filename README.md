# Task Management App Mk I - Lightweight

A lightweight, web-based task management application built with Flask, SQLite, and Bootstrap. This application allows users to register, log in, and manage their tasks with a clean and modern interface.

## Features

- User authentication (registration, login, logout)
- Create, view, update, and delete tasks
- Responsive and user-friendly interface with Bootstrap

## Getting Started

### Prerequisites

- Python 3.6+
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Anastasios3/Task-Managment-App-Mk-I--lightweight.git
    cd Task-Managment-App-Mk-I--lightweight
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Initialize the database:**

    ```sh
    python
    ```

    Then, run the following commands inside the Python shell:

    ```python
    from app import app
    from extensions import db

    with app.app_context():
        db.create_all()
    exit()
    ```

5. **Run the application:**

    ```sh
    python app.py
    ```

    Visit `http://127.0.0.1:5000/` in your web browser to see the application in action.

## Contributing

1. **Fork the repository**
2. **Create a new branch**

    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Commit your changes**

    ```sh
    git commit -m 'Add some feature'
    ```

4. **Push to the branch**

    ```sh
    git push origin feature/your-feature-name
    ```

5. **Open a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
