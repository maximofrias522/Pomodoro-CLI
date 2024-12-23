#!/bin/bash

# Nombre del programa
PROGRAMA="pomo"
DESTINO="/usr/local/bin"

echo "Iniciando la instalación de $PROGRAMA..."

# Verifica si tienes permisos de superusuario
if [[ $EUID -ne 0 ]]; then
  echo "Este script necesita ejecutarse como root. Usa sudo."
  exit 1
fi

# Verifica que el archivo existe
if [[ ! -f "$PROGRAMA" ]]; then
  echo "Error: No se encontró el archivo $PROGRAMA en el directorio actual."
  exit 1
fi

# Copia el archivo a /usr/local/bin
echo "Copiando $PROGRAMA a $DESTINO..."
cp "$PROGRAMA" "$DESTINO/"

# Asegura permisos de ejecución
echo "Configurando permisos de ejecución..."
chmod +x "$DESTINO/$PROGRAMA"

echo "¡Instalación completada! Ahora puedes ejecutar $PROGRAMA desde cualquier lugar."
