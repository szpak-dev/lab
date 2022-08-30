class User:
    def __init__(self, identifier, name, email, login, password):
        self._id = identifier
        self._name = name
        self._email = email
        self._login = login
        self._password = password

    def change_password(self, current_password, new_password):
        """Password must be at least 10 characters long and match current one"""
        if current_password != self._password:
            raise Exception('You must provide valid old password')

        if len(new_password) < 10:
            raise Exception('New password must be at least 10 characters long')

        self._password = new_password

    def update_email(self, new_email):
        """No special requirements, it's just a setter"""
        self._email = new_email
