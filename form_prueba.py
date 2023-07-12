import pygame
from pygame.locals import *


from GUI_button import *
from GUI_button_image import *
from GUI_form import *
from GUI_label import *
from GUI_slider import *
from GUI_textbox import *
from formulario_prueba_score import *
from class_nivelUno import *

class FormPrueba(Form):
    def __init__(self,screen, x, y, w, h,  color_fondo, color_borde = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_fondo,color_borde, border_size, active)

        self.volumen = 0.01
        self.flag_play = True

        pygame.mixer.init()

        ###
        self.btn_play = Button(self._slave,x,y,100,100,100,50,"Red","Blue", self.btn_play_click, "Nombre", "Pausa", font="Verdana", font_size=15, font_color="White")
        self.label = Label(self._slave, 650,190,100,50,"1%","comic Sans",15,"Black","API_FORMS\Table.png")
        self.slider_volumen = Slider(self._slave,x,y,100,200,500,15,self.volumen,"Blue","White")
        self.btn_tabla = Button_Image(self._slave,x,y,255,100,50,50,"API_FORMS\Menu_BTN.png",self.btn_tabla_click, "lalal")
        ###

        #Agregar a lista
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)



        pygame.mixer.music.load("Efectos e imagenes\sonidos\SaveTube.io - MI CORAZON ENCANTADO - AARON MONTALVO OFICIAL - DRAGON BALL GT FULL HD (128 kbps).mp3")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for wiget in self.lista_widgets:
                    wiget.update(lista_eventos)
                self.update_volume(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)

    def btn_play_click(self, texto):

        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color= "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color= "Black"
            self.btn_play.set_text("Pausa")
        
        self.flag_play = not self.flag_play
    
    def update_volume(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    def btn_tabla_click(self,texto):
        dic_score = [{"jugador": "Facundo", "score": 1000},
                     {"jugador": "Facundo", "score": 1000},
                     {"jugador": "Facundo", "score": 1000}]

        form_puntaje = FormMenuScore(self._master,0,0,1900,900,(220,0,220),"White",True,"API_FORMS\Window.png",dic_score,100,10,10)

        self.show_dialog(form_puntaje)