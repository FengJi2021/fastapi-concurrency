from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def async_sleep(self):
        self.client.get("/async_sleep")

    @task
    def async_sleep_await(self):
        self.client.get("/async_sleep_await")

    @task
    def sync_sleep(self):
        self.client.get("/sync_sleep")
