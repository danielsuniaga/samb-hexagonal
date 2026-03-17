FROM python:3.9.6

# Copia primero el archivo de espera wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh

# Dale permisos de ejecución al archivo de espera
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Copia los archivos requeridos y ejecuta las actualizaciones
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y curl tree
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

# Crea los directorios de logs necesarios
RUN mkdir -p /var/log/samb && chmod 755 /var/log/samb

# Establece el directorio de trabajo
WORKDIR /code

# Establece el script de entrada como el comando de inicio del contenedor
# ENTRYPOINT ["./entrypoints.sh"]