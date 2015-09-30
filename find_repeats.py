#!/usr/bin/env python

import os, re
import time, csv

#Directorio actual donde se encuentra nuestro script
actual_dir = os.path.dirname(os.path.realpath(__file__))
compare = raw_input("### Introduzca el nombre del fichero a comparar con el resto (type 'exit' to exit): ")
if compare != "exit":

    #BUSCAMOS TODOS LOS CSVs QUE HAY EN EL DIRECTORIO
    exp_csv = re.compile("^([\S\W]+)\.csv$")
    for d, s, files in os.walk(actual_dir):
        files = [f for f in files if exp_csv.match(f) ]

    if compare in files:
        compare_file = files.remove(compare)
        print "### Se encontro el fichero a comparar"
        for f in files:
            print " - "+f
        if raw_input("### Comparar todos los ficheros y generar archivos?(Type 'Si') ") == "si":
            pass
    else:
        print "NO SE ENCONTRO EL FICHERO"
        print "### ficheros encontrados:"
        for f in files:
            print " - "+f
