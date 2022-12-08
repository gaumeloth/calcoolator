def somma(num1,num2):
    return float(num1)+float(num2)

def sottrazione(num1,num2):
    return float(num1)-float(num2)

def moltiplicazione(num1,num2):
    return float(num1)*float(num2)

def divisione(num1,num2):
    print("divisione")
    if int(num2)==0:
        return "stai cercando di dividere per 0, l'operazione è impossibile" 
    else:
        return float(num1)/float(num2)

def somma_cumulativa (addendi):
    tot = 0
    i=0
#    print("DEBUG: somma_cumulativa iniziata | tot={} | i={} ".format(tot,i))
    for addendo in addendi:
#        print("DEBUG: for | tot={} | i={} ".format(tot,i))
        tot += float(addendo)
        i+=1
    return tot

def crea_lista_addendi():
    continua=True
    prompt=True
    lista_addendi=[]
    usrinput=0
#   print("DEBUG: continua="+str(continua))
    while continua==True:
#        print("DEBUG: while iniziato continua={}".format(continua))
        usrinput=input("inserire addendo oppure digitare '='e/o premere invio per terminare\n   >>:")
#        print("DEBUG: usrinput="+usrinput+"continua="+str(continua))
#        print("DEBUG: usrinput={usrinput} type usrinput={type(usrinput)} continua={continua}")
        if usrinput=="=" or usrinput=="":
#           print("DEBUG: if '=' | continua="+str(continua))
           continua=False
#           print("DEBUG: if '=' | continua ="+str(continua))
        else:
#           print("DEBUG: elif | continua="+str(continua))
           lista_addendi.append(float(usrinput))
#           continua=False if usrinput=="="els e lista_addendi.append(float(usrinput))
    return lista_addendi
########################################################################################
#
#           /--------------------------------------\
#           |   inserire controllo input utente    |
#           \--------------------------------------/
#
########################################################################################

print("Calcoolator\n")
while True:
    operando=int(input("\nseleziona un operazione\n1)somma\n2)sottrazione\n3)moltiplicazione\n4)divisione\n5)somma cumulativa\n0)esci\n>>:"))
    if operando==1:print(somma(input("inserisci il primo numero:"),input("inserisci il secondo numero:")))
    if operando==2:print(sottrazione(input("inserisci il primo numero:"),input("inserisci il secondo numero:")))
    if operando==3:print(moltiplicazione(input("inserisci il primo numero:"),input("inserisci il secondo numero:")))
    if operando==4:print(divisione(input("inserisci il primo numero:"),input("inserisci il secondo numero:")))
#    if operando==5:print(crea_lista_addendi())
    if operando==5:print(somma_cumulativa(crea_lista_addendi()))
    if operando==0:break

