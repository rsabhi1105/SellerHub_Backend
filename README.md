# SellerHub_Backend
# Seller Hub

### _Mulltivendor Ecommerce Website_

_seller hub is basically mulltivender site like amezon , flipkart etc. which is connect seller to custmer_

# Seller Hub

### Multivendor Ecommerce Website

seller hub is basically mulltivender site like amezon , flipkart etc. which is connect seller to custmer

## Features

- Frontend

        - Website
            - Home page
                - papuler categorys
                - papuler products
                - papuler Seller
                - custmer reviews & rating
                - footer
            - All categorys list
            - All products list according to categorys
                - sort according to price
            - products details
            - checkout page 
            - order success and faliar page

------------------------------------

- Backend

        - Authentication 
            - Simplejwt
            - Token based authentication

        - customer panel 
            - Registration
            - login
            - forget password
            - Dashboard
                - order
                - profile
                - change password
                - cart

        - Seller pannal
            - Registration
            - login
            - forget password
            - Dashboard
                - products
                - product rateing
                - order
                - profile
                - change password
                - customer 
                - manage products
                - manage custmer

        - Admin pannal
            - manage Seller
            - manage custmer
            - manage categorys
            - manage products
            - manage order

## Installation

Install my-project with npm

```bash
  Python 3.11.6 
  Django==4.2.7
  djangorestframework==3.14.0
  pip install djangorestframework-simplejwt

```

## SellerHub API Reference

## Authentication

**Registration**

| Method       | Type  | Description (url)                             |
|:-------------|:------|:----------------------------------------------|
| `GET , POST` | `url` | `http://127.0.0.1:8000/user/api/registration` |

**Login**

| Method       | Type  | Description (url)                      |
|:-------------|:------|:---------------------------------------|
| `GET , POST` | `url` | `http://127.0.0.1:8000/user/api/login` |

**Refrsh token**

| Method  | Type  | Description (url)                          |
|:--------|:------|:-------------------------------------------|
| ` POST` | `url` | `http://127.0.0.1:8000/api/token/refresh/` |

#### (Seller_panel) Product item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
|:----------|:---------|:----------------------------------|
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

