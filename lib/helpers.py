# lib/helpers.py

from models.user import User
from models.listing import Listing

def exit_program():
    print("Goodbye!")
    exit()

def list_users(): 
    user = User.get_all() 
    for User in user: 
        print(user)

def find_users_by_name():
    pass 

def find_users_by_id(): 
    pass

def create_user(): 
    pass

def update_user(): 
    pass

def delete_user(): 
    pass

def list_listings(): 
    pass

def find_listing_by_name(): 
    pass

def find_listing_by_id(): 
    pass

def create_listing(): 
    pass

def update_listing(): 
    pass

def delete_listing(): 
    pass

def list_users_listings(): 
    pass

