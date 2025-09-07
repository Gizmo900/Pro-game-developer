
"""   
Dictionary Homework 13 September

Step 1: Create a Dictionary

Create a dictionary named product with the following data:

Key	Value
name	"Wireless Mouse"
price	1200
stock	50
category	"Electronics"

Step 2: Access Values

Print the name of the product.
Print the stock available.

Step 3: Add a New Key-Value Pair

Add a new key "brand" with the value "Logitech".

Step 4: Update a Value

Update the "price" of the product to 999.

Step 5: Check if a Key Exists

Check if the key "discount" exists in the dictionary.
If not, add "discount" with the value 10 (representing 10% discount).

Step 6: Delete a Key

Remove the "category" key completely from the dictionary.

"""


Itemandvalue={ "name":"Wireless mouse",
              "price":1200,
              "stock":50,
              "category":"Electronics"}


print("Itemandvalue:",Itemandvalue)

""" 
Step 2: Access Values

"""
print("name of the product:",Itemandvalue["name"])


"""   
Step 3: Add a New Key-Value Pair

"""
Itemandvalue["brand"]="Logitech"
print("Itemandvalue:",Itemandvalue)

"""
Step 4: Update a Value

Update the "price" of the product to 999.

"""
Itemandvalue["price"]=999
print("Itemandvalue:",Itemandvalue)


"""
Step 5: Check if a Key Exists

Check if the key "discount" exists in the dictionary.
If not, add "discount" with the value 10 (representing 10% discount).

"""
if "discount" in Itemandvalue:
    print("discount:",Itemandvalue["discount"])
else:
    print("discount not available")


"""
Step 6: Delete a Key

Remove the "category" key completely from the dictionary.

"""
del Itemandvalue["category"]
print("Itemandvalue:",Itemandvalue)

