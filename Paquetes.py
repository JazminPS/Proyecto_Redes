class Grado:
    def __init__(self,id_grado,N):
        self.id_grado = id_grado
        self.nodo = []

    #getters y setters
    def set_id_grado(self,id_grado):
        self.id_grado = id_grado
    

    def get_id_grado(self):
        return self.id_grado
    

    def set_N(self,N):
        self.N = N

    
    def get_N(self):
        return self.N
    

class Nodo:
    def __init__(self,id_nodo,grado):
        self.id_nodo = id_nodo
        self.buffer = [None] * 15

    #getters y setters
    def set_id_nodo(self,id_nodo):
        self.id_nodo = id_nodo
    

    def get_id_nodo(self):
        return self.id_nodo
    

    def set_grado(self,grado):
        self.grado = grado
    

    def get_grado(self):
        return self.grado


class Paquete:
    def __init__(self,id_paquete,nodo,ta,t_NodoSink):
        self.id_paquete = id_paquete
        self.nodo = nodo
        self.grado = grado
        self.ta = ta
        self.t_NodoSink = t_NodoSink
        
        if t_NodoSink != 0:
            self.retardoSourceToEnd = self.t_NodoSink - self.ta

    #getters y setters
    def set_id_paquete(self,id_paquete):
        self.id_paquete = id_paquete
    

    def get_id_paquete(self):
        return self.id_paquete

    
    def set_nodo(self,nodo):
        self.nodo = nodo
    

    def get_nodo(self):
        return self.nodo

    
    def set_ta(self,ta):
        self.ta = ta
    

    def get_ta(self):
        return self.ta

    
    def set_tNodoSink(self,t_NodoSink):
        self.t_NodoSink = t_NodoSink
    

    def get_tNodoSink(self):
        return self.t_NodoSink


    def get_latenciaEntrega(self):
        return self.retardoSourceToEnd