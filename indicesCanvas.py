import math

class LogicIndexs():
    def __init__(self):
        self.Registros = 0
        self.CapacidadBloques = 0
        self.LongRegistrosIndices = 0
        self.LongRegistros = 0

        self.Process = ""
    
    def reiniciar(self):
        self.Registros = 0
        self.CapacidadBloques = 0
        self.LongRegistrosIndices = 0
        self.LongRegistros = 0

    def saveData(self, CR, longR, longRI, B):
        self.Registros = CR
        self.LongRegistros = longR
        self.LongRegistrosIndices = longRI
        self.CapacidadBloques = B

    def UnNivel(self, Tipo: str) -> list:
        self.Process = ""
        lista = []
        if Tipo == "Primario":
            RxB = 1 if math.trunc(self.CapacidadBloques / self.LongRegistros) == 0 else math.trunc(self.CapacidadBloques / self.LongRegistros)
            NB = math.ceil(self.Registros / RxB)
            RIxB = 1 if math.trunc(self.CapacidadBloques / self.LongRegistrosIndices) == 0 else math.trunc(self.CapacidadBloques / self.LongRegistrosIndices)
            BRI = math.ceil(NB / RIxB)
            lista.append(RxB)
            lista.append(NB)
            lista.append(RIxB)
            lista.append(BRI)
            n = math.ceil(math.log(NB, BRI))
            self.Process = "Niveles = " + str(n) + "\nNumero de Accesos = " + str(n + 1) + "\n"
            self.Process = self.Process + "---E. Principal\nRegistros por Bloque: " + str(RxB) + "\nNumero de Bloques: " + str(NB) + "\n"
            self.Process = self.Process + "---E. Indice Nivel 1\nRegistros Indice por Bloque: " + str(RIxB) + "\nNumero de Bloques de Registros Indice: " + str(BRI) + "\n"
        if Tipo == "Secundario":
            RIxB = 1 if math.trunc(self.CapacidadBloques / self.LongRegistrosIndices) == 0 else math.trunc(self.CapacidadBloques / self.LongRegistrosIndices)
            BRI = math.ceil(self.Registros / RIxB)
            lista.append(1)
            lista.append(self.Registros)
            lista.append(RIxB)
            lista.append(BRI)
            n = math.ceil(math.log(self.Registros, BRI))
            self.Process = "Niveles = " + str(n) + "\nNumero de Accesos = " + str(n + 1) + "\n"
            self.Process = self.Process + "---E. Principal\nNumero de Registros Indice: " + str(self.Registros) + "\n"
            self.Process = self.Process + "---E. Indice Nivel 1\nRegistros Indice por Bloque: " + str(RIxB) + "\nNumero de Bloques de Registros Indice: " + str(BRI) + "\n"
        return lista
    
    def Multinivel(self, Tipo: str):
        l = self.UnNivel(Tipo)
        return self.calcularMultinivel([l[2], l[3]], 1, [[l[0], l[1]]])

    def calcularMultinivel(self, ListaUse, c, returnList):
        returnList.append(ListaUse)
        x = list(returnList[c])
        BRI = math.ceil(x[1] / x[0])
        if c != 1:
            self.Process = self.Process + "---E. Indice Nivel "+str(c-1)+"\nRegistros Indice por Bloque: " + str(x[0]) + "\nNumero de Bloques de Registros Indice: " + str(x[1]) + "\n"
        if BRI == 1:
            if x[1] != 1:
                self.Process = self.Process + "---E. Indice Nivel "+str(c+1)+"\nRegistros Indice por Bloque: " + str(ListaUse[0]) + "\nNumero de Bloques de Registros Indice: " + str(BRI) + "\n"
                returnList.append([ListaUse[0], BRI])
            return returnList
        else:
            self.calcularMultinivel([ListaUse[0], BRI], c + 1, returnList)