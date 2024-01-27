import sys
from add_user import user_add
from login import login_user
from changepw import change_password_rot13
from del_user import user_del

def main():
    #Get the Password form the command line arguments
    passwd = "passwd.txt"

    #display user commands
    print("\nUSER COMMANDS:")
    print("1.Add User")
    print("2.login")  
    print("3.Change Password")
    print("4.Delete user")
    print("5.Exit") 

    
    while True:
        choice =input("enter your choice (1-5): ")
        if choice == '1':
            # Call function to add user
            user_add(passwd)
       
        elif choice == '2':
            # Call Function to login
            login_user(passwd)
                
        elif choice == '3':
           # Call function to change password
           change_password_rot13(passwd)
                
        elif choice == '4':
            # Call functon to delete user
            user_del(passwd)

        elif choice =='5':
            #exit the program
            print("Exiting program. Goodbye!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a choice between 1 and 5.")
# Call the main function to start the program
main()

               


                  



    
