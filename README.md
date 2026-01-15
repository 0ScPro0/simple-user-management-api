# Simple User Management API

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Architecture](https://img.shields.io/badge/Architecture-Clean%20Architecture-orange.svg)

A production-ready RESTful API for user management built with FastAPI, featuring clean architecture, SOLID principles, and modern Python development practices.

## ✨ Features

- **Full CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Clean Architecture**: Separated layers (Models, Schemas, Services, Repositories, API)
- **Type Safety**: Comprehensive Python type hints throughout
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc
- **Production Ready**: Proper error handling, validation, and structured responses
- **SOLID Principles**: Well-structured code following software design best practices
- **In-Memory Storage**: Easy to understand and modify (can be replaced with any database)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/user-management-api.git
cd user-management-api
```

2. Create and activate virtual environment (recommended):

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

The API will be available at http://localhost:8000

## 📖 API Documentation

Once running, access the interactive documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔧 API Endpoints

| Method | Endpoint | Description | Status Codes | 
|------|------|------|------|
|GET	| /users/ | Get all users | 200 |
|GET | /users/{id} | Get specific user | 200, 404 |
|POST | /users/ | Create new user | 201, 400 |
|PUT | /users/{id} | Update existing user | 200, 404 |
|DELETE | /users/{id} | Delete user | 204, 404 |

## 📝 Example Requests

### Create a User
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "securepass123"}'
```

### Get All Users
```bash
curl "http://localhost:8000/users/"
```

### Get Specific User
```bash
curl "http://localhost:8000/users/1"
```

### Update User
```bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_updated"}'
```

### Delete User
```bash
curl -X DELETE "http://localhost:8000/users/1"
```

## 🏗️ Project Architecture
```text
simple-user-management-api/
├── api/
│   └── endpoints/
│       └── users.py           # API route handlers and HTTP logic
├── models/
│   └── user.py               # Data models (pure data structures)
├── schemas/
│   └── user.py               # Pydantic models for validation
├── repositories/
│   └── user_repository.py    # Data access layer (Repository pattern)
├── services/
│   └── user_service.py       # Business logic layer
├── main.py                   # Application entry point
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

### Architecture Layers
1. Models: Pure data containers using Python dataclasses
2. Schemas: Request/response validation with Pydantic
3. Repositories: Data persistence abstraction
4. Services: Business logic and use cases
5. API Endpoints: HTTP handlers and route definitions

## 🧪 Testing the API

### Using cURL (examples above)

### Using Python requests library:
```python
import requests

# Create user
response = requests.post("http://localhost:8000/users/", 
    json={"username": "testuser", "password": "testpass"})
print(response.json())

# Get all users
response = requests.get("http://localhost:8000/users/")
print(response.json())
```

### Using the interactive Swagger UI:
Visit http://localhost:8000/docs and try the endpoints directly in your browser.

## 🛠️ Development

### Adding New Features
1. Add new endpoint: Create or modify in api/endpoints/
2. Add business logic: Implement in services/
3. Add data access: Update repositories/
4. Add validation schemas: Create new Pydantic models in schemas/

### Extending the Project
- Database Integration: Replace UserRepository with SQLAlchemy, MongoDB, or other database
- Authentication: Add JWT or OAuth2 authentication
- Pagination: Implement pagination for /users/ endpoint
- Logging: Add structured logging with Python's logging module
- Testing: Add pytest tests for each layer

## 📚 Learning Resources
This project demonstrates:
- FastAPI fundamentals and best practices
- Clean Architecture implementation in Python
- SOLID principles in real-world code
- RESTful API design patterns
- Type hints and modern Python features
- Dependency injection patterns
- Error handling in web APIs

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- FastAPI for the amazing web framework
- Pydantic for data validation
- All contributors and supporters

## 📧 Contact
#### Telegram - @ScPro0
#### Email - muhamadievbogdan@gmail.com
___
#### Project Link: https://github.com/yourusername/user-management-api

### ⭐ If you found this project helpful, please give it a star! ⭐