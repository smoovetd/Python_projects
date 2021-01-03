from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import os
import random
import pathlib
import glob
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from difflib import SequenceMatcher

Builder.load_file('design.kv')

def is_file_non_empty(path):
    is_empty = os.path.isfile(path) and os.path.getsize(path) > 0
    print(path, is_empty)
    return is_empty

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'

    def login(self, username, password):
        users = dict()
        if is_file_non_empty('users.json') == True:
            with open ('users.json') as file:
                users = json.load(file)

        if username in users.keys()and users[username]['username'] == username and users[username]['password'] == password:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = 'Error: incorrect username/password'

    def go_to_password_reset(self):
        self.manager.current = 'password_reset'

class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.current = 'login_screen'

    def enlight(self, mood):
        file_path = ''
        available_moods = [ pathlib.Path(item).stem for item in glob.glob('quotes/*.txt')]
        if mood in available_moods:
            file_path = f'quotes/{mood}.txt'
            with open(file_path, 'r') as file:
                output_content = random.choice(file.readlines())
        else:
            output_content = 'Unsupported mood: ' + mood

        self.ids.output.text = output_content

    def go_to_add_quote(self):
        self.manager.current = 'add_quote'

class AddNewQuoteScreen(Screen):
    matcher_ratio = 0.95

    def go_to_login_success(self):
        self.manager.current = 'login_screen_success'

    def add_quote(self, mood, quote):
        file_path = ''
        available_moods = [ pathlib.Path(item).stem for item in glob.glob('quotes/*.txt')]
        file_path = f'quotes/{mood}.txt'
        if is_file_non_empty(file_path) == True:
            with open (file_path, 'r') as file:
                crnt_quotes = file.readlines()
            with open(file_path, 'a') as file:
                is_quote_existing = False
                quote = quote + '\n'
                for single_quote in crnt_quotes:
                    if SequenceMatcher(a = quote, b = single_quote).ratio() >= self.matcher_ratio:
                        is_quote_existing = True
                        break

                if is_quote_existing == True:
                    self.ids.output.text = 'This quote already exists'
                else:
                    file.writelines(quote)
                    self.ids.output.text = 'Quote is successfully added'
        else:
            with open(file_path, 'w+') as file:
                file.writelines(quote)
                self.ids.output.text = 'Quote is successfully added'


class SignUpScreen(Screen):
    def add_user(self, username, password):
        users = dict()
        if is_file_non_empty('users.json') == True:
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

class ForgotPasswordScreen(Screen):
    def change_pass(self, uname, newpword):
        if is_file_non_empty('users.json') == True:
            with open ('users.json', 'r') as file:
                users = json.load(file)

            if uname in users.keys():
                users[uname]['password'] = newpword
                with open ('users.json', 'w') as file:
                    json.dump(users, file)
                self.ids.confirmation.text = 'Successfull password reset'
        else:
            self.ids.confirmation.text = 'Error: No such User.'

    def go_to_login(self):
        self.manager.current = 'login_screen'

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
