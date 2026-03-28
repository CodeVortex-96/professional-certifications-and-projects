import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Definição das cores (RGBA)
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class HboxLayoutExample(App): # Herdando de App para o Kivy saber que isso é um aplicativo
    def build(self):
        # O layout principal onde os botões serão inseridos
        layout = BoxLayout(padding=10) # 'B' maiúsculo aqui

        colors = [red, green, blue, purple]

        for i in range(5): # Adicionado o 'i' que faltava
            btn = Button(
                text=f"Botão #{i+1}",
                background_color=random.choice(colors) # 'b' minúsculo aqui
            )
            layout.add_widget(btn)
            
        return layout

if __name__ == "__main__": # 'm' minúsculo aqui
    app = HboxLayoutExample()
    app.run()