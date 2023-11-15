from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QColor

from indicesCanvas  import LogicIndexs

class IndicesView(QtW.QGroupBox):
    def __init__(self, p: QWidget):
        super().__init__(p)

        self.x = 10
        self.y = 60
        self.w = 200
        self.h = 600

        self.logica = LogicIndexs()

        self.ventanaCanvas = QtW.QScrollArea(self)
        self.ventanaCanvas.setGeometry(450,30,950,700)
        self.ventanaCanvas.verticalScrollBar().setVisible(False)
        self.ventanaCanvas.verticalScrollBar().setEnabled(False)
        self.ventanaCanvas.horizontalScrollBar().setVisible(True)
        self.ventanaCanvas.horizontalScrollBar().setEnabled(True)
        self.ventanaCanvas.setStyleSheet("background-color:white")
        self.ventanaCanvas.setFrameStyle(1)

        self.panel = QtW.QWidget(None)
        self.panel.setGeometry(0,0,2100,695)
        self.panel.setStyleSheet("border: 0px")
        self.ventanaCanvas.setWidget(self.panel)

        self.ListaEstructuras = []
        self.ListaTitulos = []
        for i in range(0, 10):
            s = 0
            if i > 0:
                s+= 10 * i
            
            label = QtW.QLabel("", self.panel)
            label.move(self.x + (i * 200) + s, self.y - 40)
            label.resize(self.w, 15)
            label.setFont(QFont("Times", 13, QFont.Bold))
            label.setVisible(False)

            self.ListaTitulos.append(label)

            Structura = QtW.QTableWidget(self.panel)
            Structura.setGeometry(self.x + (i * 200) + s, self.y, self.w, self.h)

            Structura.setColumnCount(2)

            header_item = QtW.QTableWidgetItem("Dir")
            header_item.setFont(QFont("Times", 13, QFont.Bold))
            Structura.setHorizontalHeaderItem(0,header_item)
            Structura.setColumnWidth(0, 50)

            header_item = QtW.QTableWidgetItem("Clave")
            header_item.setFont(QFont("Times", 13, QFont.Bold))
            Structura.setHorizontalHeaderItem(1,header_item)
            Structura.setColumnWidth(1, 144)

            Structura.horizontalHeader().setStyleSheet("border: 2px solid black")
            Structura.verticalHeader().setStyleSheet("border: 2px solid black")
            Structura.setStyleSheet("background-color:white; border: 2px solid black")
            Structura.verticalHeader().setVisible(False)
            Structura.setFont(QFont("Times", 10))

            Structura.setVisible(False)

            self.ListaEstructuras.append(Structura)

        self.setStyleSheet("background-color:#CBF5E3; "+
                           "border: 3px solid black;" +
                           "border-top-left-radius: 5px;" +
                           "border-top-right-radius: 5px;" +
                           "border-bottom-left-radius: 5px;" +
                           "border-bottom-right-radius: 5px;")
        
        # Registro Procesos
        # Tipo de indice
        label = QtW.QLabel("Tipo de Indice: ", self)
        label.move(11, 40)
        label.setFont(QFont("Times", 13, QFont.Bold))
        label.setStyleSheet("border: 0px solid white")
        self.opcionIndice = QtW.QComboBox(self)
        self.opcionIndice.addItems(["Primario", "Secundario"])
        self.opcionIndice.move(280, 40)
        self.opcionIndice.resize(150, 30)
        self.opcionIndice.setFont(QFont("Times", 13, QFont.Bold))
        # Niveles 
        label = QtW.QLabel("Niveles Estructura:", self)
        label.move(11, 100)
        label.setFont(QFont("Times", 13, QFont.Bold))
        label.setStyleSheet("border: 0px solid white")
        self.opcionNivel = QtW.QComboBox(self)
        self.opcionNivel.addItems(["Un Nivel", "Multinivel"])
        self.opcionNivel.move(280, 100)
        self.opcionNivel.resize(150, 30)
        self.opcionNivel.setFont(QFont("Times", 13, QFont.Bold))
        # Tamaño de Bloque 
        label = QtW.QLabel("Tamaño de Bloque:", self)
        label.move(11, 160)
        label.setFont(QFont("Times", 13, QFont.Bold))
        label.setStyleSheet("border: 0px solid white")
        self.sizeBloque = QtW.QTextEdit(self)
        self.sizeBloque.setFrameStyle(1)
        self.sizeBloque.move(280, 160)
        self.sizeBloque.resize(150, 30)
        self.sizeBloque.setFont(QFont("Times", 13))
        # Cantidad de Registros
        label = QtW.QLabel("Cantidad de Registros:", self)
        label.move(11, 220)
        label.setFont(QFont("Times", 13, QFont.Bold))
        label.setStyleSheet("border: 0px solid white")
        self.countRegistrers = QtW.QTextEdit(self)
        self.countRegistrers.setFrameStyle(1)
        self.countRegistrers.move(280, 220)
        self.countRegistrers.resize(150, 30)
        self.countRegistrers.setFont(QFont("Times", 13))
        # Tamaño de Bloques Registro
        label = QtW.QLabel("Tamaño de Registros:", self)
        label.move(11, 280)
        label.setFont(QFont("Times", 13, QFont.Bold))
        label.setStyleSheet("border: 0px solid white")
        self.sizeRegistrer = QtW.QTextEdit(self)
        self.sizeRegistrer.setFrameStyle(1)
        self.sizeRegistrer.move(280, 280)
        self.sizeRegistrer.resize(150, 30)
        self.sizeRegistrer.setFont(QFont("Times", 13))
        # Tamaño de Registros Indice
        label = QtW.QLabel("Tamaño de Registros Indice:", self)
        label.move(11, 340)
        label.setFont(QFont("Times", 13, QFont.Bold))
        label.setStyleSheet("border: 0px solid white")
        self.sizeRegistrerIndex = QtW.QTextEdit(self)
        self.sizeRegistrerIndex.setFrameStyle(1)
        self.sizeRegistrerIndex.move(280, 340)
        self.sizeRegistrerIndex.resize(150, 30)
        self.sizeRegistrerIndex.setFont(QFont("Times", 13))
        # Boton de Crear
        self.bnCreate = QtW.QPushButton("Crear", self)
        self.bnCreate.setGeometry(124, 380, 170, 30)
        self.bnCreate.setStyleSheet("QPushButton{background-color:#0097A7; color: white;}"
                                        "QPushButton::hover{background-color :#006064;}"
                                        "QPushButton::pressed{background-color:#00838F; }")
        self.bnCreate.setFont(QFont("Times", 13, QFont.Bold))
        self.bnCreate.clicked.connect(self.verifyCompleteData)
        # Boton reiniciar
        self.bnReiniciar = QtW.QPushButton("Reiniciar", self)
        self.bnReiniciar.setGeometry(124, 415, 170, 30)
        self.bnReiniciar.setStyleSheet("QPushButton{background-color:#0097A7; color: white;}"
                                        "QPushButton::hover{background-color :#006064;}"
                                        "QPushButton::pressed{background-color:#00838F; }")
        self.bnReiniciar.setFont(QFont("Times", 13, QFont.Bold))
        #self.bnReiniciar.clicked.connect(self.verifyCompleteData)

        # Consola
        self.consola = QtW.QTextEdit(self)
        self.consola.setFrameStyle(1)
        self.consola.move(10, 465)
        self.consola.resize(420, 270)
        self.consola.setReadOnly(True)
        self.consola.setStyleSheet("background-color:#ffffff;")
        self.consola.setFont(QFont("Times", 12))

    def warningError(self, msg: str):
        error = QtW.QMessageBox(self)
        error.setIcon(QtW.QMessageBox.Icon.Warning)
        error.setText(msg)
        error.setStyleSheet("background-color:white; border: 0pc solid white")
        error.setFont(QFont("Times", 13, QFont.Bold))
        error.exec_()

    def registrerConsole(self, msg: str):
        self.consola.setText("\n> " + msg)

    def verifyCompleteData(self):
        Process = "Falta ingresar: "
        count = 0

        CaR = 0
        longR = 0
        longRI = 0
        Bl = 0
        try:
            CaR = int(self.countRegistrers.toPlainText())
            longR = int(self.sizeRegistrer.toPlainText())
            longRI = int(self.sizeRegistrerIndex.toPlainText())
            Bl = int(self.sizeBloque.toPlainText())

            if CaR <= 0 or longR <= 0 or longRI <= 0 or Bl <= 0:
                self.warningError("Los datos no pueden ser menores a 0")
                return
        except:
            self.warningError("No puede ingresar letra o caracteres")
            return
        self.cleanTables()
        self.logica.saveData(CaR, longR, longRI, Bl)
        if self.opcionNivel.currentText() == "Un Nivel":
            self.buildUnNivel(self.logica.UnNivel(self.opcionIndice.currentText()))
        elif self.opcionNivel.currentText() == "Multinivel":
            self.buildMultinivel(self.logica.Multinivel(self.opcionIndice.currentText()))
        self.registrerConsole(self.logica.Process)

    def buildUnNivel(self, ListaDatos):
        L = [ListaDatos[2], ListaDatos[3], ListaDatos[0], ListaDatos[1]]
        self.ListaEstructuras[0].setVisible(True)
        self.ListaEstructuras[1].setVisible(True)
        self.ListaTitulos[0].setVisible(True)
        self.ListaTitulos[1].setVisible(True)
        if ListaDatos[0] != 1:
            self.ListaEstructuras[0].resize(self.w, self.h - 100)

        for i in range(1, -1, -1):
            if i == 0:
                self.ListaTitulos[i].setText("E. Indice Nivel 1")
            else:
                self.ListaTitulos[i].setText("Estructura Principal")
            for j in range(1, (L[i*2]*L[(i*2)+1])):
                U = "Usado"
                if j > self.logica.Registros and i == 0:
                    U = "Sin Usar" 
                elif j > L[1] and i == 1:
                    U = "Sin Usar"
                bloque_actual = j // L[i*2] + 1
                self.ListaEstructuras[i].insertRow(j-1)
                self.ListaEstructuras[i].setItem(j-1, 0, QtW.QTableWidgetItem(str(j)))
                self.ListaEstructuras[i].setItem(j-1, 1, QtW.QTableWidgetItem("B" + str(bloque_actual) + "------ " + U))

    def buildMultinivel(self, ListaDatos: list):
        L = ListaDatos[::-1]
        n = list(L[len(L) - 1])[0]
        limite = 0
        for i in range(len(L) - 1, -1, -1):
            if i == (len(L) - 1):
                self.ListaTitulos[i].setText("Estructura Principal")
            else:
                self.ListaTitulos[i].setText("E. Indice Nivel " + str((len(L) - 1) - i))

            self.ListaEstructuras[i].setVisible(True)
            self.ListaTitulos[i].setVisible(True)
            B = 70 * ((len(L) - 1) - i)
            if n != 1 and i != (len(L) -1):
                self.ListaEstructuras[i].resize(self.w, self.h - B)
            elif n == 1 and i < (len(L) -2):
                self.ListaEstructuras[i].resize(self.w, self.h - B)
            nivel = list(L[i])

            if i == (len(L) - 1) :
                limite = self.logica.Registros
            else: 
                limite = list(L[i + 1])[1]

            for j in range(1, (nivel[0]*nivel[1])):
                U = "Usado"
                if j > limite:
                    U = "Sin Usar"
                bloque_actual = j // nivel[0] + 1
                self.ListaEstructuras[i].insertRow(j-1)
                self.ListaEstructuras[i].setItem(j-1, 0, QtW.QTableWidgetItem(str(j)))
                self.ListaEstructuras[i].setItem(j-1, 1, QtW.QTableWidgetItem("B" + str(bloque_actual) + "------ " + U))

    def cleanTables(self):
        for s in self.ListaEstructuras:
            s.setRowCount(0)
            s.resize(self.w, self.h)
            s.setVisible(False)
        
        for l in self.ListaTitulos:
            l.setVisible(False)