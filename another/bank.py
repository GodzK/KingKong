class bl:
    def __init__(self):
        self.userdata = {}
    def addnewuser(self, idregis, userregis):
        self.userdata[idregis] = userregis
        print(self.userdata)
    def checkuser(self, idlogin,userlogin):
        if idlogin in self.userdata:
            return True
        else:
            return False

class ui:
    def __init__(self,bl_instance):
        self.bl = bl_instance

    def mainpage(self):
        print("welcome to Bank")
        print("Type [1]  to go register")
        print("Type [2] to go to login")
        userinp = input("Type Your Choice ! : ")
        try:
            match int(userinp):
                case 1:
                    self.register()
                case 2:
                    self.login()
        except ValueError:
            print("invalid input")

    def register(self):
        idregis = input("type your id : ")
        userregis = input("type your name : ") 
        self.bl.addnewuser(idregis , userregis)
        self.mainpage()

    def login(self):
        print("Login page")
        idlogin = input("Type your Id : ")
        userlogin = input("Type Your Name : ")
        try:
            if self.bl.checkuser(idlogin,userlogin):
                self.menu()
            else:
                print("You have not an account")
                self.mainpage()
        except TypeError:
                raise ("Your Type data is Error!!!")
        except ValueError:
                raise ("You Pass The wrong Data!!!")
                
            
        
            

    def menu(self):
        print("This is Menu Page")

            


            
        
        

        
            




    
def main():
    bl_instance = bl()
    ui_instance = ui(bl_instance)
    ui_instance.mainpage()


main()


        
        