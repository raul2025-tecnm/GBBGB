class SistemadePedidos:
    def __init__(self):
        pass
    def nombre(self):
        self.crearPedido=(input("Ingrese el nombre del pedido:"))
        return(self.crearPedido)
    def agregarPedido(self):
        print("selecciona:")
        print("1. agua")
        print("2. refresco")
        print("3. papas")
        self.opcion=int(input("digita el numero:"))
        return (self.opcion)
    def lista(self):
        if self.opcion==1:
            self.AgregarPedido=("agua")
        elif self.opcion==2:
            self.AgregarPedido=("refresco")
        else:
            self.AgregarPedido=("papas")
    def mostrarpedido(self):
        print(f"\n la opcion que eligio fue:",self.crearPedido," y el producto que agregaste fue:",self.AgregarPedido)
        
obj=SistemadePedidos()
a=obj.nombre()
a=obj.agregarPedido()
a=obj.lista()
a=obj.mostrarpedido()
    