# Django E-Commerce Platform

A full-stack e-commerce web application built using Python and Django. The platform provides product browsing, product search, shopping cart, checkout, order placement, order tracking, payment integration, and a blog section.

## Features

- Product listing
- Product details
- Product search
- Shopping cart
- Checkout
- Order placement
- Order tracking
- Razorpay payment integration
- Blog section
- Contact page
- Admin panel
- Product image management

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Payment Gateway:** Razorpay
- **Version Control:** Git & GitHub

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

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

---

## Database

The project uses **SQLite** as the development database.

Django migrations are included for the `shop` and `blog` applications.

---

## Payment Integration

The application includes **Razorpay** payment integration for online payments.

> **Security:** Never commit real Razorpay API keys, Django secret keys, passwords, or other sensitive credentials to a public GitHub repository. Use environment variables for sensitive configuration.

---

## Applications

### Shop

The `shop` application handles the main e-commerce functionality, including:

- Products
- Product details
- Product search
- Shopping cart
- Checkout
- Order placement
- Payment processing
- Order tracking
- Contact functionality

### Blog

The `blog` application handles the blog functionality, including:

- Blog posts
- Blog post details
- Comments
- Likes
- Blog management

---

## Admin Panel

Django's built-in admin panel can be used to manage application data such as products, orders, blog posts, and other registered models.

To create an administrator account:

```bash
python manage.py createsuperuser
```

Then start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

---

## Screenshots

Screenshots can be added here to demonstrate the main features and user interface of the application.

Recommended screenshots:

- Home page
- Product listing
- Product details
- Search results
- Shopping cart
- Checkout page
- Payment page
- Payment success page
- Order tracking
- Blog page
- Admin panel

---

## Future Improvements

- Deploy the application to a cloud platform
- Migrate from SQLite to PostgreSQL for production
- Use environment variables for sensitive configuration
- Improve responsive design
- Add product reviews and ratings
- Add wishlist functionality
- Improve security and production configuration
- Add automated testing

---

## Author

**Jyoti Ranjan**

GitHub:  
https://github.com/JyotiRanjan784