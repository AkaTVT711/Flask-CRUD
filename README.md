## Overview

This is a pool where I can swim with Flask-Python frameworks.

## Prerequisites

- `Up-to-date dependencies`
- `Database`: `SQLite`, `MySql`
- `DB Tools`: SQLAlchemy ORM, `Flask-Migrate`
- `Authentication`, Session Based
- `Docker`, `Flask-Minify` (page compression)

## Getting Started

To get started, follow these steps:

1. Clone the repository to your local machine:
   git clone https://github.com/AkaTVT711/Flask-CRUD.git
   cd Flask-CRUD


2. Creates a virtual environment named 'env'

   ```virtualenv env```


3. Set up a virtual environment

- via WSL:
  ```
   $ virtualenv env
   $ source env/bin/activate
   $ pip install -r requirements.txt
  ```
- via Windows:
   ```
   $ virtualenv env
   $ .\env\Scripts\activate
   $ pip install -r requirements.txt
  ```
4. Set Up Flask Environment
   ```
   $ export FLASK_APP=run.py
   $ export FLASK_ENV=development
   ```

6. Run the Flask application:
   ```
   $ flask run
   // OR
   $ flask run --cert=adhoc # For HTTPS server
   // OR
   $ flask run --host=localhost
   ```

7. Check the url http://localhost:5000

```
[2024-04-05 09:25:32,772] INFO in run: DEBUG            = True
[2024-04-05 09:25:32,773] INFO in run: Page Compression = FALSE
[2024-04-05 09:25:32,773] INFO in run: DBMS             = mysql+mysqldb://MYSQL_USER:MYSQL_PASSWORD@localhost:3306/YOUR_DATABASE
[2024-04-05 09:25:32,773] INFO in run: ASSETS_ROOT      = /static/assets
 * Serving Flask app 'run.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
```

![Screenshot 2024-04-05 093037.png](Screenshot%202024-04-05%20093037.png)

## Project Structure

The project structure is organized as follows:

```bash
 < PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |-- news/                           # A simple app that serve HTML files
   |    |    |-- __init__.py                # Initializes the news.
   |    |    |-- models.py                  # Defines data models specific to the news.
   |    |    |-- forms.py                   # Contains Flask-WTF forms for handling user input related to news.
   |    |    |-- routes.py                  # Defines URL routes and corresponding view functions for the news. 
   |    |    |-- utils.py                   # Contains utility functions used within the news.
   |    |-- products/                       # A simple app that serve HTML files
   |    |    |-- __init__.py                # Initializes the products.
   |    |    |-- models.py                  # Defines data models specific to the products.
   |    |    |-- forms.py                   # Contains Flask-WTF forms for handling user input related to products.
   |    |    |-- routes.py                  # Defines URL routes and corresponding view functions for the products. 
   |    |    |-- utils.py                   # Contains utility functions used within the products.
   |    |-- promocodes/                     # A simple app that serve HTML files
   |    |    |-- __init__.py                # Initializes the promocodes.
   |    |    |-- models.py                  # Defines data models specific to the promocodes.
   |    |    |-- forms.py                   # Contains Flask-WTF forms for handling user input related to promocodes.
   |    |    |-- routes.py                  # Defines URL routes and corresponding view functions for the promocodes. 
   |    |    |-- utils.py                   # Contains utility functions used within the promocodes.
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

[Original] Source reference: https://github.com/app-generator/flask-datta-able