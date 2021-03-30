
import time
import random

class roverData():
    
    def __init__(self):
        self.n=0

    
    def actData(self):

        B = random.randint(50, 200)
        C = random.randint(500, 1000)
        D = random.randint(0, 100)
        E = random.randint(-90, 90)
        F = random.randint(-90, 90)
        G = random.randint(-90, 90)
        port = [self.n, B, C, D, E, F, G]
        self.n += 1

        return port
    