#!/usr/bin/env python

import os, re
import time, csv

#Directorio actual donde se encuentra nuestro script
actual_dir = os.path.dirname(os.path.realpath(__file__))
compare = raw_input("### Introduzca el nombre del fichero a comparar con el resto (type 'exit' to exit): ")
if compare != "exit":
    #BUSCAMOS TODOS LOS CSVs QUE HAY EN EL DIRECTORIO
    exp_csv = re.compile("^([\S\W]+)\.csv$")
    files = [f for f in os.listdir('.') if os.path.isfile(f) and exp_csv.match(f) ]

    if compare in files:
        compare_file = files.remove(compare)
        print "### Se encontro el fichero a comparar"
        for f in files:
            print " - "+f
        if raw_input("### Comparar todos los ficheros y generar archivos?(Type 'Si') ").upper() in ["SI","S","YES"]:
            cf = open('compare.csv')
            emails_to_compare = [line for line in csv.reader(cf)]
            cf.close()
            for f in files:
                fo = open(f)
                coincidencias = [line for line in csv.reader(fo) if line in emails_to_compare]
                fo.close()
                if len(coincidencias) > 0:
                    print "Se encontraron %d coincidencias en el fichero %s" % (len(coincidencias), f)
                    print "################"
                    to_write  = open('results_'+f, "wb")
                    writer = csv.writer(to_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    for row in coincidencias:
                        writer.writerow(row)
                    to_write.close()
    else:
        print "NO SE ENCONTRO EL FICHERO"
        print "### ficheros encontrados:"
        for f in files:
            print " - "+f
