# Author:Lithlu
import time
user,passwd = "lithlu","abc123"
def auth(auth_type):
    print("auth func:",auth_type)
    def out_wrapper(func):
        def wrapper(*args, **kvargs):
            print("wrapper func args:", *args,**kvargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication \033[0m")
                    res = func(*args, **kvargs)  # from home
                    print("----after authentication ")
                    return res
                else:
                    exit("\003[31;1mInvild username or password")
            elif auth_type == "ldap":
                print("------------")
        return wrapper
    return out_wrapper
def index():
    print("welcome to index page!")
@auth(auth_type = "local") # 本地认证  home = wrapper()
def home():
    print("welcome to home page!")
    return "From home"
@auth(auth_type = "ldap") #ldap认证
def bbs():
    print("welcome to bbs page!")
index()
print(home()) # run wrapper()
bbs()