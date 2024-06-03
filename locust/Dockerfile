FROM locustio/locust

COPY locustfile.py locust.conf /

ENTRYPOINT ["locust", "--config", "/locust.conf"]
