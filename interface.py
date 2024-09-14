#THIS CODE IS A BIGINNER PROJECT
#FOR RESEARCH PURPOSES
#A BANK ENTRY COMMAND LINE INTERFACE
#NOT FULLY FUNCTIONAL
print ("#"*144)
print ("#"*144)
print ("#"*144)
print ("#"*144)
print ("#####################[  WELCOME_TO_MAT.CO_BANK ]########################") #number of hash symbol are adjusted according to frame
print ("#"*144)
print ("#"*144)
print ("#"*144)
print ("#"*144 + "\n")

#GLOBALS
key = ("icu17*matco")
#_______________________________________________________________________
print ("[  ARE YOU A NEW USER?  ] (y/n)")
ans = input("\n")
# NEW USER ENTRY FUNCTION
if ans == "y":
    file = open ("INFORMATION EXTRACTION.txt", "w+")
    while True:
        print ("[  ENTER_FIRST_NAME ]")
        first_name = input ("\n")
        #file = open (first_name + ".txt", "w+")
        print ("[  ENTER_SECOND_NAME  ]")
        second_name = input ("\n")
        print("ENTER EMAIL") #input email
        email = input()
        while True:
            if "@email.com"  in email: #membership checking
                break
            if "@email.com" not in email:
                print("PLEASE ENTER A VALID EMAIL")
                
        print ("[  INSERT_A_PASSCODE. ]")
        password = input ("\n")
        if len(password) < 8:
            print ("[  PASSWORD_SHOULD_CONTAIN_ATLEAST_8_CHARACTERS  ]")
        if len(password) >= 8:
            print ("REENTER_PASSWORD_TO_CONFIRM")
            confirm = input ("\n")
            if confirm not in password:
                print ("PASSWORD_DOES_NOT_MATCH")
    #CONFIRM AND WRITE INPUT ON A TXT FILE
            if  confirm in password:
                print ("****CONFIRM? (y/n)****")
                print ("FIRST_NAME :" + first_name )
                print ("SECOND_NAME :" + second_name)
                confirmed = input ("\n")
                if confirmed == "y":
                    file.write("FIRSTNAME:\n" + first_name + "\n" )
                    file.write("SECONDNAME:\n" + second_name + "\n")
                    file.write("PASSCODE:\n" + password + "\n")
                    file.write("EMAIL:\n" + email + "\n")
                    print ("YOU_HAVE_SUCCESSFULLY_CREATED_A_MAT.CO_ACCOUNT\n")
                    print ("YOUR ENCRYPTION KEY is ' icu17*matco' ")
                    print ("YOU NEED TO HAVE ATLEAST $10 IN YOUR ACCOUNT FOR IT TO ACTIVATE AND MAT.CO HAS PROVIDED IT FOR YOU BUT IT IS TO BE PAID IN LESS THAN 7 DAYS/n ")
                    print ("#"* 72)
                file.close()
                break
                           
   
 #NEW BALANCE GLOBAL
new_balance = int(10)

#NEW USER ENTRY CONDITION
if ans == "n":
    while True:
        print ("#"*72)
        print ("#"*72)    
        print ("ENTER EMAIL")
        email = input("") 
        if '@email.com'   not in email:
            print ("invalid email")          
        if '@email.com' in email:
            break                                 
                             
#HOME
menu = { 1:"ACCOUNT INFO", 2:"BALANCE", 3:"TRANSACTIONS", 4:"CUSTOMER SERVICE"}
print ("HOME\n")   
first_ui = ["1.MENU", "2. EXIT", "3: SETTINGS"]
print (first_ui)
home = input ("")
#MENU
if home == "1":
    print ("#"*72)
    print ("#"*72)
    
    print ("\n")
    print (" MENU\n")
    print (menu)
    option = input ("")
    
#EXIT 
if home == "2":
    print ("Exit")
    exit()
        
#ACCOUNT_INFO
if option == "1":
    print ("#"*72)
    print ("#"*72)
    print (menu [1])
    account_options = print({ 1: "VERIFY YOUR ID",2:"DELETE ACCOUNT" })
    option_number = input ("\n")
    while True: #looping
            if option_number == "1":
                print ("DO YOU WANT TO VERIFY YOUR ACCOUNT? (y/n)")
                verify = input()
                if verify == "y":
                    print ("PLEASE ENTER A VALID EMAIL")
                    email = input()
                    if "@email.com" in email: #confirming email
                        print("CONFIRM? y/n"+ email)
                        email_confirmation = input()
                        if email_confirmation == "y":
                            print("YOU WILL RECEIVE AN EMAIL CONTAINING YOUR SUBSCRIPTION DETAILS")
                        if email_confirmation == "n":
                            exit()
                    if "@email.com" not in email:
                        print("PLEASE ENTER A VALID EMAIL")
                if verify == "n":
                    pass
                    exit()
                break #loop breaks here
            elif option_number == "2":# deleting account
                print ("DO YOU WANT TO DELETE ACCOUNT (y/n)")
                delete = input()
                if delete == "y":
                    print ("CONFIRM y/n :WARNING! : All Your Data Will be lost")
                    confirm = input()
                    if confirm == "y":
                        print("DELETING ACCOUNT...")
                        exit()
                    else:
                        pass
                if delete == "n":
                    pass 
                break
            else:
                print("INVALID OPTION")
         
    
    
            
# BALANCE
if  option == "2":
     print ("#"*72)
     print ("#"*72)
     print (menu [2])
     print (new_balance)#global variable
     
#TRANSACTIONS
if option == '3': 
    def transactions(): 
        #if option == "3":
        print ("#"*72)
        print ("#"*72)
        print (menu [3])
        transact_options = {1: "Send", 2:"Receive"}
        print (transact_options)
        transaction = input ("\n")
        if transaction == "1":
            print ("ENTER_AMOUNT")
            amount = int(input (""))
            if amount < new_balance:
                print("INSUFFIENT BALANCE")
                exit()
            while True:
                print ("ENTER_RECEIVER'S_ENCRYPTION_KEY")
                receiver = input ("")
                print ("ARE YOU SURE YOU WANT TO SEND " + "$" + str(amount) + " to " +   receiver + "? (y/n)")
                confirmation = input ("")
                if confirmation == "n":
                    print ("PLEASE RECONFIRM")
                if confirmation == "y":
                    print ("ENTER PASSCODE")
                    passcode = input ("")
                    if passcode == "0000":
                        print ("SENDING...")
                    break               
        if transaction == "2":
            while True:
                print ("ENTER YOUR ENCRYPTION KEY")
                encryption_key = input ("\n")
                global key
                if encryption_key == key: #needs access to a global variable
                    print ("ARE YOU SURE " + key + "IS YOUR ENCRYPTION_KEY? (y/n)")
                    confirm_key = input ("")
                    if confirm_key == "n":
                        print ("REENTER_KEY")
                    if confirm_key == "y":
                        print ("YOU WILL RECEIVE AN SMS MESSAGE")
                    break    
                else:
                    print ("WRONG_KEY")  
                          
    transactions()
    
 #CUSTOMER SERVICE   
if option == "4":
    print ("#"*72)
    print ("#"*72)
    print (menu [4] + "\n")
    print ("PHONE : +263 78 625 1790")
    print("contact us for support")
    print ("EMAIL : mlotshwaashley33@gmail.com") #how to put an email link in python
 