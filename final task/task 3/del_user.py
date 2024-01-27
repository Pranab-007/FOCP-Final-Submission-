def user_del(passwd):
    import codecs
    import getpass                             #importing modules

    def read_password_file(passwd):
        with open (passwd,"r") as file:        # open the password file in read mode
            lines= file.readlines()            #Read all lines from the file into a list
        return[line.strip() for line in lines]  #return a list containing each line from the file, stripped of leading and tarailing whitespaces

    def write_password_file(entries):
        with open (passwd , "w") as file:         # open the file in write mode
            file.write("\n". join(entries))       # join the entries with new line characters and write them to the file

    def delete_user(username):
        entries=read_password_file(passwd)      #read exisiting entries from the password file
        new_entries = []                        # Create a new list to store entries excluding the one with the specified username
        for entry in entries:                   # Iterate through each entry in the password file
            parts = entry.split(":")
            if parts[0] != username:            #check if the current entry's username is not equal to the specified username
                new_entries.append(entry)       # add the entry to the new_entries list
        write_password_file(new_entries)        # write the modified entries (excluding the specified username) back to the password file

    def deluser(passwd):                       
        username = input("enter username to delete:")
        entries =  read_password_file(passwd)         #read exisitng entries from the password flie

        if any(entry.split(":")[0]==username for entry in entries):     #check if the specified username exists in the entries
            delete_user(username)                      # call the delete_user function to remove the specified user
            print("User Deleted Sucessfully!!!!!!")
        else:
            print("No Such User found.....")   

    deluser(passwd)  
