users = []

def create_user():
    user_id = input("Enter user ID: ")
    name = input("Enter user name:")
    age = input("Enter user age:")
    user = {"id":user_id,"name":name,"age":age}
    users.append(user)
    print(f"User {name} added. \n")


def read_users():
    if users:
        print("\nList of Users:")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Age: {user['age']}")
    else:
        print("No users found.\n")


def update_user():
    user_id = input("Enter user ID to update: ")
    for user in users:
        if user["id"] == user_id:
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            user["name"] = new_name
            user["age"] = new_age
            print(f"User {user_id} updated.\n")
            return
    print(f"User {user_id} not found.\n")


def delete_user():
    user_id = input("Enter user ID to delete: ")
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print(f"User {user_id} deleted.\n")
            return
    print(f"User {user_id} not found.\n")



def menu():
    while True:
        print("select an option:")
        print("1. Create user")
        print("2. Read users")
        print("3. Update user")
        print("4. Delete user")
        print("5. Exit")
        choice =  input("Enter your choice (1-5): ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__=="__main__":
    menu()
