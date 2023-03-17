import sys
from unittest import result
from PyQt5 import QtWidgets, uic
from random import *

qtCreatorFile = "juego_tarea.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Game(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		super(Game, self).__init__(parent)
		uic.loadUi("juego_tarea.ui", self)
		
		self.btn_result.clicked.connect(self.btn_result_clicked)       
		self.btn_new_number.clicked.connect(self.btn_new_number_clicked)
		self.l_text_juegos.setText(str(0)) 
		self.l_text_malos.setText(str(0))
		self.text_result.setText(str(0))
		self.text_1.setText(str(0))
		self.text_2.setText(str(0))
		self.var_alea = 0
		self.var_juegos = 0
		self.var_buenos = 0
		self.var_malos = 0
		self.show()
	
	
	def radio_suma_clicked(self):
		self.l_text_signo.setText('+')

	def radio_resta_clicked(self):
		self.l_text_signo.setText('-')

	def radio_multiplicacion_clicked(self):
		self.l_text_signo.setText('*')

	def radio_division_clicked(self):
		self.l_text_signo.setText('/')


	
	def btn_result_clicked(self):
		if  self.var_alea != 0 :
			if self.var_alea == 1 and int(self.text_result.text()) == int(self.text_1.text()) + int(self.text_2.text()):
				self.var_buenos += 1
				self.l_text_buenos.setText(str(self.var_buenos))
				result = int(self.text_1.text()) + int(self.text_2.text())		
				self.text_result.setText(str(resultado))
			elif self.var_alea == 1 and int(self.text_result.text()) != int(self.text_1.text()) + int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
				resultado = int(self.text_1.text()) + int(self.text_2.text())		
				self.text_result.setText(str(result))
			elif self.var_alea == 2 and int(self.text_result.text()) == int(self.text_1.text()) - int(self.text_2.text()):
				self.var_buenos += 1		
				self.l_text_buenos.setText(str(self.var_buenos))
				result = int(self.text_1.text()) - int(self.text_2.text())		
				self.text_result.setText(str(result))
			elif self.var_alea == 2 and int(self.text_result.text()) != int(self.text_1.text()) - int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
				result = int(self.text_1.text()) - int(self.text_2.text())		
				self.text_result.setText(str(result))
			elif self.var_alea == 3 and int(self.text_result.text()) == int(self.text_1.text()) * int(self.text_2.text()):
				self.var_buenos += 1
				self.l_text_buenos.setText(str(self.var_buenos))
				resultado = int(self.text_1.text()) * int(self.text_2.text())		
				self.text_result.setText(str(result))
			elif self.var_alea == 3 and int(self.text_result.text()) != int(self.text_1.text()) * int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
				resultado = int(self.text_1.text()) * int(self.text_2.text())		
				self.text_result.setText(str(result))
			elif self.var_alea == 4 and float(self.text_result.text()) == float(self.text_1.text()) / float(self.text_2.text()):
				self.var_buenos += 1
				self.l_text_buenos.setText(str(self.var_buenos))
				result = float(self.text_1.text()) / float(self.text_2.text())		
				self.text_result.setText(str(resultado))
			elif self.var_alea == 4 and float(self.text_result.text()) != float(self.text_1.text()) / float(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
				resultado = float(self.text_1.text()) / float(self.text_2.text())		
				self.text_result.setText(str(result))

			self.var_juegos += 1
			self.l_text_juegos.setText(str(self.var_juegos))
		    
			


	
	def btn_new_number_clicked(self):
		self.var_alea = randint(1 , 4)
		
		if self.var_alea == 1:
			self.radio_suma_clicked()
			self.radio_suma.setChecked (True)
		elif self.var_alea == 2:
			self.radio_resta_clicked()
			self.radio_resta.setChecked(True)
		elif self.var_alea == 3:
			self.radio_multiplicacion_clicked()
			self.radio_multiplicacion.setChecked(True)
		elif self.var_alea == 4:
			self.radio_division_clicked()
			self.radio_division.setChecked(True)
		primer_numero = randint(1,50)
		segundo_numero = randint(1,50)
		self.text_1.setText(str(primer_numero))
		self.text_2.setText(str(segundo_numero))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Game()
    app.exec()

