class Producto():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
class Medicamento(Producto):
    def __init__(self,nombre, cantidad, precio, composicion, porcentaje):
        super().__init__(nombre, cantidad, precio)   #Llama a Producto para que se construya y poder usarlo más tarde
        self.composicion = composicion
        self.porcentaje = porcentaje
class Laboratorio():
    def __init__(self, laboratorio, Producto1, Producto2):
        self.laboratorio = laboratorio
        self.producto1 = Producto1
        self.producto2 = Producto2

tiritas = Producto("Tiritas", 3, 4)

naprox = Medicamento("Naproxeno", 5, 2.75, "Ácido propiónico", 0.25)

vir = Laboratorio("Vir", naprox, tiritas)

print(vir.producto1.nombre)
print(vir.producto2.nombre)
print("El laboratorio", vir.laboratorio, "tiene", vir.producto1.nombre ,", ", vir.producto2.nombre)
print("La composición de", vir.producto1.nombre,"es", vir.producto1.composicion)
