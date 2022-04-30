import os
import mysql.connector
#Esta funcion es solo el menu que define las alcaldias
def mostrarAlcaldias():
    print("escribe el numero:")
    print("1.Alvaro Obregon 2.Azcapotzalco 3.Benito Juarez 4.Coyoacan")
    print("5.Cuajimalpa de Morelos 6.Cuauhtemoc 7.Gustavo A. Madero 8.Iztacalco")
    print("9.Iztapalapa 10.La Magdalena Contreras 11.Miguel Hidalgo 12.Milpa Alta")
    print("13.Tlahuac 14.Tlalpan 15.Venustiano Carranza 16.Xochimilco")
    condado=input()
    return condado
#consulta general a la base de datos
#query recibe la consulta y title coloca el titulo de la tabla
def mostrarDB(query,title):
    #se definen las credenciales
    mydb = mysql.connector.connect(
      host="mydb",
      user="cabin",
      password="cabinpw",
      database="cdMexico"
    )
    #se define el cursor para la base de datos
    mycursor = mydb.cursor()
    #se ejecuta el query
    mycursor.execute(query)
    #se llena un arreglo con la solucion y se imprime
    myresult = mycursor.fetchall()
    print(title)
    for x in myresult:
      print(x)
    #cerramos la base de datos
    mydb.close()
#generamos un menu general de las opciones
#se mostrara siempre que no se de la opcion 'q'
while True:
    print("Escribe la opcion a ver del metrobus de la ciudad de Mexico:")
    print("a.Lista de unidades Disponibles:")
    print("b.Consultar la ubicación de una unidad dado su ID")
    print("c.Lista de alcaldias Disponibles")
    print("d.Lista de unidades dentro de la alcaldia")
    print("Escribe q para salir")
    seleccion=input()
    if seleccion=="a":
        #se muestran todas la s unidades Disponibles
        texto1="select vehicle_id,vehicle_label,position_latitude,position_longitude from metro where trip_start_date=0"
        titulo1="unidad_id,Etiqueta,Latitud,Longitud"
        mostrarDB(texto1,titulo1)
    elif seleccion=="b":
        #se busca el id de la alcaldia
        print("Escriba id")
        texto2a=input()
        texto2="select vehicle_id,position_latitude,position_longitude from metro where id='"+texto2a+"'"
        titulo2="unidad_id,Latitud,Longitud"
        mostrarDB(texto2,titulo2)
    elif seleccion=="c":
        #se muestran todas las alcaldias
        texto3="select * from alcaldias"
        titulo3="id Alcaldia, Nombre de Alcaldia"
        mostrarDB(texto3,titulo3)
    elif seleccion=="d":
        #se busca el dato de la alcaldia a buscar en la siguiente funcion
        condado2=mostrarAlcaldias()
        texto4="SELECT metro.vehicle_label, metro.position_latitude,metro.position_longitude,alcaldias.alcaldia FROM metro INNER JOIN alcaldias ON metro.county = alcaldias.idAlcaldia and alcaldias.idAlcaldia='"+condado2+"'"
        titulo4="Etiqueta,Latitud,Longitud,Alcaldia"
        mostrarDB(texto4,titulo4)
    if seleccion == "q":
        break
#fin de la ejecucion
print("fin de ejecucion")
