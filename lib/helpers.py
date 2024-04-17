# lib/helpers.py

from models.user import User
from models.listing import Listing

def exit_program():
    print("Goodbye!")
    exit()

def list_users(): 
    users = User.get_all() 
    for user in users: 
        print(f'User: {user.username}, Email: {user.email}')

def find_users_by_username():
    username = input("Enter the users's username: ")
    user = User.find_by_username(username)
    print(f'User: {user.username}, Email: {user.email}') if user else print(
        f'User {username} not found') 

def find_users_by_id(): 
    id_ = input("Enter the users's id: ")
    user = User.find_by_id(id_)
    print(f'User: {user.username}, Email: {user.email}') if user else print(f'User {id_} not found')

def create_user(): 
    username = input("Enter the user's username: ")
    email = input("Enter the users's email: ")
    password = input("Enter the password: ")
    try:
        user = User.create(username, email, password)
        print(f'Success: {user}')
    except Exception as exc:
        print("Error creating user: ", exc)

def delete_user(): 
    password = input("Enter the user's password: ")
    if user := User.find_by_password(password):
        user.delete()
        print(f'User {user.username} deleted')
    else:
        print(f'User {user} not found')

def list_listings(): 
    listings = Listing.get_all() 
    for listing in listings: 
        print(f'{listing.title} for ${listing.price}')

def find_listing_by_title(): 
    title = input("Enter the listing's title: ")
    listing = Listing.find_by_title(title)
    if listing:
        print(f'{listing.title} for ${listing.price}')
    else:
        print(f'Listing {title} not found')

def find_listing_by_state(): 
    state = input("Enter the listing's state: ")
    listing = Listing.find_by_state(state)
    print(f'{listing.title} located in {listing.state} for ${listing.price}') if listing else print(f'Listings in {state} not found')

def create_listing(): 
    title = input("Enter the listings title: ")
    price = input("Enter the listings's price: ")
    username = input("Enter the username: ")
    state = input("Enter the listings state: ")

    user = User.find_by_username(username)
    if user:
        try:
            listing = Listing.create(title, price, state, user.id)
            print(f'Success: {listing}')
        except Exception as exc:
            print("Error creating listing: ", exc)
    else:
        print(f"Error: User with username '{username}' not found.")


def delete_listing():
    id_ = input("Enter the listing's id: ")
    password = input("Enter your password: ")
    if listing := Listing.find_by_id(id_):
        listing.delete(password)
        print(f'Listing {id_} deleted')
    else:
        print(f'Listing {id_} not found')

def list_users_listings():
    username = input("Enter the username: ")
    user = User.find_by_username(username)

    if user:
        user_listings = user.listings()
        if user_listings:
            print(f"Listings for user {username}:")
            for listing in user_listings:
                print(f'{listing.title} for ${listing.price}')
        else:
            print(f"No listings found for user {username}")
    else:
        print(f"User with username {username} not found.")

