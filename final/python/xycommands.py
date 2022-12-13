from serial import Serial
import time

def sweepFromCorner():
    serialPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection 
    i = 0
    j = 0
    time.sleep(5)
    while True:
        
        serialPort.write(b'b100\n')  
        time.sleep(0.1)
        if i%2 == 0:   
            j = 0
            while j<20:       
                time.sleep(0.1)
                serialPort.write(b'h100\n')
                j += 1
        else:
            j = 0
            while j<20:
                time.sleep(0.1)
                serialPort.write(b'i100\n')
                j+=1
        i +=1
sweepFromCorner()