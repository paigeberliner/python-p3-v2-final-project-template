from helpers import (
    exit_program,
    list_users, 
    find_users_by_name, 
    find_users_by_id, 
    create_user, 
    update_user, 
    delete_user,
    list_listings, 
    find_listing_by_name, 
    find_listing_by_id,
    create_listing,
    update_listing,
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
            find_users_by_name()
        elif choice == "3":
            find_users_by_id()
        elif choice == "4":
            create_user()
        elif choice == "5":
            update_user()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            list_listings()
        elif choice == "8":
            find_listing_by_name()
        elif choice == "9":
            find_listing_by_id()
        elif choice == "10":
            create_listing()
        elif choice == "11":
            update_listing()
        elif choice == "12":
            delete_listing()
        elif choice == "13":
            list_users_listings()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all users")
    print("2. Find users by name")
    print("3. Find users by id")
    print("4. Create a user")
    print("5. Update a user")
    print("6. Delete user")
    print("7. List listings")
    print("8. Find listings by name")
    print("9. Find listings by id")
    print("10. Create a listing")
    print("11. Update a listing")
    print("12. Delete a listing")  
    print("13. List all users listings")


if __name__ == "__main__":
    main()
