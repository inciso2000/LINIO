class Carrito():
    def __init__(self, ID_carrito, cantidad, sub_total):
        self.ID_carrito = ID_carrito
        self.cantidad = cantidad
        self.sub_total = sub_total

    def get_ID_carrito (self):
        return self.ID_carrito
    def set_ID_carrito(self, ID_carrito):
        self.ID_carrito = ID_carrito

    def get_cantidad(self):
        return cantidad
    def set_cantidad(self,cantidad):
        self.cantidad = cantidad


class Categoria():
    def __init__(self, ID_categoria, nombre, descripcion):
        self.ID_categoria = ID_categoria
        self.nombre = nombre
        self.descripcion = descripcion

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
        

class Pedido():
    def __init__(self, ID_pedido, fecha, ID_cliente, ID_comercio, estado, ID_envio, ID_pago):
        self.ID_pedido = ID_pedido
        self.fecha = fecha
        self.ID_cliente = ID_cliente
        self.ID_comercio = ID_comercio
        self.estado = estado
        self.ID_envio = ID_envio
        self.ID_pago = ID_pago

    def get_ID_pedido(self):
        return self.ID_pedido
    def set_ID_categoria(self, ID_categoria):
        self.ID_pedido = ID_pedido

    def get_fecha(self):
        return self.fecha
    def set_fecha(self, fecha):
        self.fecha = fecha
    
    def get_ID_cliente(self):
        return self.ID_pedido
    def set_ID_cliente(self, ID_cliente):
        self.ID_cliente = ID_cliente

    def get_ID_comercio(self):
        return self.ID_comercio
    def set_ID_comercio(self):
        self.ID_comercio = ID_comercio

    def get_estado(self):
        return self.estado
    def set_estado(self):
        self.estado = estado

    def get_ID_pedido(self):
        return self.ID_pedido
    def set_ID_pedido(self):
        self.ID_pedido = ID_pedido
    
    def get_ID_pago(self):
        return self.ID_pago
    def set_ID_pago(self):
        self.ID_pago = ID_pago


        
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

class Usuario():
    def __init__(self, username, contraseña, cod_confirmacion, nombre_usuario, apellido_usuario, correo, num_telefonico, fecha_nac):
        self.username = username
        self.contraseña = contraseña
        self.cod_confirmacion = cod_confirmacion
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.correo = correo
        self.num_telefonico = num_telefonico
        self.fecha_nac = fecha_nac