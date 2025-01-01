import hashlib
import os
def generate_salt():
    return os.urandom(16).hex()
def generate_hash(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()
users = {}
def sign_up ():
    username = input('Enter username: ')
    password = input('Enter password: ')
    salt = generate_salt()
    password_hash = generate_hash(password, salt)
    if username not in users.keys():
        users[username] = [salt, password_hash]
        print('Sign-up successful')
    else:
        print('username already taken')
def login():
    username = input('Enter username: ')
    if username not in users.keys():
        print('username not found, please sign-up')
        return
    password = input('Enter password: ')
    hash_ = generate_hash(password, users[username][0])
    if hash_ == users[username][1]:
        print('Login successful')
    else:
        print('wrong password, try logging in again')
def main():
    while True:
        print('Sign-up = 1')
        print('Login = 2')
        print('Exit = 3')
        choice = input('Enter 1/2/3: ')
        if choice=='1':
            sign_up()
        elif choice=='2':
            login()
        else:
            break
        
if __name__ == "__main__":
    main()