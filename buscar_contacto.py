# función para buscar un contacto a través del nombre
def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nom=input("Introduzca el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telf'])
				print("E-mail: ",self.contactos[x]['email'])
				return x