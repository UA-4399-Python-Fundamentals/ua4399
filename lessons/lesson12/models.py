class User:
    def __init__(self, pk, username, email, password):
        self.pk = pk
        self.username = username
        self.email = email
        self.password = password  # WARNING: Never store passwords in plain text!

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email
    def get_pk(self):
        return self.pk

    def to_dict(self):
        return {
            "pk": self.pk,
            "username": self.username,
            "email": self.email,
            "password": self.password,  # WARNING: Never store passwords in plain text!
        }   
    def __str__(self):
        return f"User(pk={self.pk}, username='{self.username}', email='{self.email}')"

    def __repr__(self):
        return f"User(pk={self.pk}, username='{self.username}', email='{self.email}', password='{self.password}')" #Added pk

    def change_password(self, new_password):
        self.password = new_password #  WARNING: Never store passwords in plain text!
        print("Password changed successfully.") # Added a print statement for confirming password change



def generate_users(num_users=10):
    """Generates a list of User objects.

    Args:
        num_users (int, optional): The number of users to generate. Defaults to 10.

    Returns:
        list: A list of User objects.
    """
    users = []
    for i in range(1, num_users + 1):
        str_pk = str(i).zfill(3)
        username = f"user_{str_pk}"
        email = f"user_{str_pk}@example.com"
        password = f"password{i}"  # WARNING: Never store passwords in plain text!
        users.append(User(i, username, email, password))
    return users