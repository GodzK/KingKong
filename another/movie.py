class bl:
    def __init__(self):
        #Private Attribute
        self.user_data = {"moviewatch" : []}
        self.movie_data = {"movie" : ["pirate of the carebian" , "iron man 3 " , "avengers"]}
    def adduser(self,userregis,regispass):
        self.user_data[userregis] =  regispass
        print(self.user_data)
    
    def checkuser(self,userlogin , userpass):
        if userlogin in self.user_data :
            if self.user_data[userlogin] == userpass:
                return True
        else:
            raise ValueError
    def showmovie(self):
        print(self.movie_data) 

    def addmovietouser(self, moviepick):
        movie = self.movie_data["movie"][moviepick]
        self.user_data["moviewatch"].append(movie) 
        print(f"Movies watched: {self.user_data['moviewatch']}")

class ui:
    def __init__(self,bl) -> None:
        self.bl =  bl
    def mainpage(self):
        print("Welcome to major cineplex")
        print("please login or register")
        print("type [1] to register")
        print("type [2] to login")
        choice = int(input("Type Your Choice : "))
        match choice:
            case 1:
                self.register()
            case 2:
                self.login()
            case _:
                raise ValueError
    
    def register(self):
        userregis = input("Type Your name : ")
        regispass = input("type Your Password")
        self.bl.adduser(userregis,regispass)
        self.mainpage()

    def login(self):
        try:
            userlogin = input("Type Your username")
            userpass = input("Type Your password")
            self.bl.checkuser(userlogin,userpass)
            self.menu(userlogin)
            
        except ValueError:
            raise ("Your data isnt in our database")
    
    def menu(self,userlogin):
        print(f"Welcome to our app {userlogin}")
        print("WHAT MOVIE THAT YOU WANT TO SEE") 
        self.bl.showmovie()
        while True: 
            print("[1] Pirate of the carebian")
            print("[2] ironman 3")
            print("[3] avengers")
            print("[4] Stop Picking ")
            
            try:
                moviepick = int(input("Type Your Choice"))
                if moviepick == 4:  
                    self.watch(userlogin)   
                    break
                match moviepick:
                    case 1:
                        self.bl.addmovietouser(1-1)
                    case 2:
                        self.bl.addmovietouser(2-1)
                    case 3:
                        self.bl.addmovietouser(3-1)
            except ValueError:
                raise ("value Error!!")
            
    def watch(self,userlogin):
        print(f"สวัสดี{userlogin} มาเริ่มดู กัน")
        print(self.bl.user_data["moviewatch"])

def main():
    blinstance = bl()
    uiinstance = ui(blinstance)
    uiinstance.mainpage()


if  __name__ == "__main__":
    main()  
        