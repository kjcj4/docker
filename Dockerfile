# Usar la imagen oficial de Python 3.9 como base
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos del proyecto al contenedor
COPY . /app/

# Exponer el puerto 5000 (el puerto por defecto de Flask)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Definir el punto de entrada al contenedor
ENTRYPOINT ["flask"]




