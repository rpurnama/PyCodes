import serial
import sys
import time

#import credentials

READ_TIMEOUT = 8


def main():

    print "\nInitializing serial connection"

    console = serial.Serial(
        port='COM3',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=READ_TIMEOUT
    )

    if not console.isOpen():
        sys.exit()

    console.write("\r\n\r\n")
    time.sleep(1)
    input_data = console.read(console.inWaiting())
    print input_data
    """if 'Username' in input_data:
        console.write(credentials.username + '\r\n')
	time.sleep(1)
	"""
    input_data = console.read(console.inWaiting())
	
if __name__ == "__main__":
    main()