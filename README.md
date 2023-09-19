Brian Yu [brian@cs.harvard.edu](mailto:brian@cs.harvard.edu)  
David J. Malan [malan@harvard.edu](mailto:malan@harvard.edu)
# Harvard University - CS50 Web Programming with Python and Javascript<br>
## ARTAX - Capstone project by M. N. Zeenny
Project Name: Artax  
Project Completed on: Monday, September 11, 2023  
[Marc's me50 GitHub](https://github.com/me50/marcnz06.git)  
[Video Presentation of the web app]  
Email: [marcnzeenny@outlook.com](mailto:marcnzeenny@outlook.com)  
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## About
The project itself is a Library Management System (LMS) for law firms. It handles a lot of complex aspects ranging from user authentication to content management to logging.

## Setup

1. Unzip the project.
2. In your terminal, `cd` into the zeennylawfirm directory.
3. Run `python manage.py makemigrations` auctions to make migrations for the auctions app. 
4. Run `python manage.py migrate` to apply migrations to your database.
5. Run `python manage.py runserver` to activate your development server. You can also run `python manage.py runserver --insecure` with `debug=False` to be able to view the custom-made 403, 404... error pages without the need to have a production server set up.
6. Run `python manage.py createsuperuser` and follow the onscreen instructions to create a superuser. The latter will be needed to be able to access basic Artax needs.

# Files and project modules
## Project Structure
```
├── artax
│   ├── management
│   │   ├── commands
│   │   │    └── setup_permissions.py
│   │   ├── static
│   │   │   └── artax
│   │   │       ├── css
│   │   │       ├── fonts
│   │   │       ├── img
│   │   │       ├── js
│   │   │       └── vendor
│   │   ├── templates
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   ├── 500.html
│   │   │   └── artax
│   │   │       ├── all-books.html
│   │   │       ├── contact.html
│   │   │       ├── dashboard.html
│   │   │       ├── email-verify-email.html
│   │   │       ├── email_confirmation_email.html
│   │   │       ├── email_confirmation_invalid.html
│   │   │       ├── email_confirmed.html
│   │   │       ├── faq.html
│   │   │       ├── layout.html
│   │   │       ├── login.html
│   │   │       ├── new-book.html
│   │   │       ├── queries-books.html
│   │   │       ├── query-results.html
│   │   │       ├── record-404.html
│   │   │       ├── record-book.html
│   │   │       ├── register.html
│   │   │       └── users-profile.html
│   │   ├── templatetags
│   │   │   └── custom_tags.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── logs
│   ├── app.log
│   ├── books.log
│   └── users.log
├── media
│   ├── cover
│   └── summary
├── zeennylawfirm
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── __init__.py
├── manage.py
├── README.md
└── requirements.txt
```
## File contents
`setup_permissions.py`: Creates a custom manage.py command named `setup_permission` that sets up the user permissions.  
`403.html`, `404.html`, `500.html`: A custom error page when each of the corresponding error (403, 404 and 500) are thrown.  
`all-books.html`: Page containing a datable containing all books where each row is clickable and leads to `record-book.html` being displayed.  
`contact.html`: Law firm contact information + location based on Google Maps.  
`dashboard.html`: ARTAX 's dashboard where you can access the View, New, Review functions + see the past 7 actions made by users + check the 5 most recent books added to the database.  
`email-verify-email.html`: Page where the administrator is warned that an email with a verification link has been sent to the user's inbox.  
`email_confirmation_email.html`: Email content sent to users' inboxes to verify their email address.  
`email_confirmation_invalid.html`: Link for verification not valid.  
`email_confirmed.html`: Link valid and account verified.  
`faq.html`: A page where administrators can insert useful commonly asked questions with their respective answers  
`layout.html`: Base template of this website with sidebar, header, footer...  
`login.html`: Login page of all users.  
`new-book.html`: Template that lets users add records to the database.  
`queries-books.html`: Page that contains a query form with filters and two other forms that let you select your record based on their ID or their Special ID (lib_id).  
`query-results.html`: Displays the results of the query.  
`record-404.html`: 404 Error page when a record isn't found.  
`record-book.html`: Displays a record's details + the ability to edit them, to remove and/or upload a new book cover or summary and to delete the whole record.  
`register.html`: Register page for new users. Only available to admins.  
`users-profile.html`: Page for each user where there details are viewed and can be modified.  
`custom_tags`: The `nav_link` custom tag is meant to be used in django templates. It comes handy in a sidebar, it detects the current page we are in and makes the button in the sidebar active. And then, when we switch to another one, it changes automatically.  
`admin.py`: File where we specify what models have forms built-in in the admin dashboard.  
`app.py`: Some settings specific to the artax app like setting the app's name...  
`models.py`: File where models' blueprints are written with each model's fields, methods...  
`urls.py`: All the app's (artax) urls.  
`views.py`: Web app views, each one associated with a controller.
`app.log`: When DEBUG=FALSE, django logs everything with a level of warning or higher in this file.  
`books.log`: Logs when a user adds, alters, deletes a record and logs the current record details (When a record is added or altered).  
`users.log`: Logs everything related to users.  
`pymedia/cover` and `media/summary`: Every book has its cover and summary uploaded to the corresponding directory.


# Distinctiveness and Complexity

This project represents a significant departure from standard course assignments and represents a unique combination of complexity and innovation. Its uniqueness lies in several key aspects that distinguish it  from  other projects in the course:

## Implementation

Users accounts are first created by an administrator (more on that below) where first name, last name, email address, password and clearance are required. 
As information security is a game changer in a law firm system, the clearance field is a very important part of the web app. Indeed, there are 4 clearance level for users.  

- Visitor (View and Review any book record.)
- Lawyer (View, review and alter any book record.)
- Office Administrator (View, review, alter add and delete any book record in addition to user management and access to the admin panel)
- System Administrator (Unrestricted access to all data and functionality within the application as well as having the highest level of control and authority within the Django project)

After a thorough client-side verification (with javascript) and then a deeper server-side verification(python in the backend), an nicely formatted email is sent to the email address specified with a link containing a unique token, to be used for verification. 
If verification is successful, the user is redirected to his profile where he can edit additional fields such as phone number, job, description...
The limit of his actions is determined by his clearance.

Users actions are also logged in 3 different files in the `logs` directory: `app.log` is where all errors are written, `books.log` for every action related to the books table beginning with adding a new record to editing it and finally deleting and finally `users.log` where all users actions like logging in, logging out... are recorded and timestamped accordingly. 


Technologies used in this project:
- Django
- JavaScript
- HTML + CSS
- Bootstrap
- Django QR Codes
- Logging


## Purpose of this web app

This web app is a content management system, and more specifically a book management system custom-made for law firms.
It encompasses everything needed to have a good, performing and reliable system. 
Let's take for example a user named Marc with system administrator privileges:
1. Marc can add books to the database by going to /books/new-record/. He will be prompted by a well-designed form with Bootstrap with proper user experience and validation.
The model Book (defined in models.py) comes into play where it logs 
With security in mind, he can upload a book summary as a scanned file (with pdf as the only supported file type) and a book cover (with limited photo types).
There is also the book location, type, language and author who are stored in the database as foreign keys. To add manage those fields, an administrator can just go to the admin panel. He will be able to add any object he wants.
A special ID (lib_id field) is automatically generated by combining the type code of each book type with the ID of each book given its type. So if we have 5 book of type commercial, the 6th one will have a special ID of FIN6.
A QR Code for each record is also generated by dynamically generating the url that will take the user to the record. 
2. Each record has its own dedicated page by simply going to `books/<x>/` where `x` is the auto-number generated (!= lib_id). Marc can view the books details, or download the books QR Code. He can also add and/or edit data related to the record. Indeed, he can modify 10 of the 19 book fields manually. Moreover, he can add or delete any of the book's cover or summary very easily.  
3. Marc will also be able to delete any record he would like by simply going to the "Delete Record" tab, pressing on the "Proceed" button, and finally "Delete Permanently" in the delete pane.
4. In addition to view, adding and deleting, the user can query the database by going to `books/queries/`. He will be asked to make a choice between being redirected to the exact record by entering the ID or Special ID on one hand, or entering data in a Multi Filter Form. The latter will enable the user to limit the dataset he is searching in and finding the appropriate record in record time. 


The capstone project is simply miles away of any other project made in this course.
Here are few of the goals and objectives set and achieved in this project:

- Stability (easy postgres integration).
- Good-looking, practical and well thought of design + mobile responsive.
- Optimized for small to medium scale law firms.
- Security (CSRF, Email verification, SQL Injection...).
- Maintainable (Django)
- User experience (JavaScript)

## In-Depth Documentation
In addition to its technical complexity, this project also stands out for its comprehensive documentation. The README.md file you are currently reading is just one aspect of many ongoing documentation efforts. This is a testament to the dedication and commitment to ensuring that users and potential collaborators have all the information they need to understand and effectively use this unique system.

## Project's future

This Django project was a priority for me, and I worked on it to achieve perfection because of my plans for its future. Indeed, I intend to deploy this web app as an intranet in my dad's law firm, named Zeenny Law. To complete this website, it took me as much time as all the other projects combined.
I learned new technologies, didn't limit myself to what I learned in the course and pushed the boundaries of what a Capstone Project can be.


In short, this capstone project goes  beyond  course requirements to provide a complex, industry-specific solution. It reflects a deep understanding of the challenges facing law firms and leverages cutting-edge technologies to solve them. The complexity and uniqueness of this project is evident in its specialized features, meticulous security measures and comprehensive documentation.




