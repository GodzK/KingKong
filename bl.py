class BL:
    def __init__(self):
        self.user_data = {}
        self.currentid = ''
        self.course_data = {
            "Discrete": [671305, 516712],
            "Ux-Ui": [671304, 671300],
            "DesignThinking": [671345, 671378]
        }

    def current_user(self, user_id):
        self.currentid = user_id

    def get_currentid(self):
        return self.currentid

    def logout(self):
        self.currentid = ''

    def enroll(self, course, user_id):
        self.course_data[course].append(user_id)
        print(self.course_data)
    
    def duplicate_enroll_corse(self, course_enroll):
        if course_enroll in self.course_data[course_enroll]:


    def get_user_data(self):
        return self.user_data

    def get_course_data(self):
        return self.course_data

    def check_duplicate(self, user_id):
        return user_id not in self.user_data

    def register_user(self, user):
        user_id = user.get_user_id()
        user_name = user.get_user_name()
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

    def checkid(self, user_id):
        if user_id == "":
            raise ValueError
        if not (67130500000 < user_id < 67130500200):
            raise ValueError
    


    def checkname(self, username):
        if username.isdigit() or username == "":
            raise ValueError
