class Grado:
    def __init__(self,id_grado):
        self.id_grado = id_grado

    #getters y setters
    def set_id_grado(self,id_grado):
        self.id_grado = id_grado
    

    def get_id_grado(self):
        return self.id_grado


class Nodo:
    def __init__(self,id_nodo):
        self.id_nodo = id_nodo
        buffer = []

    #getters y setters
    def set_id_nodo(self,id_nodo):
        self.id_nodo = id_nodo
    

    def get_id_nodo(self):
        return self.id_nodo


class Paquete:
    def __init__(self,id_paquete,nodo,grado,ta,t_NodoSink):
        self.id_paquete = id_paquete
        self.nodo = nodo
        self.grado = grado
        self.ta = ta
        self.t_NodoSink = t_NodoSink
        self.latencia_entrega = self.t_NodoSink - self.ta

    #getters y setters
    def set_id_paquete(self,id_paquete):
        self.id_paquete = id_paquete
    

    def get_id_paquete(self):
        return self.id_paquete

    
    def set_nodo(self,nodo):
        self.nodo = nodo
    

    def get_nodo(self):
        return self.nodo
    

    def set_grado(self,grado):
        self.grado = grado
    

    def get_grado(self):
        return self.grado

    
    def set_ta(self,ta):
        self.ta = ta
    

    def get_ta(self):
        return self.ta

    
    def set_tNodoSink(self,t_NodoSink):
        self.t_NodoSink = t_NodoSink
    

    def get_tNodoSink(self):
        return self.t_NodoSink


    def get_latenciaEntrega(self):
        return self.latencia_entrega