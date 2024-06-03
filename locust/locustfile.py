from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 1) 

    @task(1)
    def endpoint1(self):
        self.client.get("/api/v1/endpoint1")

    @task(1)
    def endpoint2(self):
        self.client.get("/api/v1/endpoint2")

    @task(1)
    def endpoint3(self):
        self.client.get("/api/v1/endpoint3")
