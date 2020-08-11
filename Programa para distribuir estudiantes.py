import random
##########################################

lgrupos=[]
lnombres=[]   #listas
ltemas=[]

#########################################

#path1, path2, path3 = input("Introduzca el directorio de grupos, nombres y temas: ").split()  #//asigna el string de cada ruta a una variable diferente
#grupos = open(path1,"r");
#nombres = open(path2,"r");      # abre el documento con el paramentro de lectura "r" read
#temas = open(path3,"r");

grupos = open("D:\\grupos.txt","r");          #//rutas definidas anteriormente
nombres = open("D:\\nombres.txt","r");
temas = open("D:\\temas.txt","r");

#########################################

for x in grupos: 
 lgrupos.append(x)
 pass

for x in nombres:                          #for each para guardar cada linea del documento en una lista
 lnombres.append(x)
 pass

for x in temas: 
 ltemas.append(x)
 pass

#########################################

integrantes1 = int(len(lnombres)/len(lgrupos))
integrantes2 = integrantes1+1                                                                #algoritmo para determinar el numero de grupos y de integrantes
sector2 = int(len(lnombres)-(len(lgrupos)*integrantes1))
sector1 = int((len(lnombres)-(sector2*integrantes2))/integrantes1)
###########################################

for i in range(sector1):
     showgrupo = random.choice(lgrupos)             #muestra un grupo aleatorio
     print (showgrupo)
     lgrupos.remove(showgrupo)                      #lo elimina de la lista para que no se repita en la siguiente iteracion
     showtema = random.choice(ltemas)
     print ("Tema: " + showtema)                    #muestra un tema aleatorio
     ltemas.remove(showtema)                        #lo elimina de la lista para que no se repita en la siguiente iteracion
     for i in range(integrantes1):
         showintegrante = random.choice(lnombres)
         print ("Integrante #{}".format(i+1) + ": " + showintegrante)      #la misma logica con los nombres
         lnombres.remove(showintegrante)
         pass
     pass

###########################################


for i in range(sector2):
    showgrupo = random.choice(lgrupos)
    print (showgrupo)                                         #este es el mismo programa que el anterior solo que este tiene cantidades de grupos con diferente numero de integrantes
    lgrupos.remove(showgrupo)
    showtema = random.choice(ltemas)
    print ("Tema: " + showtema)
    ltemas.remove(showtema)
    for i in range(integrantes2):
         showintegrante = random.choice(lnombres)
         print ("Integrante #{}".format(i+1) + ": " + showintegrante)
         lnombres.remove(showintegrante)
         pass
    pass
########################################