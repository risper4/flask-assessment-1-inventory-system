# Inventory System

### By : Risper Gichia

## Introduction

* An inventory system that :
    - Enlists all products
    - Displays a certain product
    - Creates a new product
    - Updates a specific product
    - Deletes a specific product
    - Finds a products details using a barcode

* The system includes :
    - Backend flask system : backend
    - CLI Tool : frontend

* The command line tool is accessed by running `python3 main.py` on `main.py`


## Instructions

* These are the step-by-step instructions on how to use the Inventory CLI System :

    1. Veiwing inventory
- Run on terminal : `python3 main.py inventory`
    2. Displaying a specific product
- Run on terminal : `python3 main.py display-product --id '*id*'` 
    3. Creating a new product 
- Run on terminal : `python3 main.py add-product --name '*name*' --price'*price*'`
    4. Updating a specific product's price
- Run on terminal : `python3 main.py update-product --id '*id*' --price '*price*'`
    5. Delete a specific product
- Run on terminal : `python3 main.py delete-product --id '*id*'`
    6. Find product details on the api
- Run on terminal : `python3 main.py update-product --barcode '*barcode*'`


* For any assistance :
    - Run on terminal : `python3 main.py --help`


## Tools used
  - Flask (Backend)
  - Python (Frontend)
  - Pytest (Testing)


### Access
* Access the system through :
    * Github : `https://github.com/risper4/flask-assessment-1-inventory-system.git`

#### Contact
    * Github : `risper4`