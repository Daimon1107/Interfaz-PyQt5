from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp,self).__init__(parent)
        self.setFixedSize(1170,342)
        self.setWindowTitle("Interfaz")
        
        #! Conectar con css 
        
        self.setObjectName("designer")
        with open("stylesQt.css") as f:
            self.setStyleSheet(f.read())
        
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        #! label titulo
        self.label = QLabel("Bienvenido",self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(230, 0, 321, 71)
        #? Tipó de letra
        font = QFont()
        font.setFamily("MV Boli")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        
        #! label subtitulo
        self.label_2 = QLabel("Puedes elegir alguna de estas opciones:",self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(80, 90, 341, 61)
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        
        #! labels de opciones  
        #? sub label 1
        self.label_3 = QLabel("1.- Imagen",self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 150, 81, 21))
        
        font2 = QFont()  #? este font uso para todos los label de las opciones
        font2.setFamily("Leelawadee UI Semilight")
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        
        self.label_7 = QLabel("2.- Matriz de pulsadores",self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 180, 161, 31))
        self.label_7.setFont(font2)
        self.label_4 = QLabel("3.-  Matriz de QlLineEdit",self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 220, 171, 21))
        self.label_4.setFont(font2)
        self.label_5 = QLabel("4.- Grafica de Matlib",self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 260, 141, 21))
        self.label_5.setFont(font2)
        
        #! Combo box
        
        self.ComboBox = QComboBox(self.centralwidget)
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.setGeometry(QRect(490, 185, 191, 51))
        self.ComboBox.addItems(["Selecciona","Opción 1","Opción 2","Opción 3", "Opción 4"])
        self.ComboBox.activated.connect(self.switchPage)
        font3 = QFont()
        font3.setFamily(u"MS Sans Serif")
        font3.setPointSize(12)
        self.ComboBox.setFont(font3)
        
        #? Se esta probando el codigo para el layout vertical al lado derecho
        
        self.verticalLayoutWidget = QWidget(self.centralwidget)  #? Widget adicional en la parte derecha
        self.verticalLayoutWidget.setGeometry(QRect(750,0,410,370))
        
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        
        #? Se crea la pagina 0 y la union
        self.stackedLayout = QStackedLayout()
        
        self.page0 = QWidget()
        universidad = QLabel("<h1>UNIVERSIDAD TÉCNICA DE AMBATO</h1>",self.page0)
        
        facultad = QLabel("<h2>FACULTAD DE INGENIERIA EN SISTEMAS</h2>",self.page0)
        facultad.setGeometry(22,30,400,30)
        materia = QLabel("<h3>PROGRAMACIÓN AVANZADA</h3>",self.page0)
        materia.setGeometry(115,60,400,30)
        integrantes = QLabel("<h3>Integrantes:</h3>",self.page0)
        integrantes.setGeometry(50,90,100,30)
        damian = QLabel("<h4>Damián Alban</h4>",self.page0)
        damian.setGeometry(100,110,100,30)
        
        karina = QLabel("<h4>Karina Yucailla</h4>",self.page0)
        karina.setGeometry(100,130,100,30)
        
   
        self.label0  =QLabel(self.page0)
        self.label0.move(250,150)
        pixmap0 = QPixmap("logo.jpg")
        self.label0.setPixmap(pixmap0)
        
        
        
        self.stackedLayout.addWidget(self.page0)
        
        #? crear el cambio y la pagina 1
        
        self.page1 = QWidget()
        self.page1Layout = QVBoxLayout()
        self.labelimage = QLabel()
        pixmap = QPixmap("python.jpg")
        self.labelimage.setPixmap(pixmap)
        self.page1Layout.addWidget(self.labelimage)
        self.page1.setLayout(self.page1Layout)
        
        self.stackedLayout.addWidget(self.page1)
        
        #? Se crea la pagina 2
        
        self.page2 = QWidget()
        
        self.labelpage2 = QLabel("<h2>Matriz Pulsadores</h2>",self.page2)
        self.labelpage2.resize(300,40)
        #self.labelpage2.setGeometry(QRect(0,0,100,100))
        
        self.gridLayout_Btnes  =QGridLayout()
        
        self.btn_push1 = QPushButton("0")
        self.btn_push2 = QPushButton("0")
        self.btn_push3 = QPushButton("0")
        self.btn_push4 = QPushButton("0")
        self.btn_push5 = QPushButton("0")
        self.btn_push6 = QPushButton("0")
        
        self.btn_push1.setFixedSize(80,40)
        self.btn_push2.setFixedSize(80,40)
        self.btn_push3.setFixedSize(80,40)
        self.btn_push4.setFixedSize(80,40)
        self.btn_push5.setFixedSize(80,40)
        self.btn_push6.setFixedSize(80,40)
        
        self.btn_push1.setObjectName("btn_push")
        self.btn_push2.setObjectName("btn_push")
        self.btn_push3.setObjectName("btn_push")
        self.btn_push4.setObjectName("btn_push")
        self.btn_push5.setObjectName("btn_push")
        self.btn_push6.setObjectName("btn_push")
        
        self.gridLayout_Btnes.addWidget(self.btn_push1,0,0)     
        self.gridLayout_Btnes.addWidget(self.btn_push2,0,1)     
        self.gridLayout_Btnes.addWidget(self.btn_push3,1,0)        
        self.gridLayout_Btnes.addWidget(self.btn_push4,1,1)        
        self.gridLayout_Btnes.addWidget(self.btn_push5,2,0)
        self.gridLayout_Btnes.addWidget(self.btn_push6,2,1)
        
        self.page2.setLayout(self.gridLayout_Btnes)
        
        self.btn_push1.clicked.connect(lambda: self.aumentarPush("btn1"))
        self.btn_push2.clicked.connect(lambda: self.aumentarPush("btn2"))
        self.btn_push3.clicked.connect(lambda: self.aumentarPush("btn3"))
        self.btn_push4.clicked.connect(lambda: self.aumentarPush("btn4"))
        self.btn_push5.clicked.connect(lambda: self.aumentarPush("btn5"))
        self.btn_push6.clicked.connect(lambda: self.aumentarPush("btn6"))

        self.stackedLayout.addWidget(self.page2)     
        
        #? Se crea la pagina 3
           
        self.page3 = QWidget()
        self.Horizontaltitulo = QVBoxLayout()

        self.labelpag3 = QLabel("<h4>Ingrese los numeros que desea sacar la gráfica:</h4> ",self.page3)
        self.labelpag3.resize(300,40)
        
        #self.labelpag3.setGeometry(0,0,300,70)
        self.labelpag3.setObjectName("labelpage3")
        
        self.gridLayout_Qedit =QGridLayout()
        
        self.Qline1 = QLineEdit()
        self.Qline2 = QLineEdit()
        self.Qline3 = QLineEdit()
        self.Qline4 = QLineEdit()
        self.Qline5 = QLineEdit()
        self.Qline6 = QLineEdit()
        
        self.gridLayout_Qedit.addWidget(self.Qline1,0,0)     
        self.gridLayout_Qedit.addWidget(self.Qline2,0,1)     
        self.gridLayout_Qedit.addWidget(self.Qline3,1,0)        
        self.gridLayout_Qedit.addWidget(self.Qline4,1,1)        
        self.gridLayout_Qedit.addWidget(self.Qline5,2,0)
        self.gridLayout_Qedit.addWidget(self.Qline6,2,1)
        
        self.Qline1.setObjectName("Lines")
        self.Qline2.setObjectName("Lines")
        self.Qline3.setObjectName("Lines")
        self.Qline4.setObjectName("Lines")
        self.Qline5.setObjectName("Lines")
        self.Qline6.setObjectName("Lines")
        
      
        self.page3.setLayout(self.gridLayout_Qedit)
        self.btn_enviar = QPushButton("Enviar",self.page3)
        
        self.gridLayout_Qedit.addWidget(self.btn_enviar,3,1)
        self.btn_enviar.setObjectName("btn_enviar")
        self.btn_enviar.setGeometry(10,10,80,40)
        
        self.btn_enviar.clicked.connect(self.ext_datos)
        
        
        self.stackedLayout.addWidget(self.page3)
        
        #? Se crea la pagina 4
        
        self.page4 = QWidget()
        self.button_grafica = QPushButton("Grafica",self.page4)
        self.button_grafica.clicked.connect(self.mostrar_grafica)
        self.button_grafica.setGeometry(150,90,100,50)
        
        self.stackedLayout.addWidget(self.page4)
        
        #! Se envia el stackedLayout al layout vertical alado
        
        self.verticalLayout.addLayout(self.stackedLayout)
    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.ComboBox.currentIndex())
    
    def ext_datos(self):
        try:
 
            self.dato1 = int(self.Qline1.text())
            self.dato2= int(self.Qline2.text())
            self.dato3=int(self.Qline3.text())
            self.dato4=int(self.Qline4.text())
            self.dato5 = int(self.Qline5.text())
            self.dato6 = int(self.Qline6.text())
        except:
            print("No ha enviado datos")
            
    def aumentarPush(self,aument):
        if aument=="btn1":
            a = int(self.btn_push1.text())+1
            self.btn_push1.setText(str(a))
        if aument=="btn2":
            a = int(self.btn_push2.text())+1
            self.btn_push2.setText(str(a))
        if aument=="btn3":
            a = int(self.btn_push3.text())+1
            self.btn_push3.setText(str(a))
        if aument=="btn4":
            a = int(self.btn_push4.text())+1
            self.btn_push4.setText(str(a))
        if aument=="btn5":
            a = int(self.btn_push5.text())+1
            self.btn_push5.setText(str(a))
        if aument=="btn6":
            a = int(self.btn_push6.text())+1
            self.btn_push6.setText(str(a))
        
    def mostrar_grafica(self):
        try:
            xpoints_1 = np.array([self.dato1,self.dato2,self.dato3])
        
            plt.plot(xpoints_1)
            plt.show()
        except: 
            print("No se han ingresado datos")
        
if __name__=='__main__':
    app = QApplication([])
    app.setStyle("plastique")
    window= MainApp()
    
    window.show()
    app.exec_()

