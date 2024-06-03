FROM locustio/locust

# Copiar los archivos necesarios
COPY locustfile.py locust.conf /

# Configurar el comando de inicio
ENTRYPOINT ["locust", "--config", "/locust.conf"]
