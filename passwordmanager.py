import random

chars = 'abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
1234567890-=\
!"£$%^&*()_+'

ver = ('1.22')
# Ver 1.0, base version
# Ver 1.1 added write to text file
# Ver 1.21 writing in formatting
# Ver 1.22 added loop

print(f'Hello, welcome to password manager {ver}.')


def start():
    # user input
    website = input('What website is this for?: ')
    username = input(f'What is the username for {website}?: ')
    # password length
    passwordlength = input('How many characters for your password?: ')
    length = int(passwordlength)
    # password maker
    password = ''
    for randompassword in range(length):
        password += random.choice(chars)
    print(
        f'Okay, your username for {website} is {username} and the password is {password}')
    # file save
    # Add own path for save file
    database = (open(r'C:\Users\Mike!\Desktop\testfile.txt', 'a'))
    database.write(
        f'\nWebsite: {website}\nUsername: {username}\nPassword: {password}\n')
    print('Congratulations! This has been saved to the database.')
    # loop
    print('Would you like to add another? Y/N ')
    addanother = input()
    while addanother == 'Y' or addanother == 'y':
        start()
    if addanother == 'N' or addanother == 'n':
        database.close()
        print(f'Thank you for using password manager {ver}!')
        input('Press any key to quit.')
        quit()


start()
