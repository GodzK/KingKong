class bl:
    def __init__(self):
        self.userdata = {}
    def addnewuser(self, idregis, userregis):
        self.userdata[idregis] = {"name" : userregis , "money" : 0 }
        print(self.userdata)
    def checkuser(self, idlogin,userlogin):
        if idlogin in self.userdata:
            return True
        else:
            return False
    def savemoney(self,idlogin,money):
        self.userdata[idlogin]["money"] += money
    def returnmoney(self,idlogin):
        return self.userdata[idlogin]["money"]
    def checkidregis(self,idregis):
        if 0 < int(idregis) < 100:
            return True
        else:
            return ValueError
    def checkuserregis(self,userregis):
        if userregis == str:
            return True
        else:
            return ValueError
        
    
        
class ui:
    def __init__(self,bl_instance):
        self.bl = bl_instance

    def mainpage(self):
        while True:
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
        while True:
            try:
                idregis = input("type your id : ")
                self.bl.checkidregis(idregis)
                userregis = input("type your name : ") 
                self.bl.checkuserregis(userregis)
                self.bl.addnewuser(idregis , userregis)
                self.mainpage()
            except TypeError:
                raise("your data is wrong")
                
        

    def login(self):
        print("Login page")
        idlogin = input("Type your Id : ")
        userlogin = input("Type Your Name : ")
        try:
            if self.bl.checkuser(idlogin,userlogin):
                self.menu(idlogin,userlogin)
            else:
                print("You have not an account")
                self.menu(idlogin,userlogin)
        except TypeError:
                raise ("Your Type data is Error!!!")
        except ValueError:
                raise ("You Pass The wrong Data!!!")
                  

    def menu(self,idlogin,userlogin):
        while True: 
            print(f"Welcome {userlogin}")
            print("[1] to safe money")
            print("[2] to see your money")
            print("[3] to exit")
            userchoice = input("Type Your Choice : ")
            match int(userchoice):
                case 1:
                    try:
                        money = int(input("Type Your money : "))
                        self.bl.savemoney(idlogin,money)
                        print("Save!!")
                        self.menu(idlogin,userlogin)
                    except TypeError:
                        return ("Your type is Error")
                case 2 :
                    print(f"You Have {self.bl.returnmoney(idlogin)} Bath")
                    self.menu(idlogin,userlogin)
                case 3:
                    print("See You later")
                    break
                
                
    
def main():
    bl_instance = bl()
    ui_instance = ui(bl_instance)
    ui_instance.mainpage()


main()