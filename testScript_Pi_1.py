# Import libraries.
import time
import os
import subprocess
import serial
import datetime

# Function definitions.
def camera_handling():
    """ camera_handling checks availability, encodes and sends pictures. """
    exitcode = subprocess.call("sh " + "camera.sh", shell=True)
    #res = subprocess.check_output(["sh camera.sh"], shell=True)
    #print(exitcode)
    return


def measure_temp(): #!
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "").replace("'C", "").replace("\n","")


def retreive_data():
    """ retreive_data pulls internal temp. and current timestamp. """

    return


def encoding():
    """ encoding encodes the picture and other data and represents it as a string. """

    return


def logging(inputstring = ""):
    """ Logging saves an input string to a datetimestamped file."""
    with open('log.txt', 'a') as log_file:
        log_file.write(inputstring + '\n')
    return


def print_to_UART(inputstring = ""):
    """ print_to_UART prints an input string to the UART port. """
    port = serial.Serial("/dev/serial0", baudrate=115200, timeout=3.0)
    print("printing... " + inputstring)
    port.write(inputstring)  #str(datetime.datetime.utcnow()) + " Helloworld\r\n")
    return


if __name__ == "__main__":
    period = 0.3  # Creates about ~1GB/hr in pictures.
    t = time.time()
    counter = 0

    while True:
        t += period

        #camera_handling()
        retreive_data()
        encoding()
        logging()
#	print measure_temp()
        print_to_UART(str(datetime.datetime.utcnow()) + "\t" + str(measure_temp()) + "\n")
#	print_to_UART(measure_temp())
        time.sleep(max(0, t - time.time()))
