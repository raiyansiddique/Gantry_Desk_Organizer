from serial import Serial
import time
gripperPort = Serial('/dev/ttyACM1', 9600, timeout=1)    # Establishes Serial connection 
xyPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection 
time.sleep(5)
beam_state = gripperPort.readline().decode()
gripperPort.write(bytes(('e200' + '\n'), "utf8"))
time.sleep(2)
gripperPort.write(bytes(('c2000' + '\n'), "utf8"))
time.sleep(2)

print(beam_state)
while 'Broken' not in beam_state:
    xyPort.write(bytes(('b100' + '\n'), "utf8"))
    gripperPort.write(bytes(('a' + '\n'), "utf8"))
    print(beam_state)
    output = xyPort.readline().decode()
    beam_state = gripperPort.readline().decode()
    while 'finished' not in output:
        output = xyPort.readline().decode()
        pass
gripperPort.write(bytes(('d100' + '\n'), "utf8"))
time.sleep(0.1)
gripperPort.write(bytes(('b2000' + '\n'), "utf8"))
time.sleep(2)
xyPort.write(bytes(('b10000' + '\n'), "utf8"))
time.sleep(3)
xyPort.write(bytes(('l10000' + '\n'), "utf8"))
time.sleep(4)

    