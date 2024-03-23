# Simple Restapi with django rest_framework
## Overview

This project aims to demonstrate the implementation of a REST API in Django, leveraging the Django REST Framework (DRF). By following this guide, you'll be able to create a powerful backend for your web or mobile applications, allowing seamless interaction with your Django project's data.

## Features

- **HTTP Methods**: Utilize standard HTTP methods such as GET, POST, PUT, DELETE, etc., for interacting with resources.
- **Serializers**: Convert complex data types into native Python data types and vice versa for easy serialization and deserialization.
- **Authentication & Permissions**: Integrate authentication and permission systems to control access to API endpoints.
- **Pagination & Filtering**: Implement pagination and filtering to manage the amount of data returned by API endpoints.
- **Nested Relationships**: Represent complex data structures and model relationships in API responses.
- **Browsable API**: Use a browsable API interface for easier exploration and testing during development.


## clone the repository
```Bash
git clone https://github.com/andromedaismynexthome/RestApi_with_django.git
```
u get a file name RestApi_with_django
### go in that file
```Bash
cd RestApi_with_django
```
## now create virtual environment
```
python3 -m venv env
```
## now activate virtual environment
```
source env/Scripts/activate
```
## Now install depencies
```
pip install django && djangorestframework
```
## now everything is set and now run server
```
cd core && python manage.py runserver
```
