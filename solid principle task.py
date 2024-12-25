# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:59:11 2024

@author: EMAN
"""
from abc import ABC
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class UserRepository(ABC):
    
    def save(self,user):
        pass
    
    def list_all(self):
        pass
class inMemoryRepository(UserRepository):
    def __init__(self):
        self.users=[]
    def save(self,user):
        self.users.append(user)
    def list_all(self):
        return self.users
class Notifier(ABC):
   
    def send(self,user):
        pass
class SMSNotifier(Notifier):
    def send(self,user):
        print(f"SMS:hello{user.name},Your email has been registered:{user.email}.")
class UserManager:
    def __init__(self,repository,notifier):
        self.repository=repository
        self.notifier=notifier
    def add_user(self, name, email):
        user = User(name, email)
        self.repository.save(user)
        self.notifier.send(user)    
    def show_users(self):
        for idx, user in enumerate(self.repository.list_all(), start=1):
            print(f"{idx}. {user.name} - {user.email}")
if __name__ == "__main__":
    repo = inMemoryRepository()
    notifier = SMSNotifier()
    manager = UserManager(repo, notifier)
manager.add_user("eman","eman@example.com")
manager.add_user("elham","elham@example.com")
print("\n users list")
manager.show_users()    
    
    

