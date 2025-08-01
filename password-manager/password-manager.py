from cryptography.fernet import Fernet # symmetric cryptography
import json

#load
def load_key():
    return open('secret.key', 'rb').read() #rb - read binary. secret.key - file

#Save encrypted password
def save_password(service, password):
    key = load_key() # get the key
    f = Fernet(key) # instance of Fernet object with key (bytes)

    # .encode() - from str to bytes
    # .encrypt() - return  ciphertext (bytes)
    encrypted_password = f.encrypt(password.encode())

    with open("passwords.json", 'r') as file:
        passwords = json.load(file) #read json and convert into python file

    passwords[service] = encrypted_password.decode() #.decode() turns bytes to str

    with open("passwords.json", 'w') as file: #write in file
        json.dump(passwords, file) #from python file to json format
    file.close()
#Retrieve password
def get_password(service):
    key = load_key()
    f = Fernet(key)

    with open('passwords.json', 'r') as file:
        passwords = json.load(file)

    encrypted_password = passwords.get(service)
    file.close()
    if encrypted_password:
        return f.decrypt(encrypted_password.encode()).decode()
    return None


def show_services():

    with open('passwords.json', 'r') as file:
        passwords = json.load(file)
        print(*passwords.keys() if passwords != {} else 'The passwords list is empty')
    file.close()


def delete_service(service):

    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)

        if service in passwords:
            del passwords[service]

        with open('passwords.json', 'w') as file:
            json.dump(passwords, file)
        file.close()
        print(f'{service.upper()} service was deleted from password manager')
    except Exception as e:
        print('Something went wrong!\n', e)

def print_get_choices():
    choice = input(
        "1. Save Password\t2. Retrieve Password\t3. Show services\t4. Delete service and password\t5. Exit\nChoose an option (e.g. 1(save password)): ")
    return choice



if __name__ == "__main__":
    #TO DO
    #MAKE A LOOP with command 'exit' for exiting the programm - done
    #show created services - done
    #delete option for services - done
    choice = print_get_choices()
    while choice != '5':
        match choice:
            case '1':
                service = input('Enter the service name: ').lower()
                password = input('Enter the password: ')
                save_password(service, password)
                print('Passsword saved!')
            case '2':
                service = input('Enter the service name to retrieve (e.g. Youtube(str)): ')
                password = get_password(service)
                if password:
                    print('Password: ', password)
                else:
                    print('Service not found.')
            case '3':
                show_services()
            case '4':
                service = input('Enter the service name to delete (e.g. Youtube(str)): ')
                delete_service(service)
            case '5':
                break
            case _:
                print('Command not found')
                print('type the number-->1(save password)')

        choice = print_get_choices()