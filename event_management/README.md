# Event Management API

This is a Django-based Event Management API designed to facilitate the management of events, users, and related functionalities. The API provides endpoints for creating, retrieving, updating, and deleting event information, making it suitable for various event management applications.

## Features

- User authentication and management
- CRUD operations for events
- Integration with Django Admin for easy management
- RESTful API design using Django REST Framework

## Project Structure

```
event-management-api
├── event_management
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── events
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the migrations:
   ```
   python manage.py migrate
   ```

2. Start the development server:
   ```
   python manage.py runserver
   ```

3. Access the API at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
# Users App Documentation

## Overview
The `users` app is designed to handle user-related functionality for the Social Media API project. It includes features such as user registration, authentication, and profile management.

## Setup Instructions
1. **Install Dependencies**: Ensure that Django and Django REST Framework are installed in your environment.
2. **Add to Installed Apps**: Include the `users` app in your project's `settings.py` file under `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       ...
       'users',
       ...
   ]
   ```

## Usage
- **User Registration**: Users can register through the `/register` endpoint.
- **User Login**: Users can log in using the `/login` endpoint, which returns a token for authentication.
- **Profile Management**: Users can manage their profiles through the `/profile` endpoint.

## Features
- Custom user model extending Django's `AbstractUser`.
- Token-based authentication using Django REST Framework.
- Serializers for converting user data to and from JSON format.

## Testing
To run tests for the `users` app, use the following command:
```bash
python manage.py test users
```

## Contributing
Contributions to the `users` app are welcome. Please follow the project's contribution guidelines.