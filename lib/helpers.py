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
        print("List of sellers:")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user.username}")
        print("____________________")
        print("")
    else:
        print("No users found.")
    return users

def find_users_by_username():
    username = input("Enter the seller's username: ")
    user = User.find_by_username(username)

    if user:
        print("____________________")
        print("") 
        print("Seller found:")
        print(f'1. Seller: {user.username} is still in the marketplace. Contact them through their email: {user.email}')
        print("____________________")
        print("") 
    else:
        print("Seller not found.")

def create_user(): 
    username = input("Enter the seller's username: ")
    email = input("Enter the seller's email: ")
    password = input("Enter the sellers password: ")
    try:
        user = User.create(username, email, password)
        print("____________________")
        print("")
        print(f'Success: Seller {user.username} has been added to the marketplace')
        print("____________________")
        print("")
    except Exception as exc:
        print("Error creating seller: ", exc)

def delete_user(): 
    username = input("Enter the user's username: ")
    password = input("Enter the password: ")
    try: 
        user = User.find_by_username(username)
        if user:
            user.delete(password)
            print("____________________")
            print("")
            print(f'Success: Seller {user.username} has been removed from the marketplace')
            print("____________________")
            print("")
        else:
            print("User not found.")
    except Exception as exc:
        print("Error deleting user: ", exc)



def list_listings(user): 
    #listings = Listing.get_all() 
    listings = user.listings
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

def create_listing(user): 
    title = input("Enter the listings title: ")
    price = input("Enter the listings's price: ")
    state = input("Enter the listings's state: ")

    #username = input("Enter the username: ")
    #state = input("Enter the listings state: ")

    #user = User.find_by_username(username)
    if user:
        try:
            listing = Listing.create(user, title, price, state, user.id)
            print("____________________")
            print("")
            print(f'Success: {listing.title} has been created')
            print("____________________")
            print("")
        except Exception as exc:
            print("Error creating listing: ", exc)

def delete_listing(user):
    title = input("Enter the listing's title: ")
    password = input("Enter the seller's admin password: ")

    # Check if the provided password matches the user's password
    if user.password == password:
        listing = Listing.find_by_title(title)
        if listing and listing.user_id == user.id:
            listing.delete(password)
            print("____________________")
            print("")
            print(f'Listing {title} deleted')
            print("____________________")
            print("")
        else:
            print("Listing not found or you do not have permission to delete it.")
    else:
        print("Incorrect password. Listing not deleted.")

def select_user(): 
    users = list_users()
    enter_number = input("Enter number from the users listed above: ")
    #check to make sure number exists 
    user = users[int(enter_number) - 1]
    return user 
            

def list_users_listings(user):
    #username = input("Enter the username: ")
    #user = User.find_by_username(username)
    
    if user:
        user_listings = user.listings()
        if user_listings:
            print("____________________")
            print("")
            print(f"Listings for user {user}:")
            for listing in user_listings:
                print(f'{listing.title} for ${listing.price}')
            print("____________________")
            print("")
        else:
            print(f"No listings found for user {user}")
    else:
        print(f"User with username {user} not found.")

