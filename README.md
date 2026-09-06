# Django E-Commerce Platform

A full-stack e-commerce web application built with **Python and Django**, with a REST API layer powered by **Django REST Framework (DRF)**. The platform provides product browsing, product search, shopping cart, checkout, order management, authentication, and API documentation through Swagger/OpenAPI.

## Features

### E-Commerce Features

* Product listing
* Product details
* Product search
* Shopping cart
* Checkout
* Order placement
* Order management
* User-specific order access
* Product image management
* Blog section
* Contact functionality
* Django admin panel
* Razorpay payment integration

### REST API Features

* RESTful API endpoints
* User registration API
* JWT-based authentication
* Login API
* JWT access and refresh tokens
* Token refresh API
* Product API
* Product detail API
* Order API
* Authenticated order access
* User-level order isolation
* API request validation
* Invalid/negative order amount validation
* Protected API endpoints
* OpenAPI schema generation
* Swagger UI API documentation

## Technologies Used

* **Programming Language:** Python
* **Web Framework:** Django
* **API Framework:** Django REST Framework
* **Authentication:** JWT / Simple JWT
* **API Documentation:** drf-spectacular / OpenAPI / Swagger UI
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Payment Gateway:** Razorpay
* **Version Control:** Git & GitHub

## Project Structure

```text
Ecomwebsite/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── Ecomwebsite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   ├── wsgi.py
│   │
│   └── templates/
│       └── index.html
│
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── shop/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── blog/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── media/
    └── shop/
        └── images/
```

## Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/JyotiRanjan784/django-ecommerce-platform.git
```

### 2. Navigate to the Project Directory

```bash
cd django-ecommerce-platform
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Open:

```text
http://127.0.0.1:8000/
```

## REST API

The project provides REST APIs using **Django REST Framework**.

The API layer includes functionality for:

* User registration
* User authentication
* JWT token generation
* JWT token refresh
* Product retrieval
* Product details
* Order creation and retrieval
* Authenticated API access
* User-specific order access
* Request validation

API endpoints are organized under the `api/` application.

### Authentication

The API uses **JWT (JSON Web Token)** authentication.

Authenticated requests require a valid access token.

Example authorization header:

```text
Authorization: Bearer <access_token>
```

Access tokens can be refreshed using the refresh-token endpoint.

## API Documentation

The project uses **drf-spectacular** to generate an OpenAPI schema and provide Swagger UI documentation.

Swagger provides an interactive interface for exploring and testing the available API endpoints.

The exact Swagger URL depends on the URL configuration in:

```text
Ecomwebsite/urls.py
```

For example:

```text
http://127.0.0.1:8000/api/docs/
```

if that route is configured in the project.

## Database

The project uses **SQLite** as the development database.

Django migrations are included for the project applications.

For production deployment, the application can be migrated to PostgreSQL or another production-ready relational database.

## Payment Integration

The application includes **Razorpay** payment integration for online payments.

### Security

Never commit sensitive credentials to GitHub.

Do not store the following directly in source code:

* Razorpay secret keys
* Django secret keys
* JWT secrets
* API keys
* Database passwords
* User passwords
* Other sensitive credentials

Sensitive configuration should be provided through environment variables.

## Applications

### `shop`

The `shop` application handles the main e-commerce functionality, including:

* Products
* Product details
* Product search
* Shopping cart
* Checkout
* Order placement
* Payment processing
* Order management
* Contact functionality

### `blog`

The `blog` application handles blog functionality, including:

* Blog posts
* Blog post details
* Comments
* Likes
* Blog management

### `api`

The `api` application provides the REST API layer, including:

* Serializers
* API views
* API URLs
* Authentication
* Product APIs
* Order APIs
* Request validation

## Admin Panel

Django's built-in admin panel can be used to manage application data such as products, orders, blog posts, and other registered models.

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## API Testing

The API can be tested using tools such as:

* Swagger UI
* Postman
* Browser/API clients
* PowerShell `Invoke-RestMethod`

When testing protected endpoints, provide a valid JWT access token in the request headers.

## Screenshots

Screenshots can be added here to demonstrate the application's main features and API documentation.

Recommended screenshots:

* Home page
* Product listing
* Product details
* Search results
* Shopping cart
* Checkout
* Payment page
* Order page
* Blog page
* Django admin panel
* Swagger UI
* API authentication
* API product endpoints
* API order endpoints

## Future Improvements

* Deploy the application to a cloud platform
* Migrate from SQLite to PostgreSQL for production
* Use environment variables for all sensitive configuration
* Improve responsive design
* Add product reviews and ratings
* Add wishlist functionality
* Improve API test coverage
* Add automated testing and CI/CD
* Add API pagination and filtering
* Add production security configuration
* Improve API error handling
* Add API rate limiting

## Author

**Jyoti Ranjan**

GitHub:
https://github.com/JyotiRanjan784
