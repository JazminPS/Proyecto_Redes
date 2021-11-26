class Paquete:
    def __init__(self,id_paquete,nodo,grado,ta,t_NodoSink):
        self.id_paquete = id_paquete
        self.nodo = nodo
        self.grado = grado
        self.ta = ta
        self.t_NodoSink = t_NodoSink
        self.latencia_entrega = self.t_NodoSink - self.ta


class Nodo:
    def __init__(self,id_nodo):
        self.id_nodo = id_nodo
        buffer = []


class Grado:
    def __init__(self,id_grado):
        self.id_grado = id_grado