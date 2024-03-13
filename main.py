bandas=[]
#Contruyendo la interfaz 
print("***ALTAVOZ ES TU VOZ***")
print("***********************")
opcion=100
while(opcion!=5):
    print("1. Registrar Banda")
    print("2. Buscar Informacion De Una Banda")
    print("3. Agenda Del Evento")
    print("4. RModificar Una Banda")
    print("5. SALIR")
    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #Creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["Nombre"]=input("Nombre de la banda: ")
        banda["Genero"]=input("Genero:")
        banda["Clasificacion"]=input("Clasificacion: ")
        banda["Tiempo"]=int(input("Tiempo: "))
        banda["Costo"]=int(input("$"))
        
        #Agregando un diccionario a una lista 
        bandas.append(banda)

    elif opcion==2:
        bandaBuscada=input("Digita el nombre de la banda que estas buscando:")
        for bandAuxiliar in bandas:
            if bandAuxiliar["Nombre"]==bandaBuscada:
                #Como lo encontre muestro os datos de la banda auxiliar
                print(f"id:{bandAuxiliar["id"]}--- Nombre:{bandAuxiliar["Nombre"]}")
            else:
                print("Sigue buscando")
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass