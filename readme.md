# Quiz 2 API

## Overview
The **Quiz 2 API** is a RESTful API built with Django for managing a quiz application. It supports quiz categories, questions, and user interactions.

## Features
- Manage quiz categories
- Create, retrieve, update, and delete questions
- Track user scores and quiz results

## Technologies Used
- **Back-end:** Django, Django REST Framework
- **Front-end:** React (Reflex)
- **Database:** SQLite (default) or PostgreSQL
- **Development Environment:** Vagrant with VirtualBox
- **API Integration:** OpenAI API

## Setup Instructions

### Prerequisites
- Python 3.x
- Vagrant & VirtualBox
- Node.js & npm (for the front-end)

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/MohamedElderkaoui/quiz_2_api.git
cd quiz_2_api
```

2. **Start Vagrant Machine**
```bash
vagrant up
vagrant ssh
```

3. **Set Up the Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

5. **Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the Development Server**
```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Category Endpoints
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create a new category
- `GET /api/categories/{id}/` - Retrieve a specific category
- `PUT /api/categories/{id}/` - Update a category
- `DELETE /api/categories/{id}/` - Delete a category

### Question Endpoints
- `GET /api/questions/` - List all questions
- `POST /api/questions/` - Create a new question
- `GET /api/questions/{id}/` - Retrieve a specific question
- `PUT /api/questions/{id}/` - Update a question
- `DELETE /api/questions/{id}/` - Delete a question

### Quiz Endpoints
- `GET /api/quiz/start/` - Start a new quiz
- `POST /api/quiz/submit/` - Submit quiz answers
- `GET /api/quiz/results/` - Retrieve quiz results

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```bash
OPENAI_API_KEY=<your_openai_api_key>
DJANGO_SECRET_KEY=<your_secret_key>
DEBUG=True
```

## Deployment
To deploy the application, consider using services like Heroku, AWS, or DigitalOcean. Update environment variables and database settings accordingly.

## License
This project is licensed under the MIT License.

---

**Happy quizzing!** 🎯

