from serial import Serial

gripperPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection 
xyPort = Serial('/dev/ttyACM1', 9600, timeout=1)    # Establishes Serial connection 

beam_state = gripperPort.readline().decode()

while 'Broken' not in beam_state:
    xyPort.write('b20')
    output = xyPort.readline().decode()
    while 'finished' not in output:
        output = xyPort.readline().decode()
        pass
    beam_state = gripperPort.readline().decode()
    