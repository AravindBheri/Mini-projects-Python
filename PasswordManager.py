from cryptography.fernet import Fernet

'''
def write_key():
    
    key = Fernet.generate_key()
    
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''
        
def load_key():
    
    f = open('key.key', 'rb')
    key = f.read()
    f.close()
    return key

master_pwd = input("Enter the master password: ")

key = load_key()
fer = Fernet(key)

def view():
    
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pd = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(pd.encode()).decode())

def add():
    
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view the existing one's (view, add)? or Q to quit. ").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Enter a valid mode.")
        continue