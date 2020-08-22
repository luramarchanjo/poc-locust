from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0.1, 1)

    @task
    def index_page(self):
        payload = {
            "name" : "Luram Archanjo"
        }
        self.client.post("/v1/proposals", json=payload)