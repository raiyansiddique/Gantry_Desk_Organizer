from serial import Serial
import time
import math
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
serialPort = Serial('/dev/ttyACM0', 9600, timeout=1)  
time.sleep(5)
def backToZero(i, j):
    x = i
    if j < 0:
        y = -j
    else:
        y = j
    if y<=x:
        steps =  int(x * 100* math.sqrt(2))
        serialPort.write(bytes(('g'+ str(steps) + '\n'), "utf8"))
        output = serialPort.readline().decode()
        while 'finished' not in output:
            print(output)
            output = serialPort.readline().decode()
            pass
        if j<0:
            serialPort.write(bytes(('d'+ str((y-x) * 100) + '\n'), "utf8"))
        else:
            serialPort.write(bytes(('e'+ str((y-x) * 100) + '\n'), "utf8"))

        output = serialPort.readline().decode()
        while 'finished' not in output:
            print(output)
            output = serialPort.readline().decode()
            pass
    else:
        steps =  int(y * 100* math.sqrt(2))
        serialPort.write(bytes(('g'+ str(steps) + '\n'), "utf8"))
        output = serialPort.readline().decode()
        while 'finished' not in output:
            print(output)
            output = serialPort.readline().decode()
            pass
        if j<0:
            serialPort.write(bytes(('b'+ str((x-y) * 100) + '\n'), "utf8"))
        else:
            serialPort.write(bytes(('c'+ str((x-y) * 100) + '\n'), "utf8"))

        output = serialPort.readline().decode()
        while 'finished' not in output:
            print(output)
            output = serialPort.readline().decode()
            pass
backToZero(10, 10)