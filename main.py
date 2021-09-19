import instaloader

def getPic(username):
    engine = instaloader.Instaloader()
    print(engine.download_profile(username, profile_pic_only=True))


if __name__ == '__main__':
    try:
        getPic(input("Enter the username: "))
    except:
        print("Invalid username or Something went wrong!!!")
