import os
import shutil


DIR="/home/mating/Documents/COCIENTES_PRUEBAS/dir_prueba"

## crear directorio
try:
    os.mkdir(DIR)
except OSError:
    print("La creación del directorio %s falló" % DIR)
else:
    print("Se ha creado el directorio: %s " % DIR)

## borrar directorio
try:
    shutil.rmtree(DIR)
except OSError as e:
    print(f"Error:{ e.strerror}")