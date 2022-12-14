# Send Case # and # of steps over Serial

from serial import Serial

n_steps = '500'

def search(n_steps):
    """
    """    
    pass

def write_serial(info):
    """
    """
    serialPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection
    serialPort.write(bytes(str(info), 'utf8'))              # Writes String over Serial to Arduino
    serialPort.close()

def forward(n_steps):
    """
    Case 0
    """
    write_serial('b' + n_steps)

def backward(n_steps):
    """
    Case 1
    """
    write_serial('c' + n_steps)

def forward_left_diagonal(n_steps):
    """
    Case 2
    """
    write_serial('d' + n_steps)

def forward_right_diagonal(n_steps):
    """
    Case 3
    """
    write_serial('e' + n_steps)

def backward_left_diagonal(n_steps):
    """
    Case 4
    """
    write_serial('f' + n_steps)

def backward_right_diagonal(n_steps):
    """
    Case 5
    """
    write_serial('g' + n_steps)

def left(n_steps):
    """
    Case 6
    """
    write_serial('h' + n_steps)

def right(n_steps):
    """
    Case 7
    """
    write_serial('i' + n_steps)

def still():
    """
    Case 8
    """
    write_serial('a')

def main():
    """
    
    """
    
    forward(n_steps)
    backward(n_steps)

main()