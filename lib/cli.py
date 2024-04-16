from helpers import (
    exit_program,
    list_users, 
    find_users_by_username, 
    find_users_by_id, 
    create_user,  
    delete_user,
    list_listings, 
    find_listing_by_title, 
    find_listing_by_id,
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
        elif choice == "1":
            list_users()
        elif choice == "2":
            find_users_by_username()
        elif choice == "3":
            find_users_by_id()
        elif choice == "4":
            create_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            list_listings()
        elif choice == "7":
            find_listing_by_title()
        elif choice == "8":
            find_listing_by_id()
        elif choice == "9":
            create_listing()
        elif choice == "10":
            delete_listing()
        elif choice == "11":
            list_users_listings()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all users")
    print("2. Find users by username")
    print("3. Find users by id")
    print("4. Create a user")
    print("5. Delete user")
    print("6. List listings")
    print("7. Find listing by title")
    print("8. Find listing by id")
    print("9. Create a listing")
    print("10. Delete a listing")  
    print("11. List all users listings")


if __name__ == "__main__":
    main()
