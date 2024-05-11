from helpers import (
    exit_program,
    list_users, 
    find_users_by_username, 
    create_user,
    delete_user,  
    list_listings, 
    #find_listing_by_title, 
    #find_listing_by_state,
    create_listing,
    delete_listing,
    select_user,
    list_users_listings
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            find_users_by_username()
        elif choice == "3":
            create_user()
        elif choice == "4":
            delete_user()
        elif choice == "5": 
            user = select_user()
            listings_loop(user)
            


            
        # elif choice == "1b":
        #     list_listings()
        # elif choice == "2b":
        #     find_listing_by_title()
        # elif choice == "3b":
        #     find_listing_by_state()
        # elif choice == "4b":
        #     create_listing()
        # elif choice == "5b":
        #     delete_listing()
        # elif choice == "6b":
        #     list_users_listings()
        # else:
        #     print("Invalid choice")

def listings_loop(user):
    while True:
        listings_menu(user)
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users_listings(user)
        elif choice == "2": 
            create_listing(user)
        elif choice == "3":
            delete_listing(user)
        elif choice == "4":
            main()

def menu():
    print("Please select an option to get more information on the marketplace:")
    print("1. List all sellers in the marketplace")
    print("2. Check to see if a specific seller is still in the marketplace")
    print("3. Add a new seller to the marketplace")
    print("4. Remove a seller from the marketplace")
    print("5. Select a seller and make updates to their listings")


def listings_menu(user):
    print(f"1. See seller {user.username}'s listings" )
    print(f"2. Create a listing for seller {user.username}")
    print(f"3. Delete a listing for seller {user.username}")
    print(f'4. Go to main menu')
    #print("1b. List listings")
    #print("2b. Find listing by title")
    #print("3b. Find listing by state")
    #print("4b. Create a listing")
    #print("5b. Delete your listing")  
    #print("6b. List all users listings")
    print("PRESS 0 to exit marketplace")


if __name__ == "__main__":
    main()
