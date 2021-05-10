import time
import random
import serial

serial_port = '/dev/ttyACM0' # Arduino port
baud_rate = 9600


class roverData():
    
    def __init__(self):
        self.ser = serial.Serial(serial_port, baud_rate) # Serial COM with arduino
        self.letters = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
        pass
    
    def rcv_data(self):
        def rad_data(self):
            b = self.ser.readline()			 # read a byte string 
            string_n = b.decode()		 # decode byte string into Unicode	
            string = string_n.rstrip()
            return string
        if not self.ser.isOpen(): self.ser.open()
        while True:
            string = rad_data()
            if string[0] == "A":
                data = string[1:]
                while True:
                    string = rad_data()
                    if string[0] in self.letters:
                        data = data + string[1:]
                        if string[0] == 'H':
                            data = data[0:-1]
                            self.ser.close()
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
                data = data.split(";")
                i = 0
                for value in data:
                    data[i] = float(value)
                    i += 1
                return data
            except:
                continue
    