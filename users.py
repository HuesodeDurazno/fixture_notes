class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, role):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = {'password': password, 'role': role}

    def login(self, username, password):
        if username not in self.users:
            raise ValueError("User does not exist")
        if self.users[username]['password'] != password:
            raise ValueError("Incorrect password")
        return True

    def find_users_by_role(self, role):
        return [username for username, details in self.users.items() if details['role'] == role]
    

