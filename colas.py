class Cola:
      def __init__(self, tamano):
        self.cola = []
        self.tope = 0
        self.size = tamano

      def push(self,tamaño):
        if self.size > self.tope:
            for x in range (tamaño):
                dato = input('INGRESE UN DATO A LA COLA: ')
                self.cola.append(dato)
                self.tope += 1
        else:
            print('COLA LLENA\n')

      def pop(self):
        if len(self.cola) != 0:
            self.cola.pop(0)
            self.tope -= 1
            print(f'MOSTRANDO COLA NUEVA: {self.cola}\n')
        else:
            print('COLA VACIA\n')

      def longitud(self):
        print(f'LA LONGUITUD DE LA COLA ES: {len(self.cola)}\n')

      def show(self):
        if len(self.cola) != 0:
            print(self.cola)
        else:
            print('COLA VACIA\n')

      def buscar(self):
        if len(self.cola) != 0:
            pos = input('INGRESE EL ELEMENTO PARA RETORNAR UNA POSICION: ')
            if pos in self.cola:
                print(f'POSICION: {self.cola.index(pos)}')
            else:
                print(f'IMPRIMIENDO ELEMENTO DE LA POSICION -1: {self.cola[-1]}\n')
        else:
            print('COLA VACIA\n')