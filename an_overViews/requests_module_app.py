import requests
import json

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com/"
        self.token = "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"

    def findUser(self, username):
        response = requests.get(self.api_url + "users/" + username)
        return response.json()
    
    def getRepository(self, username):
        
        response = requests.get(self.api_url + "users/" + username + "/repos") 
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url + 'user/repos?access_token=' + self.token, json = {
            "name":name,
            "description":"This is your first repository",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })

        return response.json() 

github = Github()

while True:
    secim = input("1- Find User\n2- Get Reppository\n3- Create Repository\n4- Exit\nSeçiminiz: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Kullanıcı Adınızı Giriniz: ")
            result = github.findUser(username)
            print(f" name: {result['name']} bio: {result['bio']} location: {result['location']}  ")

        elif secim == "2":
            username = input("Kullanıcı Adınızı Giriniz: ")
            result = github.getRepository(username)
            for repo in result:
                print(repo['name'])
            
        elif secim == "3":
            name = input("repository name: ")
            result = github.createRepository(name)
            print(result)


        else:
            print("Yanlış Seçim Yaptınız.")










# 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