class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName(self):
        print(f"Имя: {self.first_name}")

    def getLasttName(self):
        print(f"Фамилия: {self.last_name}")

    def getName(self):
        print(f"Имя и фамилия: {self.first_name} {self.last_name}")
