from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/es/blog/")

    wait_time = between(0.5, 10)