Ejam Test Product API
---------------

Step for Installation
----------------------

1. You need to put module in addons directory or custom addons.
2. You need to Update App List from app menu.
3. Search module name in search bar.
4. Click on install button.

Step for Testing.
-------------------------------

1. First you need to install Postman in your system. You can install postman 
   in Ubuntu using below command.

   $sudo snap install postman.

2. Open the postman and send request on below endpoint.

   http://localhost:8069/ejam_test_product_api/product/2

   Here last parameter is product id. Api will return data for 
   id which pass in above request.

3. Example of output.

   {
    "name": "Hotel Accommodation",
    "sale_price": 400.0,
    "cost_price": 400.0,
    "onhand_quantity": 0.0,
    "category": "Expenses"
    }

