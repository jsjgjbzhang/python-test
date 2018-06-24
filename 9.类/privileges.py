from user import User

class Privileges():
    """docstring for Privileges"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def showPrivileges(self):
        for x in self.privileges:
            print(x)

    def addPrivileges(self,value):
    	self.privileges.append(value)


class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()

