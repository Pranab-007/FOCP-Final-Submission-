def change_password_rot13(passwd):
    import codecs
    import getpass                      

    def read_password_file():
        with open (passwd,"r") as file:                # open the password file in read mode
            lines= file.readlines()                    #Read all lines from the file into a list
        return[line.strip() for line in lines]         

    def write_password_file(entries):
        with open (passwd , "w") as file:
            # join the entries with new line characters and write them to the file
            file.write("\n". join(entries))

    def change_password_rot13(username,current_password, new_password):
        #read the existing entries from the password file
        entries= read_password_file()

        found = False   #flag to indicate whether a matching user and password were found

        for i, entry in enumerate(entries): # Iterate over the entries to find and update the users password
            parts = entry.split(":")
            if parts[0] == username and codecs.encode(parts[2],"rot_13")==codecs.encode(current_password , "rot_13"):
                # Upadte the entry with the new password
                entries[i] = f"{username}:{parts[1]}:{new_password}"
                found = True
                break 
        if found: 
            write_password_file(entries) #write the updated entries back to password file
            print("Password changed Successfully. ")
        else:
            print("Error: Username Not Found or Invalid Current Password.")
    #check if the scriptis is not being run as the main program
    if __name__ != "__main__":
        username = input  ("Enter Username: ")
        current_password = getpass.getpass("Enter current password : ") 
        current_password = codecs.encode(current_password, "rot13") #encode the current password using rot13
        new_password =  getpass.getpass("Enter new password: ")
        new_password = codecs.encode(new_password, "rot13")  #encode the new password using rot13

    change_password_rot13(username,current_password, new_password) #call the function to change the password