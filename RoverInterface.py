import matplotlib
from data.roverData import roverData


class mainInterface():

    def __init__(self):
        
        self.roverData = roverData()
    
    def loop(self):
        pass


if __name__ == "__main__":
    mainInterface = mainInterface