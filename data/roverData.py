
import time
import random

class roverData():
    
    def __init__(self):
        self.n=0

    
    def actData(self):

        B = random.randint(50, 200)
        C = random.randint(500, 1000)
        D = random.randint(0, 100)
        E = random.randint(100, 500)
        port = [self.n, B, C, D, E]
        self.n += 1

        return port
    