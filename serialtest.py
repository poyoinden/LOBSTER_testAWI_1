import serial
import datetime

port = serial.Serial("/dev/serial0", baudrate=115200, timeout=3.0)

while True:
	#print port.isOpen()
	port.write(str(datetime.datetime.utcnow()) + "  Helloworld\r\n")
