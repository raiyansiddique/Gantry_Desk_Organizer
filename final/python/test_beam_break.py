from serial import Serial
import time
gripperPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection 
xyPort = Serial('/dev/ttyACM1', 9600, timeout=1)    # Establishes Serial connection 
time.sleep(5)
beam_state = gripperPort.readline().decode()

while 'Broken' not in beam_state:
    xyPort.write(bytes(('b100' + '\n'), "utf8"))
    output = xyPort.readline().decode()
    while 'finished' not in output:
        output = xyPort.readline().decode()
        pass
    beam_state = gripperPort.readline().decode()
    