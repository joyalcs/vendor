
# Vendor Management System

A Vendor Management Api for managing the profiles, orders and calculates the performance metrics.




[![Python](https://img.shields.io/badge/Python-3.11.6-blue)](https://www.python.org/downloads/release/python-3116/)
[![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-3.14.0-green)](https://pypi.org/project/djangorestframework/3.14.0/)
[![psycopg2-binary](https://img.shields.io/badge/psycopg2--binary-2.9-blue)](https://pypi.org/project/psycopg2-binary/2.9/)



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [API EndPoints](#api_endpoint)
- [Testing](#testing)

## Introduction
A Vendor Management Api for managing the profiles, orders and calculates the performance metrics.

## Features

1. Vendor
    - Create, Read, Update, Delete the Vendor profiles
    - Calculates the Vendor performance.

2. Purchase orders
   -  Create, Read, Update, Delete the Purchase orders.
    - User can view the status of the Order

3. Vendor Performance
    - Calculates the Vendor Performance including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Installation

1. Clone the git repository

```bash
   git clone https://github.com/joyalcs/vendor.git
```
2. Start a django Project
```bash
   python -m django-admin startproject vendor_management
```

3. Build the docker image

```bash
   docker-compose build
```

4. Run the docker
```bash
    docker-compose up
```
5. Commands for make migrations to database
```bash
    docker-compose run --rm app sh -c "python manage.py makemigrations"
    docker-compose run --rm app sh -c "python manage.py migrate"
```

## API EndPoints

- Vendor
| EndPoints | Method | Puropose |
| ---------|:---------:| ---------|
| /api/vendors/  | POST    |Create new vendor    |
|  /api/vendors/  | GET   | List all vendors    |
| /api/vendors/{vendor_id}/   | GET   | Retrieve a specific vendor's details   |
| /api/vendors/{vendor_id}/   | PUT/PATCH   |  Update a vendor's details.   |
| /api/vendors/{vendor_id}/   | DELETE  | Delete a vendor.   |

- Purchase orders

| EndPoints | Method | Puropose |
| ---------|:---------:| ---------|
| /api/purchase_orders/  | POST    |  Create a purchase order   |
|  /api/purchase_orders/  | GET   | List all purchase orders with an option to filter by vendor|
| /api/purchase_orders/{po_id}/   | GET   |  Retrieve details of a specific purchase order.   |
| /api/purchase_orders/{po_id}/   | PUT/PATCH   |  Update a purchase order.   |
| /api/purchase_orders/{po_id}/   | DELETE  | Delete a purchase order.   |

- Performance

| EndPoints | Method | Puropose |
| ---------|:---------:| ---------|
| /api/vendors/{vendor_id}/   | GET    |   Retrieve a vendor's performance metrics   |

## Testing
Run the test
```bash
    docker-compose run --rm app sh -c "python manage.py test"
```
