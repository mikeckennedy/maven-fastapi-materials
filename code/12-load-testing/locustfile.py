from locust import FastHttpUser, task, between


class PyPIUserMix(FastHttpUser):
    wait_time = between(5, 20)
    host = "http://127.0.0.1:8000"

    # Can do start up, init things like log in / get access token, then start requesting.
    # def on_start(self):
    #     self.client.post("/login", json={"username": "foo", "password": "bar"})

    @task(weight=1)
    def web_page(self):
        self.client.get("/")

    @task(weight=3)
    def package_details(self):
        self.client.get("/api/packages/count")
        self.client.get("/api/packages/details/fastapi")

    @task(weight=10)
    def package_search(self):
        self.client.get("/api/packages/search/fastapi")
        self.client.get("/api/packages/details/fastapi-pagination")
