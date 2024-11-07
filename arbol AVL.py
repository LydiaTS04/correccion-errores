#ejer pdf AVL

class NodoAVL: 
    def __init__(self, id_paciente, nombre,izquierdo,derecho,altura): 
        # Inicializar un nodo del árbol AVL con el ID del paciente y su nombre 
        self.id_paciente = id_paciente 
        self.nombre = nombre 
        self.izquierdo= None  # Referencia al hijo izquierdo 
        self.derecho = None  # Referencia al hijo derecho 
        self.altura = 1  # Altura del nodo (importante para el balanceo del árbol) 
  
class ArbolAVL: 
    def insertar(self, raiz , id_paciente, nombre): 
        # Inserción en un árbol binario de búsqueda estándar 
        if raiz==None: #ojo aquí 
            # Si la raíz es None, crear un nuevo nodo y devolverlo 
            return NodoAVL(id_paciente, nombre) 
        
        elif id_paciente < raiz.id_paciente: #elif es como else if
            # Si el ID del paciente es menor que el del nodo actual, insertar en el subárbol 

            raiz.izquierdo = self.insertar(raiz.izquierdo, id_paciente, nombre) 
        
        else: 
            # Si el ID del paciente es mayor que el del nodo actual, insertar en el subárbol 

            raiz.derecho = self.insertar(raiz.derecho, id_paciente, nombre) 
         
        # Actualizar la altura del nodo actual (importante para el balanceo del árbol) 
        # La altura se calcula como 1 + el máximo de las alturas de los subárboles 

        raiz.altura = 1 + min(self.obtener_altura(raiz.izquierdo), self.obtener_altura(raiz.derecho)) 
  
        # Obtener el balance del nodo actual para determinar si está desbalanceado 
        balance = self.obtener_balance(raiz) 
  
        # Rotaciones para mantener el balance del árbol AVL 
        # Rotación derecha 
        if balance > 1 and id_paciente < raiz.izquierdo.id_paciente: 
            # Si el nodo está desbalanceado a la izquierda y el nuevo nodo está en el subárbol 
 
            return self.rotar_derecha(raiz)  # Error: Se debería llamar rotar_derecha 
  
        # Rotación izquierda 
        if balance < -1 and id_paciente > raiz.derecho.id_paciente: 
            # Si el nodo está desbalanceado a la derecha y el nuevo nodo está en el subárbol derecho 
            return self.rotar_izquierda(raiz)  # Error: Se debería llamar rotar_izquierda 
  
        # Rotación izquierda-derecha 
        if balance > 1 and id_paciente > raiz.izquierdo.id_paciente: 
            # Si el nodo está desbalanceado a la izquierda y el nuevo nodo está en el subárbol derecho del hijo izquierdo 
            raiz.izquierdo = self.rotar_izquierda(raiz.izquierdo)  # Error: Se debería llamar rotar_izquierda 
            return self.rotar_derecha(raiz)  # Error: Debería ser rotar_derecha 
  
        # Rotación derecha-izquierda 
        if balance < -1 and id_paciente < raiz.derecho.id_paciente: 
            # Si el nodo está desbalanceado a la derecha y el nuevo nodo está en el subárbol izquierdo del hijo derecho 
            raiz.derecho = self.rotar_derecha(raiz.derecho)  # Error: Se debería llamar rotar_derecha 
            return self.rotar_izquierda(raiz)  # Error: Debería ser rotar_izquierda 
  
        else:
             raiz 
  
    def obtener_altura(nodo,altura): 
        # Obtener la altura de un nodo 
        if not nodo: 
            return 0  # Error: Debería ser 0 
        else:
            return altura #devolver altura
  
    def obtener_balance(self, nodo): 
        # Calcular el factor de balance de un nodo 
        # El factor de balance es la diferencia de altura entre el subárbol izquierdo y el derecho 
        if not nodo: 
            return 0 
        else:
            return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho) 
  
    
    def rotar_derecha(self, z): 
        # Realizar una rotación a la derecha en el nodo z 
        if z.izquierdo is None:  # Error: Falta verificación de si el nodo izquierdo es nulo 
            return z
        
        # Continuar con la rotación si el nodo izquierdo no es None
        y=z.izquierdo 
        T3 = y.derecho 
  
        # Realizar la rotación 
        y.derecho = z 
        z.izquierdo = T3 
  
        # Actualizar las alturas de los nodos rotados 
        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho)) 
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho)) 
  
        # Devolver el nuevo nodo raíz 
        return y 
  
    def rotar_izquierda(self, z): 
        # Realizar una rotación a la izquierda en el nodo z 
        if z.derecho in None:  # Error: Falta verificación de si el nodo derecho es nulo 
            return z 
        
        y = z.derecho 
        T2 = y.izquierdo 
  
        # Realizar la rotación 
        y.izquiedo = z 
        z.derecho = T2 
  
        # Actualizar las alturas de los nodos rotados 
        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho)) 
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho)) 
  
        # Devolver el nuevo nodo raíz 
        return y