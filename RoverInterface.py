import matplotlib
import time
from data.roverData import roverData


class mainInterface():

    def __init__(self):
        
        self.roverData = roverData()
    
    def readData(self):
        datos = self.roverData.actData()
        return datos


if __name__ == "__main__":
    mainInterface = mainInterface
    while True:
        datos = mainInterface.readData()
        print(datos)
        time.sleep(1)