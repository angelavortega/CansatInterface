import time
import random
import serial

serial_port = '/dev/ttyACM0' # Arduino port
baud_rate = 9600


class roverData():
    
    def __init__(self):
        self.ser = serial.Serial(serial_port, baud_rate) # Serial COM with arduino
        self.letters = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    def rcv_data(self):
        def rad_data():
            b = self.ser.readline()			 # read a byte string 
            string_n = b.decode()		 # decode byte string into Unicode	
            string = string_n.rstrip()
            return string
        initiate = False
        dict_data = []
        if not self.ser.isOpen(): self.ser.open()
        while(True):
            string = rad_data()
            try: 
                if string[0] == 'A':
                    dict_data = [float(string[1:])]
                    initiate = True
                elif string[0] in self.letters and initiate:
                    dict_data.append(float(string[1:]))
                if len(dict_data) == 8:
                    self.ser.close()
                    return dict_data
            except:
                initiate = False
                dict_data = []

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
            data = self.rcv_data()
            return data