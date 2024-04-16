# lib/helpers.py

from models.user import User
from models.listing import Listing

def exit_program():
    print("Goodbye!")
    exit()

def list_users(): 
    users = User.get_all() 
    for user in users: 
        print(user)

def find_users_by_username():
    username = input("Enter the users's username: ")
    user = User.find_by_username(username)
    print(user) if user else print(
        f'User {username} not found') 

def find_users_by_id(): 
    id_ = input("Enter the users's id: ")
    user = User.find_by_id(id_)
    print(user) if user else print(f'User {id_} not found')

def create_user(): 
    username = input("Enter the user's username: ")
    email = input("Enter the users's email: ")
    try:
        user = User.create(username, email)
        print(f'Success: {user}')
    except Exception as exc:
        print("Error creating user: ", exc)

def delete_user(): 
    id_ = input("Enter the user's id: ")
    if user := User.find_by_id(id_):
        user.delete()
        print(f'User {id_} deleted')
    else:
        print(f'User {id_} not found')

def list_listings(): 
    listings = Listing.get_all() 
    for listing in listings: 
        print(listing)

def find_listing_by_title(): 
    title = input("Enter the listing's title: ")
    listing = Listing.find_by_title(title)
    print(listing) if listing else print(
        f'Listing {title} not found') 

def find_listing_by_id(): 
    id_ = input("Enter the listing's id: ")
    listing = Listing.find_by_id(id_)
    print(listing) if listing else print(f'Listing {id_} not found')

def create_listing(): 
    title = input("Enter the listings title: ")
    price = input("Enter the listings's price: ")
    username = input("Enter the username: ")
    #print(f"Entered username: '{username}'") 

    user = User.find_by_username(username)
    #print(f"Retrieved user: {user}") 
    if user:
        try:
            listing = Listing.create(title, price, user.id)
            print(f'Success: {listing}')
        except Exception as exc:
            print("Error creating listing: ", exc)
    else:
        print(f"Error: User with username '{username}' not found.")


def delete_listing(): 
    id_ = input("Enter the listing's id: ")
    if listing := Listing.find_by_id(id_):
        listing.delete()
        print(f'Listing {id_} deleted')
    else:
        print(f'Listing {id_} not found')

def list_users_listings():
    # Prompt the user for the username
    username = input("Enter the username: ")

    # Find the user object based on the username
    user = User.find_by_username(username)

    if user:
        # If the user is found, retrieve their listings
        user_listings = user.listings()

        # Print the user's listings
        if user_listings:
            print(f"Listings for user {username}:")
            for listing in user_listings:
                print(listing)
        else:
            print(f"No listings found for user {username}")
    else:
        print(f"User with username {username} not found.")

