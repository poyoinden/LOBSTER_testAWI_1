# Import libraries.
import time
import os
import subprocess

# Function definitions.
def camera_handling():
    """ camera_handling checks availability, encodes and sends pictures. """
    exitcode = subprocess.call("sh " + "camera.sh", shell=True)
    #res = subprocess.check_output(["sh camera.sh"], shell=True)
    #print(exitcode)
    return


def measure_temp(): #!
    temp = os.popen("vcgencmd measure_temp").readline()
    print(temp)
    return temp.replace("temp=", "").replace("'C", "")


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
    print(inputstring)
    return


if __name__ == "__main__":
    period = 10  # Creates about ~1GB/hr in pictures.
    t = time.time()
    counter = 0

    while True:
        t += period

        #camera_handling()
        retreive_data()
        encoding()
        logging()
        print_to_UART("a")

        time.sleep(max(0, t - time.time()))
