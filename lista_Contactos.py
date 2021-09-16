# función para imprimir la lista de contactos
	# En este caso imprimiremos solo los nombres de los contactos
	# con ellos podremos buscar luego un contacto
def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.contactos) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])