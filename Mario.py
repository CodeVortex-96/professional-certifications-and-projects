from kivy.app import App
from kivy.uix.image import Image, AsyncImage # Corrigi o 'i' minúsculo aqui também

class MainApp(App):
    def build(self):
        # Removi a vírgula que estava sobrando depois da URL e alinhei os argumentos
        img = AsyncImage(
            source='https://supermariorun.com/assets/img/stage/mario03.png',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
                                            