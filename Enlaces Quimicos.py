#Para poder ejecutar correctamente el codigo debera utilizar:(Python 2.7).
import pandas as pd

def readElementos():
    return raw_input("ingrese formula\n")

def createQuery(elementos):
    preQuery = []
    for elemento in elementos:
        q = 's == "{}"'.format(elemento.upper())
        preQuery.append(q)
    return ' or '.join(preQuery)

def readData(fileName, query):
    data = pd.read_excel(fileName, sheet_name='Hoja1')
    total =  data.query(query).sum()
    return total['pA']
#Si desea seguir realizando sumas de los elementos quimicos deberea indicar "y", de no ser asi, debera indicar "n".
def total():
    total = readData('periodic.xlsx', createQuery(readElementos().split('+')))
    return total

run = ('y')
while run == ('y'):
    print 'total = ', total()
    if ('total > 1.67:'):
        print ("Enlace Covalente Polar")
    else:
        print ("Enlace ionico")
run = raw_input("Decea continuar con otra suma y/n\n")
#Si indica "y" podra seguir realizando sumas, sino, no podra seguir realizando sumas.
 
