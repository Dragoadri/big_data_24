#!/usr/bin/env python2
import sys

# Diccionario para almacenar el conteo de palabras
word_count = {}

# Leer cada línea desde la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco al principio y al final
    line = line.strip()
    # Dividir la línea en palabra y conteo
    word, count = line.split("\t", 1)
    # Convertir el conteo a entero
    try:
        count = int(count)
    except ValueError:
        continue
    # Acumular el conteo de palabras
    if word in word_count:
        word_count[word] += count
    else:
        word_count[word] = count

# Emitir cada palabra con su conteo total
for word in word_count:
    print("{}\t{}".format(word, word_count[word]))
