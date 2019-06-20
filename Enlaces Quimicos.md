Alejandro Ramirez Serratos,   
    correo electronico: aserratos0809@gmail.com 
    
Mario Humberto González Dimas,  
    correo electronico: mgonzalez26@ucol.mx

Juan David Hernandez Hernandez,  
    correo electronico: jhernandez14@ucol.mx

Campus Coquimatlán, 284000

# Enlaces-Qumicos

Realización de la suma de electronegatividad de los elementos químicos y indicar si es enlace Ionico o Covalente polar 

# Resumen   

Se presenta la elaboración de un pro-grama en Python para el cálculo de  la electronegatividad de los elementos químicos, facilitando el nombramiento y conocimiento del tipo de enlace que se forma al combinar ciertos elementos de la tabla periódica. Enlaces como: Iónico, Covalente Polar y Covalente puro.

Los datos de la tabla serán tomados de una hoja de cálculo de Excel.  

Palabras clave: Enlaces Químicos, Ió-nico, Covalente Polar, Covalente puro y Electronegatividad

# Abstract 

The development of a program in Py-thon is presented for the calculation of the electronegativity of the chemical elements, facilitating the appointment and knowledge of the type of link that is formed when combining certain ele-ments of the periodic table. Links such as: Ionic, Polar Covalent and pure Co-valent.

The data in the table will be taken from an Excel spreadsheet.

Keywords: Chemical bonds, Ionic, Po-lar Covalent, Pure Covalent and Elec-tronegativity.

# Introducción

La química es la ciencia que se encar-ga de estudiar el comportamiento de la materia como: su composición y cada una de sus propiedades, incluyendo los cambios que experimenta al entrar en contacto con otras sustancias.

Este proyecto está ideado para crear una aplicación capaz solucionar pe-queños problemas en este campo de estudio, dando pues la respuesta al nombre de los tipos de enlaces vistos en clase.

Los datos necesarios se encuentran en una hoja de cálculo con todos los ele-mentos de la tabla periódica y el núme-ro de electrones de valencia de cada elemento.

En Python podemos llamar el archivo de Excel a través de librerías, la aplica-ción está ideada para que el usuario elija a su gusto los elementos de la hoja de cálculo en Python, mientras que Python realiza la resta de los electrones de valencia de tal modo que si dicha resta nos arroja un resultado igual a 0 el enlace dirá Covalente Puro, si el resul-tado es mayor a 0 pero menor a 2; el enlace dirá Iónico y si el resultado es igual o mayor a 2 el enlace dirá Co-valente Polar.

Cabe mencionar que en esta suma siempre se elige primero cuál de los dos elementos seleccionados tiene mayor cantidad de electrones de valencia para que nuestro resultado siempre nos dé un número mayor o igual a 0. Después Python se encargará de hacer lo men-cionado en el párrafo anterior.

# Desarrollo

Para utilizar este programa se tiene que usar un paquete de Python que propor-ciona estructuras de datos similares a los dataframes de R. el cual es pandas, depende de Numpy, la librería añade un potente tipo matricial.

1.- Se tiene que importar el programa para poder usarlo, ya que al importarlo se incorpora una aplicación objetos, documentos u otro tipo de archivos lo cual en este caso se tomaran datos de Excel.

2.- Para poder leer el programa se ocu-pa tener el archivo guardado en csv el cual los objetos de pandas permiten tanto leer datos en diversos formatos (read_csv, read_excel, read_json, read_html, read_pickle….) como escribir en ellos (to_csv, to_excel, to_json, to_html, to_pickle….). Permite incluso leer y escribir en el portapapeles (read_clipboard, to_clipboard)
Sep: el delimitador que divide los cam-pos del csv

3.- Se imprimen los datos correspon-dientes para poder correr el programa

4.- Se especifica lo que se tiene que imprimir al llamar la columna o fila es-cogida.

5.- Para poder utilizar la entrada se ocupa que sea entero, entonces puede convertirse exitosamente a int y pode-mos decir que la entrada ingresada es un número, así que input permite obte-ner texto escrito por teclado.

6.- se denomina la formula a seguir pa-ra tener tu calculo correcto 

7.- Para la estructura del programa se ocupa if, el cual os permite que el pro-grama ejecute unas instrucciones cuando se cumplan una condición.

8.- Se pone el rango correspondiente para tener la lectura correspondiente de los valores en el rango 

9.- Se imprime la suma adecuada para poder tener el resultado correcto y así obtener los diferentes enlaces químicos

10-. Se pone los elementos que quieras calcular y así lo repites las veces que quieras que te salga el enlace químico corres-pondiente del programa.

# Manejo de Datos

El manejo de datos de este programa el cual tiene que ver con la química “enla-ces químicos” con el que se obtendrán los diferentes sus enlaces correspon-dientes ya sea iónico o covalente, cova-lente polar, mediante Python 2.7 ya que se nos acomodaba mas con la maquina que estamos usándola la cual tiene unas características con Windows 10, el cual cuenta con un sistema operativo de 64 bits.

Para que nuestro programa pueda fun-cionar se ocupó la librería panda, la cual como el archivo a importar es en Excel se ocupara la librería xlrd para leer los datos directamente de Excel.

Para leer los elementos se maneja co-mo readElementos, por ellos es funda-mental tener en claro.
Los comandos utilizados por pandas son para llamar las columnas de el ar-chivo en Excel, créate.querry, ya que así se podrá importar solo la columna que llamamos.

Read.data es idispensable para llevar a cabo la impotancion correcta y teniendo las condiciones dichas en el programa se tendrá el resultado a esperar.

# Codigo (Python 2.7)

Para poder ejecutar correctamente el codigo debera utilizar: (Python 2.7).

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
    
Si desea seguir realizando sumas de los elementos quimicos deberea indicar "y", de no ser asi, debera indicar "n".

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

Si indica "y" podra seguir realizando sumas, sino, no podra seguir realizando sumas.
 
# Conclusión

Mario Gonzalez:

En este proyecto se vio como de buena manera se podría facili-tar las cosas en la química pa-ra ello es fundamental tener en nuestro entorno se tendrá que utilizar la química en to-dos lados y teniendo en cuen-ta este programa, con mayor facilidad ya que importando datos se tendrá de manera co-rrecta el resultado esperado. Sobre todo, que la tecnología la metemos a nuestro alcance y es lo 
que los conlleva a tener más fáci-les las cosas.


Alejando Serratos:

Mediante la realización del pro-yecto logramos realizar un có-digo mediante el desarrollo de un programa para poder reali-zar la suma de diferentes ele-mentos químicos mediante su electronegatividad y con esto poder definir si la suma de es-tos elementos químicos es un enlace Iónico o un Enlace Covalente polar.
Este código fue desarrollado con el fin de poder facilitar la suma de estos elementos químicos y poder identificar el tipo de en-lace y con esto poder satisfa-cer la necesidad de facilitar el trabajo de la realización su-mas mediante la electronega-tividad de los elementos quí-micos


David Hernández:

Este proyecto nos ayudó a solucionar una problemática planteada, como ma-teria, la programación tiene una amplia variedad de aplicaciones a soluciones. Es necesario tener un conocimiento del problema para saber que se querrá co-mo resultado de dicha aplicación.

Lo que hoy en día tenemos a nuestro alcance se puede tomar en un entorno muy a favor de nosotros ya que con es-ta revolución tecnología tenemos a nuestros alcance muchas mas facilida-des para poder explorar todo lo que queremos respecto a el estudio, tener un programa el cual te pueda calcular de buena manera los diferentes enla-ces Químicos  que se pueden calcular mediante la electronegatividad, se toma en cuenta en la química como algo in-dispensable que se tiene que tener de  conocimiento básico,  y con la ayuda de este tipos de programas de facilitaran  para un mayor aprendizaje esperado de cada uno de nosotros los estudiantes.

# Referencias 

Tabla periodica de electronegativadad de Pauling
