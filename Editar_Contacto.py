# función para editar los datos de un contacto
def editar(self):
		print("---------------")
		print("Editar contacto")
		print("---------------")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			option=int(input("Introduzca la opción deseada: "))
			if option==1:
				nom=input("Introduzca el nuevo nombre: ")
				self.contactos[data]['nombre']=nom
			elif option==2:
				telf=input("Introduzca el nuevo teléfono: ")
				self.contactos[data]['telf']=telf
			elif option==3:
				email=input("Introduzca el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True


# bloque principal
agenda=Agenda()
agenda.menu()