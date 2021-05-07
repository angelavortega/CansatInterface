import time
import random

serial_port = '/dev/tty' # Arduino port
baud_rate = 9600

class roverData():
    
    def __init__(self):
        #self.ser = serial.Serial(serial_port, baud_rate) # Serial COM with arduino
        pass
    
    def rcv_data(self):
        A = random.randint(20, 30) # Temperature
        B = random.randint(900, 1060) # Pressure
        C = random.randint(0, 100) # Altitude
        D = random.randint(-20, 20) # Latitude
        E = random.randint(-20, 20) # Longitude
        F = random.randint(-90, 90) # Roll
        G = random.randint(-90, 90) # Pitch
        H = random.randint(-90, 90) # Yaw   
        data = "{},{},{},{},{},{},{},{}".format(A, B, C, D, E, F, G, H)     
        data = data.encode()
        ### All Previous code will be sustitude by next command
        #data = self.ser.read()
        data = data.decode()
        return data

    def actData(self):
        """
        A = random.randint(20, 30) # Temperature
        B = random.randint(900, 1060) # Pressure
        C = random.randint(0, 100) # Altitude
        D = random.randint(-20, 20) # Latitude
        E = random.randint(-20, 20) # Longitude
        F = random.randint(-90, 90) # Roll
        G = random.randint(-90, 90) # Pitch
        H = random.randint(-90, 90) # Yaw
        """
        while True:
            try:
                data = self.rcv_data()
                data = data.split(",")
                i = 0
                for value in data:
                    data[i] = float(value)
                    i += 1
                return data
            except:
                continue
    