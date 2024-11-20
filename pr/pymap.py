#!/usr/bin/env python2
import sys

# Leer cada linea desde la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco al principio y al final
    line = line.strip()
    # Dividir la línea en palabras
    words = line.split()
    # Emitir cada palabra con un conteo de 1
    for word in words:
        print("{}\t1".format(word))


'''
Comandos a utilizar para ejecutar este script y sus argumentos a pasar 
python3 pymap.py < archivo_txt.txt > respuesta_txt.txt


Comando final a ejecutar:

python3 pymap.py < quijote-1.txt > map_output.txt

Explicaciones:

El símbolo < redirige el contenido de quijote-1.txt como entrada estándar (stdin) al script pymap.py.
El símbolo > redirige la salida estándar (stdout) de pymap.py a un archivo llamado map_output.txt
'''