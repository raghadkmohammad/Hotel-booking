 Hotel Booking System API

This is a simple RESTful API for a hotel booking system built with Django and Django REST Framework.

## Features
- User Registration with roles: Visitor, Booking Manager, Customer Service, Investor
- Booking Management
- Investment Management

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Run server:
```bash
python manage.py runserver
```

## API Endpoints
- `/api/users/`
- `/api/bookings/`
- `/api/investments/`

## License
MIT
