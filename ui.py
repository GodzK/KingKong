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
        while True:
            print("\nStudent Information System")
            print(f"Current User: {self.bl.get_currentid()}")
            print("  [1] All Courses")
            print("  [2] My Courses")
            print("  [3] Logout")
            choice = input("Choose one [1|2|3]: ")
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
        courses = self.bl.all_course()
        print("\nAvailable Courses:")
        for course, course_ids in courses.items():
            print(f"{course}: {course_ids}")
        print("You want to enroll in some course?")
        print(f"  [1] Discrete [Enrolled ({len(courses["Discrete"])}/ 5) ]")
        print(f"  [2] Ux-Ui [Enrolled ({len(courses["Ux-Ui"])} from 5) ]")
        print(f"  [3] Design Thinking [Enrolled ({len(courses["DesignThinking"])} from 5) ]")
        print(f"  [4] Exit")
        choice = input("Choose one [1|2|3|4]: ")
        try:
            match int(choice):
                case 1:
                    print("You chose Discrete!")
                    self.bl.enroll("Discrete", self.bl.get_currentid())
                case 2:
                    print("You chose Ux-Ui!")
                    self.bl.enroll("Ux-Ui", self.bl.get_currentid())
                case 3:
                    print("You chose Design Thinking!")
                    self.bl.enroll("DesignThinking", self.bl.get_currentid())
                case 4:
                    return
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Invalid input, please enter a number.")

    def my_course(self, user_id):
        my_courses = self.bl.my_course(user_id)
        print("\nYour Courses:")
        if my_courses:
            for course in my_courses:
                print(course)
        else:
            print("You are not enrolled in any courses.")

    def register_user(self):
        try:
            from user import User
            user_id = int(input("Enter a new user ID: "))
            self.bl.checkid(user_id)
            user_name = input("Enter your name: ")
            self.bl.checkname(user_name)
            user = User(user_id, user_name)
            if self.bl.register_user(user):
                print("Registration successful!")
            else:
                print("User ID already exists. Please try a different one.")
        except ValueError:
            print("Invalid input, please try again.")
            self.register_user()
            