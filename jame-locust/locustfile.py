from locust import HttpUser, task, between

class  get_cat_facts(HttpUser):
    wait_time = between(1,5)
    @task(1)
    def get_catfacts(self):
        self.client.get("fact")
    
    @task(2)
    def get_catfact(self):
        self.client.get("facts")
        