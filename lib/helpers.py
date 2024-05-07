# lib/helpers.py

from models.user import User
from models.listing import Listing

def exit_program():
    print("Goodbye!")
    exit()



def list_users(): 
    users = User.get_all() 
    if users:
        print("____________________")
        print("")
        print("List of users:")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user.username}")
        print("____________________")
        print("")
    else:
        print("No users found.")

def find_users_by_username():
    username = input("Enter the user's username: ")
    user = User.find_by_username(username)

    if user:
        print("____________________")
        print("") 
        print("User found:")
        print(f'1. User: {user.username}, Email: {user.email}')
        print("____________________")
        print("") 
    else:
        print("User not found.")

def create_user(): 
    username = input("Enter the user's username: ")
    email = input("Enter the users's email: ")
    password = input("Enter the password: ")
    try:
        user = User.create(username, email, password)
        print("____________________")
        print("")
        print(f'Success: {user.username} has been created')
        print("____________________")
        print("")
    except Exception as exc:
        print("Error creating user: ", exc)

def list_listings(): 
    listings = Listing.get_all() 
    if listings: 
        print("____________________")
        print("")
        print("List all listings:")
        for i, listing in enumerate(listings, start=1):
            print(f'{i}. {listing.title} for {listing.price}')
        print("____________________")
        print("")
    else: 
        print('Listing not found')

def find_listing_by_title(): 
    title = input("Enter the listing's title: ")
    listing = Listing.find_by_title(title)
    if listing:
        print("____________________")
        print("")
        print(f'{listing.title} for ${listing.price}')
        print("____________________")
        print("")
    else:
        print(f'Listing {title} not found')

def find_listing_by_state(): 
    state = input("Enter the listing's state: ")
    listing = Listing.find_by_state(state)
    if listing:
        print("____________________")
        print("")
        print(f'{listing.title} located in {listing.state} for ${listing.price}') 
        print("____________________")
        print("")
    else:
        print(f'Listings in {state} not found')

def create_listing(): 
    title = input("Enter the listings title: ")
    price = input("Enter the listings's price: ")
    username = input("Enter the username: ")
    state = input("Enter the listings state: ")

    user = User.find_by_username(username)
    if user:
        try:
            listing = Listing.create(title, price, state, user.id)
            print("____________________")
            print("")
            print(f'Success: {listing.title} has been created')
            print("____________________")
            print("")
        except Exception as exc:
            print("Error creating listing: ", exc)
    else:
        print(f"Error: User with username '{username}' not found.")


def delete_listing():
    title = input("Enter the listings title: ")
    password = input("Enter your password: ")
    if user := User.find_by_password(password):
        if listing := Listing.find_by_title(title):
            if listing.user_id == user.id:
                listing.delete(password)
                print("____________________")
                print("")
                print(f'Listing {title} deleted')
                print("____________________")
                print("")
            

def list_users_listings():
    username = input("Enter the username: ")
    user = User.find_by_username(username)
    

    if user:
        user_listings = user.listings()
        if user_listings:
            print("____________________")
            print("")
            print(f"Listings for user {username}:")
            for listing in user_listings:
                print(f'{listing.title} for ${listing.price}')
            print("____________________")
            print("")
        else:
            print(f"No listings found for user {username}")
    else:
        print(f"User with username {username} not found.")

