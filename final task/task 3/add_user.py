def user_add(passwd):
    import codecs
    import getpass                #importing modules

    def read_password_file(passwd):      # open the password file in read mode
        with open (passwd,"rt") as file:
            lines= file.readlines()       #Read all lines from the file into a list
        return[line.strip() for line in lines]   #return a list containing each line from the file, stripped of leading and tarailing whitespaces

    def write_password_file(passwd, entries):     
        with open (passwd , "w") as file:       # open the file in write mode
            file.write("\n". join(entries))      # join the entries with new line characters and write them to the file

    def encode_password(password):             # Function to encode a password using rot13
        return codecs.encode(password, "rot13")

    def add_user(passwd):                         # Function to add a new user to the password file
        entries = read_password_file(passwd)       # read the existing entries from the password file

        user_name = input("\nEnter username : ")    #get input from user
        full_name = input("Enter Fullname : ")

        #Password input
        password = getpass.getpass("Enter Password : ")
        users = [entry.strip().split(",") [0]for entry in entries]    #extract existing username from entires


        if user_name not in users:     #check if the entered username already exists
            encoded_password = encode_password(password)
            entries.append(f"{user_name}:{full_name}:{encoded_password}\n") #append the new user entry to the entries list
            write_password_file(passwd,entries)     #write the modified entries back to password file
            print("User Created!!!!\n")
        else:
            print("Username already exists , please enter a new username!!")
            add_user(passwd)

    add_user("passwd.txt")



        