from serial import Serial
import time

n_steps = '500'
serialPort = Serial('/dev/ttyACM1', 9600, timeout=1)    # Establishes Serial connection 
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

def stop(n_steps):
    """
    Case a. Stop
    """
    serialPort.write('a' + n_steps)
    
def move_up(n_steps):
    """
    Case b. 
    """
    serialPort.write('b' + n_steps)

def move_down(n_steps):
    """
    Case c. 
    """
    serialPort.write('c' + n_steps)

def open_gripper(n_steps):
    """
    Case d. 
    """
    serialPort.write('d' + n_steps)

def close_gripper(n_steps):
    """
    Case e. 
    """
    serialPort.write('e' + n_steps)
    