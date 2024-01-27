def login_user(passwd):  
    import codecs            #importing modules
    import getpass

    def read_file(passwd):
        with open(passwd,"r") as file:          # open the password file in read mode
            lines= file.readlines()             #Read all lines from the file into a list
        return [line.strip() for line in lines] #return a list containing each line from the file, stripped of leading and tarailing whitespaces

    def login():                                # Function to handle the login process
        username= input("\nEnter username: ") 
        password = getpass.getpass("Enter password: ")   
        password = codecs.encode(password, "rot_13")  #encoded password using rot13

        entries = read_file(passwd)    #read the entries from the password file

        for entry in entries:           # Check if the entered username and password match any entries
            parts = entry.split(":")
            if parts[0] == username and parts[2] == password:
                print("\n Login Successful!!")
                return
        print("Invalid Username or Password")    # print error 
    if __name__ != "__main__":            # check if the script is not being run as the main program
        login()


            

        



