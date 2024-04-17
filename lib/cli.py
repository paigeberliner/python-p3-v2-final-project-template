from helpers import (
    exit_program,
    list_users, 
    find_users_by_username, 
    find_users_by_id, 
    create_user,  
    list_listings, 
    find_listing_by_title, 
    find_listing_by_state,
    create_listing,
    delete_listing,
    list_users_listings
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1a":
            list_users()
        elif choice == "2a":
            find_users_by_username()
        elif choice == "3a":
            find_users_by_id()
        elif choice == "4a":
            create_user()
        elif choice == "1b":
            list_listings()
        elif choice == "2b":
            find_listing_by_title()
        elif choice == "3b":
            find_listing_by_state()
        elif choice == "4b":
            create_listing()
        elif choice == "5b":
            delete_listing()
        elif choice == "6b":
            list_users_listings()
        else:
            print("Invalid choice")


def menu():
    print("Welcome to the marketplace! Please select an option:")
    print("Are you interested in finding a specific seller?")
    print("1a. List all users selling items")
    print("2a. Find users selling items by username")
    print("3a. Find users by id")
    print("4a. Create a user")
    print("Are you interested in finding a specific listing?")
    print("1b. List listings")
    print("2b. Find listing by title")
    print("3b. Find listing by state")
    print("4b. Create a listing")
    print("5b. Delete your listing")  
    print("6b. List all users listings")
    print("PRESS 0 to exit marketplace")


if __name__ == "__main__":
    main()
