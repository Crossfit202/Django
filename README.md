# Overview

The Web App I created is a book listing site that allows you to create listings for old textbooks that you no longer need for school.

To open up the test server for the django framework, you create the project by running "django-admin startproject (then you eneter the project name)" and "python manage.py startapp (app name)" and these create the django files and folders that you need. To start the server, run "python manage.py runserver". This runs the manage.py file that is automatically created and has a function that runs your web app. You copy the link that the terminal gives you that looks like this, "Starting development server at http://127.0.0.1:8000/" and paste it in your browser. Now you can view what is initially created and anything that you are developing.

My purpose for creating this software is to learn how the Django framework works. This is my first project using the framework and I wanted to create a website where I could learn to work with loggin in, logging out, and getting information from databases.

[Software Demo Video](https://youtu.be/RdNhTAJdP68)

# Web Pages

The web pages that I learned to create in this project are:

- base.html: This page is the main page that all th rest of them are based on. Every other html file in the project are extensions of this file. This has the bootstrap styling, nav bar, header, and body of the webstie. This is where all of the links to the pages are located so that when users select an option, Django searches the project for the path that is linked and opens the models/views associated with that url path.

- home.html: This page is the page that goes through all of the posts that users have created and displays them for everyone to see. It lists out only a few of the fields that users enter when they create the listing.

- about.html: This is a very simple about page that tells the user about the purpose of the page. A simple h1 tag and a p tag.

- post_detail: This page displys all of the details about a post when you click on it. It generates a lot of the content from the database of stored posts.

- post_confirm_delete: This page appears when you choose to delete a post and makes sure that you really want to. It generates buttons to proceed or cancel

- post_form: This generates the form to make a new listing.

- login.html: This generates a form for users to login and provides a link to make an account if they don't have one

- logout.html: This generates a message that tells the user they have been logged out and gives a link for them to log in again if they want.

- profile.html: This page shows the information about the user that is logged in. It only contains the username and email right now.

- register.html: This generates the fiels necessary to make an account and stores the account for future login.

# Development Environment

Django Framework: The web application was developed using Django, a high-level Python web framework. Django provides a robust set of tools and features for building web applications efficiently.

Python: The programming language used for developing the website is Python. Python is known for its simplicity, readability, and vast ecosystem of libraries and frameworks.

BootStrap: This is a popular front-end framework that provides a collection of pre-designed and reusable CSS classes and components. It is used to build responsive websites quickly and easily.

SQL Lite 3: This is the defualt database that django provides for us to start building the project.

# Useful Websites

Websites that I found helpful for this project are as follows:

- [BootStrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [W3Schools Django](https://www.w3schools.com/django/django_intro.php)
- [YouTube Django Series](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

# Future Work

Changes I want to make in the future are:

- Implement search function. I want people to be able to search for a specific book to see if someone has listed it for sale. I would want to be able to search by class and book.
- I want to make a feature to request a book. An email would be sent to those who actively post on the site requesting the book.
- I want to work on the design more. I was focused on functionality moreso than style and I would like to customize the website more in terms of branding.
