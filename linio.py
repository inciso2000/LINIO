class Carrito():
    def __init__(self, ID_carrito, usuario, productos_carrito, cantidad):
        self.ID_carrito = ID_carrito
        self.usuario = usuario
        self.cantidad = cantidad
        
    def get_ID_carrito (self):
        return self.ID_carrito
    def set_ID_carrito(self, ID_carrito):
        self.ID_carrito = ID_carrito

    def get_usuario(self):
        return self.usuario
    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_productos_carrito(self):
        return self.get_productos_carrito
    def get_productos_carrito(self, productos_carrito):
        self.productos_carrito = productos_carrito

    def get_cantidad(self):
        return cantidad
    def set_cantidad(self,cantidad):
        self.cantidad = cantidad


class Categoria():
    def __init__(self, ID_categoria, nombre, descripcion, lista_producto):
        self.ID_categoria = ID_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.lista_producto = lista_producto

    def get_ID_categoria(self):
        return self.ID_categoria
    def set_ID_categoria(self, ID_categoria):
        self.id_categoria = ID_categoria
    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_lista_producto(self):
        return self.lista_producto
    def set_lista_producto(self, lista_producto):
        self.lista_producto = lista_producto
        

class Pedido():
    def __init__(self, ID_pedido, fecha_pedido, carrito, repartidor, pago):
        self.ID_pedido = ID_pedido
        self.fecha_pedido = fecha_pedido
        self.carrito = carrito       
        self.repartidor = repartidor
        self.pago = pago

    def get_ID_pedido(self):
        return self.ID_pedido
    def set_ID_categoria(self, ID_categoria):
        self.ID_pedido = ID_pedido

    def get_fecha_pedido(self):
        return self.fecha_pedido
    def set_fecha_pedido(self, fecha):
        self.fecha_pedido = fecha_pedido
    
    def get_carrito(self):
        return self.ID_pedido
    def set_carrito(self, carrito):
        self.carrito = carrito
    
    def get_pago(self):
        return self.pago
    def set_ago(self, pago):
        self.pago = pago


class Repartidor():
    def __init__(self, ID_repartidor, nombre_repartidor, placa):
        self.ID_repartidor = ID_repartidor
        self.nombre_repartidor = nombre_repartidor
        self.placa = placa
        
    def get_ID_repartidor(self):
        return self.ID_repartidor
    def set_ID_repartidor(self):
        self.ID_repartidor = ID_repartidor

    def get_nombre_repartidor(self):
        return self.nombre_repartidor
    def set_nombre_repartidor(self, nombre_repartidor):
        self.nombre_repartidor = nombre_repartidor

    def get_placa(self):
        return self.placa
    def set_placa(self, placa):
        self.placa = placa


class Persona():
    def __init__(self, persona_nombre, persona_dni, edad):
        self.persona_nombre = persona_nombre
        self.persona_dni = persona_dni
        self.edad = edad

    def get_persona_nombre(self):
        return self.persona_nombre
    def set_persona_nombre(self, persona_nombre):
        self.persona_nombre
    
    def get_persona_dni(self):
        return self.persona_nombre
    def set_persona_dni(self, persona_dni):
        self.persona_dni = persona_dni
    
    def get_edad(self):
        return self.edad
    def set_edad(self, edad):
        self.edad = edad


class Usuario(Persona):
    def __init__(self, username, contraseña, correo, telefono, direccion):
        Persona.username = username
        Persona.contraseña = contraseña
        Persona.correo = correo
        Persona.telefono = telefono
        Persona.direccion = direccion 
        
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    
    def get_contraseña(self):
        return self.contraseña
    def set_contraseña(self, contraseña):
        self.contraseña = contraseña
             
    def get_correo(self):
        return self.correo
    def set_correo(self):
        self.correo = correo 

    def set_telefono(self):
        return self.telefono
    def get_telefono(self, telefono):
        self.telefono = telefono


class Comercio():
    def __init__(self, ID_comercio, nombre, email, direccion, distrito):
        self.ID_comercio = ID_comercio
        self.nombre = nombre 
        self.email = email
        self.direccion = direccion
        self.distrito = distrito

    def get_ID_comercio(self):
        return self.ID_comercio
    def set_ID_comercio(self, ID_comercio):
        self.ID_comercio = ID_comercio
    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_emai(self):
        return self.email
    def set_email(self, email):
        self.email = email
    
    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def get_distrito(self):
        return self.distrito
    def set_distrito(self, distrito):
        self.distrito = distrito


class Pago():
    def __init__(self, ID_pago, metodo_pago ):
        self.ID_pago = ID_pago
        self.metodo_pago = metodo_pago

    def get_ID_pago(self):
        return self.ID_pago
    def set_ID_pago(self, ID_pago):
        self.ID_pago = ID_pago
    
    def get_metodo_pago(self):
        return self.metodo_pago
    def set_metodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago



