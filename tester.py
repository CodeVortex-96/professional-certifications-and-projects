import os
import datetime

# --- A REZA PARA O WAYLAND NO ARCH (NÃO MEXER) ---
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_GL_BACKEND'] = 'gl'
os.environ['SDL_VIDEODRIVER'] = 'x11' 

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# Estilo Dark do Arch
Window.clearcolor = (0.1, 0.1, 0.1, 1)

# --- CLASSE BANCO DE DADOS (SIMPLIFICADA E FUNCIONAL) ---
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()
            return
        with open(self.filename, "r") as f:
            for line in f:
                if ";" in line:
                    email, password, name, created = line.strip().split(";")
                    self.users[email] = (password, name, created)

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            date = str(datetime.datetime.now()).split(" ")[0]
            self.users[email.strip()] = (password.strip(), name.strip(), date)
            self.save()
            return True
        return False

    def validate(self, email, password):
        if email in self.users:
            return self.users[email][0] == password
        return False

    def save(self):
        with open(self.filename, "w") as f:
            for u in self.users:
                f.write(f"{u};{self.users[u][0]};{self.users[u][1]};{self.users[u][2]}\n")

# Instância global do banco
db = DataBase("users.txt")

# --- INTERFACE (KV STRING) ---
KV = '''
WindowManager:
    LoginScreen:
    CreateAccountScreen:
    MainScreen:

<LoginScreen>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        padding: 50
        spacing: 15
        Label:
            text: "LOGIN SISTEMA"
            font_size: 30
            color: 0, 0.8, 1, 1
        TextInput:
            id: email
            hint_text: "Email"
            multiline: False
            size_hint_y: None
            height: "40dp"
        TextInput:
            id: password
            hint_text: "Senha"
            password: True
            multiline: False
            size_hint_y: None
            height: "40dp"
        Button:
            text: "ENTRAR"
            size_hint_y: None
            height: "50dp"
            on_release: root.do_login()
        Button:
            text: "Criar Conta"
            background_color: 0, 0, 0, 0
            color: 0, 1, 0.5, 1
            on_release: app.root.current = "create"

<CreateAccountScreen>:
    name: "create"
    BoxLayout:
        orientation: "vertical"
        padding: 50
        spacing: 15
        Label:
            text: "NOVA CONTA"
            font_size: 30
        TextInput:
            id: namee
            hint_text: "Nome Completo"
            multiline: False
        TextInput:
            id: email
            hint_text: "Email"
            multiline: False
        TextInput:
            id: password
            hint_text: "Senha"
            password: True
            multiline: False
        Button:
            text: "CADASTRAR"
            on_release: root.signup()
        Button:
            text: "Voltar"
            on_release: app.root.current = "login"

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: "vertical"
        padding: 50
        Label:
            id: user_info
            text: "Bem-vindo!"
            font_size: 25
        Button:
            text: "LOGOUT"
            size_hint_y: None
            height: "50dp"
            on_release: app.root.current = "login"
'''

# --- LÓGICA DAS TELAS ---
class LoginScreen(Screen):
    def do_login(self):
        if db.validate(self.ids.email.text, self.ids.password.text):
            # Passa o nome do usuário para a próxima tela
            user_data = db.users[self.ids.email.text]
            self.manager.get_screen("main").ids.user_info.text = f"Olá, {user_data[1]}!\\nEmail: {self.ids.email.text}"
            self.manager.current = "main"
            self.ids.email.text = ""
            self.ids.password.text = ""
        else:
            Popup(title='Erro', content=Label(text='Login Inválido'), size_hint=(0.6, 0.4)).open()

class CreateAccountScreen(Screen):
    def signup(self):
        name = self.ids.namee.text
        email = self.ids.email.text
        pwd = self.ids.password.text
        if name != "" and email != "" and pwd != "":
            if db.add_user(email, pwd, name):
                self.manager.current = "login"
            else:
                Popup(title='Erro', content=Label(text='Email já existe'), size_hint=(0.6, 0.4)).open()

class MainScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    MainApp().run()