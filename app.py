
def main():
    userData = bl.userData()
    courseData = bl.courseData()
    menu = ui()
    menu.mainmenu(userData,courseData)

class ui:
    def mainmenu(self,userData,courseData):
        while True:
            print("\nStudent Information System")
            print("  [1] Login")
            print("  [2] Register")
            print("  [3] Exit")
            result = input("  Choose one [1|2|3] or anything else to exit: ")
            try:
                match int(result):
                    case 1: self.login(userData,courseData)
                    case 2: self.regis(userData,courseData)
                    case 3: break
            except:
                print("Wrong input")
                break
            
    def login():
        pass
    def regis(self,userData,courseData):
        while True:
            try:
                userid = bl.check_duplicate(userData)
            except ValueError:
                print("ficl")
                raise "Ai Na here"
                

            
    
    def menu():
        pass 
        #enroll
        #course
        #logout

    





class bl:
    @classmethod
    def userData(cls):
        return {}
    @classmethod
    def courseData(cls):
        return {
            "Discrete": [671305,516712],
            "Ux-Ui" : [671304,671300],
            "DesignThinking": [671345,671378]
        }
    @classmethod
    def check_username(cls ,userid):
        if 1 <= userid <= 100 :
            if userid in userData:
                return True
        else:
            return False
        
    @classmethod
    def check_duplicate(cls , userid ,userData):
        if userid in userData:
            return False
        else:
            return userid
        
        

    

    

            




if __name__ == "__main__":
    main()