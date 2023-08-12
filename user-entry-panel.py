print("LEXUS Corp.\nDatabase Login Panel")

admin_username = "root"
admin_pw = "lcorp!*"
change_of_login = 3



while True:
            un = input("Please Type Username:")
            pw = input("Please Type Password:")

            if un==admin_username and pw!=admin_pw:
                print("Incorrect Password.")
                change_of_login-=1

            elif un!=admin_username and pw==admin_pw:
                print("Incorrect Username.")
                change_of_login-=1

            elif un!=admin_username and pw!=admin_pw:
                print("Incorrect Password and Username.")
                change_of_login-=1

            else:
                print ("Logining to Database...\nWelcome root !")
                break


            if change_of_login == 0:
                print("Your change of try is over !\nLogging out...")
                break

