class BL:
    def __init__(self):
        self.user_data = {
        }
        self.currentid = ''
        self.course_data = {
            "Discrete": [671305, 516712],
            "Ux-Ui": [671304, 671300],
            "DesignThinking": [671345, 671378]
        }

    
    def current_user(self,user_id):
        self.currentid = user_id

    def get_currentid(self):
        return self.currentid
    def logout(self):
        self.currentid = ''
        



    def enroll(self,course,userid):
        
        self.course_data[course].append(userid)
        print(self.course_data)
        
    def get_user_data(self):
        return self.user_data
        

    def get_course_data(self):
        return self.course_data

    def check_duplicate(self, user_id):
        return user_id not in self.user_data

    def register_user(self, user_id, user_name):
        if self.check_duplicate(user_id):
            self.user_data[user_id] = user_name
            return True
        return False

    def all_course(self):
        return self.course_data

    def filter_mycourse(self, user_id):
        my_courses = []
        for course, user_ids in self.course_data.items():
            if user_id in user_ids:
                my_courses.append(course)
        return my_courses

    def my_course(self, user_id):
        return self.filter_mycourse(user_id)


class UI:
    def __init__(self, bl_instance):
        self.bl = bl_instance
    def login_menu(self):
        while True:
            print("\nStudent Information System")
            print("  [1] Login")
            print("  [2] Register")
            print("  [3] Exit")
            choice = input("Choose one [1|2|3]: ")
            try:
                match int(choice):
                    case 1:
                        self.login()
                    case 2:
                        self.register_user()
                    case 3:
                        print("Exiting...")
                        break
                    case _:
                        print("Invalid choice!")
            except ValueError:
                print("Invalid input, please enter a number.")

    def login(self):
        user_data = self.bl.get_user_data()
        if not user_data:
            print("No users registered yet!")
            return
        try:
            user_id = int(input("Enter your user ID: "))
            
            if user_id in user_data:
                self.bl.current_user(user_id)
                print(f"Welcome back, {user_data[user_id]}!")
                self.mainmenu(user_id)
            else:
                print("User ID not found. Please register first.")
        except ValueError:
            print("Invalid input, please enter a valid user ID.")

    def mainmenu(self, user_id):
        currid = self.bl.get_currentid()
        while True:
            print("\nStudent Information System")
            print(f"Current User :{currid} ")
            print("  [1] All Courses")
            print("  [2] My Courses")
            print("  [3] Logout")
            choice = input("Choose one [1|2|3|4]: ")
            try:
                match int(choice):
                    case 1:
                        self.all_course()
                    case 2:
                        self.my_course(user_id)
                    case 3:
                        self.bl.logout()
                        self.login_menu()
                        return
                    case _:
                        print("Invalid choice!")
            except ValueError:
                print("Invalid input, please enter a number.")

    def all_course(self):
        currid = self.bl.get_currentid()
        courses = self.bl.all_course()
        
        # userid = self.bl.get_user_data()
        currid = self.bl.get_currentid()
        #courseตอนนี้
        print("\nAvailable Courses:")
        for course, course_ids in courses.items():
            print(f"{course}: {course_ids}")
        print(f"Current User :{currid} ")
        print("You Want to Enroll to Enroll Some Course")
        print("  [1] Discrete")
        print("  [2] Ux Ui")
        print("  [3] Design Thinking")
        print("  [4] Exit")
        choice = input("Choose one [1|2|3|4]: ")
        try:
                match int(choice):
                    case 1:
                        print("You Choose Discrete!")
                        self.bl.enroll("Discrete" , currid )
                    case 2:
                        print("You Choose Ux-Ui")
                    case 3:
                        print("You Choose Design-thinking")
                        self.login_menu()
                        return
                    case 4:
                        self.mainmenu()
                        
                    case _:
                        print("Invalid choice!")
        except ValueError:
                print("Invalid input, please enter a number.")




    def my_course(self, user_id):
        currid = self.bl.get_currentid()
        print(f"Current User :{currid} ")
        my_courses = self.bl.my_course(user_id)
        if my_courses:
            print("\nYour Courses:")
            for course in my_courses:
                print(course)
        else:
            print("You are not enrolled in any courses.")

    def register_user(self):
        try:
            user_id = int(input("Enter a new user ID: "))
            user_name = input("Enter your name: ")
            if self.bl.register_user(user_id, user_name):
                print("Registration successful!")
            else:
                print("User ID already exists. Please try a different one.")
        except ValueError:
            print("Invalid input, please enter a valid user ID.")


def main():
    bl_instance = BL()
    ui_instance = UI(bl_instance)
    ui_instance.login_menu()


if __name__ == "__main__":
    main()
