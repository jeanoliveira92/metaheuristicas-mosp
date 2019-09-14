import time

class timeCounter:

    def start(self):
        self.start = time.time()

    def stop(self):
        self.total = time.time() - self.start

    def total(self):
        return self.total