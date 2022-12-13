from serial import Serial
import time

def sweepFromCorner():
    serialPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection 
    i = 0
    time.sleep(5)
    while i<20:
        
        serialPort.write(b'b100\n')  
        time.sleep(0.1)
        if i%2 == 0:          
            serialPort.write(b'h2150\n')
        else:
            serialPort.write(b'i2150\n')
        i +=1
