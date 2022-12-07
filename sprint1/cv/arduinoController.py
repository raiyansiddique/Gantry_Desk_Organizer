from serial import Serial

def writeSerial(info):
    serialPort = Serial('/dev/ttyACM0', 9600, timeout=1) #Establishes Serial connection
    serialPort.write(b"%d", info)
