from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import os

Builder.load_file('design.kv')

def is_file_empty(path):
    is_empty = os.path.isfile(path) and os.path.getsize(path) > 0
    print(path, is_empty)
    return is_empty

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'

    def login(self, username, password):
        users = dict()
        if is_file_empty('users.json') == True:
            with open ('users.json') as file:
                users = json.load(file)

        if username in users.keys()and users[username]['username'] == username and users[username]['password'] == password:
            self.manager.current = 'login_screen_success'
        else:
            print('Error: incorrect username/password')

class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.current = 'login_screen'

    def enlight(self, mood):
        print('Mood is: ', mood)
        pass


class SignUpScreen(Screen):
    def add_user(self, username, password):
        users = dict()
        if is_file_empty('users.json') == True:
            #print('SignUpScreen in here')
            with open('users.json', 'r') as file:
                users = json.load(file)

        users[username] = {
            'username': username,
            'password': password,
            'created' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        #print(users)
        with open('users.json', 'w') as file:
            json.dump(users, file)

        self.manager.current = 'sign_up_screen_success'

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = 'login_screen'

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
