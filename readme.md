# Blog-Flask

This project is a web application that uses Flask as the backend framework. It allows users to create blog posts using Python and Flask. Some of the features of this project are:

- Users can register and log in to the website using their email and password.
- Users can create, edit, and delete their own blog posts.
- Users can view other users' blog posts and leave comments.
- Users can search for blog posts by keywords or categories.
- The website is responsive and mobile-friendly.

## Technologies

This project is built with [Flask](https://flask.palletsprojects.com/) as the backend framework and uses the following technologies:

- Jinja2 as the template engine to render dynamic web pages in Flask.
- MarkupSafe to ensure that the output of Jinja2 is safe from malicious code injection.
- Flask-Bootstrap to integrate Bootstrap into Flask.
- Flask-CKEditor to integrate CKEditor, a rich text editor into Flask.
- Flask-Gravatar to integrate Gravatar into Flask.
- Flask-Login to manage user authentication and authorization in Flask.
- Werkzeug to generate and check password hass code
- SQLAlchemy as the core library for working with relational databases in Python.
- Flask-SQLAlchemy to integrate SQLAlchemy into Flask.
- Requests to make HTTP requests to external APIs or web services in Python.
- WTForms to create and validate web forms in Flask.
- Gunicorn as the web server to run the Flask application.

## Installation and Usage

To run this project, you need to have Python 3.9 or higher and pip installed on your system. You also need to have PostgreSQL installed and configured.

Clone this repository and navigate to the project folder:

```sh
git clone https://github.com/itsmacr8/blog-flask.git
cd blog-flask
```

Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```sh
pip install -r requirements.txt
```

Set the environment variables for the database URL and the secret key:

```sh
export DATABASE_URL="postgresql://username:password@localhost:5432/blog_website"
export SECRET_KEY="your-secret-key"
```

Create the database tables:

```sh
python _02_database_table_classes.py
```

Run the application:

```sh
python main.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
