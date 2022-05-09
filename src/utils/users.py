from src.IO import io


class users:
    def __init__(self, message):
        self.id = message.from_user.id
        self.first_name = message.from_user.first_name
        self.last_name = message.from_user.last_name
        self.username = message.from_user.username

    def store_data(self):
        # You must make it dynamic to add all attr to json file
        data = '{' + f"id: {self.id}, first_name: {self.first_name}, username: {self.username}" + '}'
        io.write_json(f"src/db/user/{self.id}", data)

def create_user(self, message):
    self.users.update({message.from_user.id: users(message)})
    self.users[message.from_user.id].store_data()
