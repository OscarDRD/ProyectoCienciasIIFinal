from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ArbolesView.ArbolesCanvas import ArbolesCanvas
from ArbolesView.Nodo import Nodo
import copy

class ArbolesView(QGroupBox):
    def __init__(self,p:QWidget):
        super().__init__(p)
        self.pasos:list[Nodo] = []

        self.alfabeto = {}

        self.canvas = ArbolesCanvas(None)
        self.canvas.setGeometry(0,0,2000,650)
        self.canvasArea = QScrollArea(self)
        self.canvasArea.setGeometry(40,20,802,652)
        self.canvasArea.setWidget(self.canvas)
        self.canvasArea.setStyleSheet("background-color:#EBE6D2")

        self.setStyleSheet("background-color:#E6EBE0")

        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setHorizontalHeaderLabels(["Código","Letra"])
        self.tabla.setGeometry(860,20,200,310)
        self.tabla.setColumnWidth(0,100)
        self.tabla.setColumnWidth(1,100)
        self.tabla.setFont(QFont("Century Gothic",7))
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#D0C0A7}")

        panelOpciones = QGroupBox(self)
        panelOpciones.setGeometry(860,345,200,330)
        panelOpciones.setStyleSheet("QGroupBox{border:1px solid black; background-color:#D0C0A7}")

        label = QLabel("Clave",panelOpciones)
        label.move(80,30)
        label.setFont(QFont("Century Gothic",10))
        label.setStyleSheet("background-color:#D0C0A7")
        self.campoPalabra = QTextEdit(panelOpciones)
        self.campoPalabra.setGeometry(30,50,140,30)
        self.campoPalabra.setFont(QFont("Century Gothic",10))
        self.campoPalabra.setStyleSheet("background-color:#EBE6D2")
        self.campoPalabra.setFrameStyle(1)
        
        label = QLabel("Tipo Árbol",panelOpciones)
        label.move(70,100)
        label.setFont(QFont("Century Gothic",10))
        label.setStyleSheet("background-color:#D0C0A7")
        self.opcionTipoArbol = QComboBox(panelOpciones)
        self.opcionTipoArbol.setGeometry(30,130,140,30)
        self.opcionTipoArbol.setFont(QFont("Century Gothic",10))
        self.opcionTipoArbol.setStyleSheet("background-color:#EBE6D2")
        self.opcionTipoArbol.addItems(["Digital","Residuos (TRIES)"])

        label = QLabel("Paso",panelOpciones)
        label.move(35,235)
        label.setFont(QFont("Aera Gothic",10))
        label.setStyleSheet("background-color:#D0C0A7")
        self.opcionPasos = QComboBox(panelOpciones)
        self.opcionPasos.setGeometry(70,230,100,30)
        self.opcionPasos.setFont(QFont("Century Gothic",10))
        self.opcionPasos.setStyleSheet("background-color:#EBE6D2")
        self.opcionPasos.currentIndexChanged.connect(self.actualizarCanvas)

        botonGenerar = QPushButton("Generar",panelOpciones)
        botonGenerar.setGeometry(30,270,140,30)
        botonGenerar.setStyleSheet("QPushButton{background-color:#D7A184; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#D4C2AD;}"
                                   "QPushButton::pressed{background-color:#EFDFCC; }")
        botonGenerar.clicked.connect(self.generarArbol)
        
    def actualizarCanvas(self):
        if(self.opcionPasos.currentText() != ""):
            self.canvas.arbol = self.pasos[int(self.opcionPasos.currentText())-1]
            self.canvas.activo = True
            self.canvas.update()

    def generarArbol(self):
        #genera el diccionario de claves
        self.alfabeto = {}
        self.pasos = []
        for i in self.campoPalabra.toPlainText().upper():
            self.alfabeto[i] = bin(ord(i)-64).replace("0b","")
            self.alfabeto[i] = ("0"*(5-len(self.alfabeto[i])))+self.alfabeto[i]
        raiz = Nodo()
        nodo = raiz
        #genera el arbol segun estructura
        if self.opcionTipoArbol.currentText() == "Digital":
            for i in self.alfabeto:
                #generar arbol para paso
                digito = 0
                for x in self.alfabeto[i]:
                    digito += 1
                    if len(nodo.hijos) == 0:
                        nodo.hijos.append(Nodo())
                        nodo.hijos.append(Nodo())
                    if nodo.hijos[int(x)].valor == "":
                        nodo.hijos[int(x)].valor = i
                        nodo = raiz
                        break
                    else:
                        nodo = nodo.hijos[int(x)]
                        continue
                if digito  > raiz.niveles:
                    raiz.niveles = digito
                self.pasos.append(copy.deepcopy(raiz))
        elif self.opcionTipoArbol.currentText() == "Residuos (TRIES)":
            raiz.hijos.append(Nodo())
            raiz.hijos.append(Nodo())
            for i in self.alfabeto:
                digito = 0
                save = False
                nodo = raiz
                while not save:
                    if (len(nodo.hijos) == 0):
                        if nodo.valor == "":
                            nodo.valor = i
                            save = True
                            break
                        else:
                            nodo.hijos.append(Nodo())
                            nodo.hijos.append(Nodo())
                            print(digito)
                            nodo.hijos[int(self.alfabeto[nodo.valor][digito])].valor = nodo.valor
                            nodo.valor = ""
                    else:
                        nodo = nodo.hijos[int(self.alfabeto[i][digito])]
                        digito += 1
                if digito > raiz.niveles:
                    raiz.niveles = 4
                self.pasos.append(copy.deepcopy(raiz))
        self.opcionPasos.clear()
        for u in range(1,len(self.pasos)+1):
            self.opcionPasos.addItem(str(u))
        contador = 0
        self.tabla.setRowCount(0)
        for i in self.alfabeto:
            self.tabla.insertRow(contador)
            self.tabla.setItem(contador,0,QTableWidgetItem(i))
            self.tabla.setItem(contador,1,QTableWidgetItem(self.alfabeto[i]))
            contador += 1
                    
        



    
        
    
