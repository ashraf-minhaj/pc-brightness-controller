""" Computer Hack! 
    Brightness Controller

    (C) License: GPL3-General Public License

    author: ashraf minhaj
    mail  : ashraf_minhaj@yahoo.com
"""

""" libraries -
$ pip install pyserial
$ pip install screen-brightness-control
"""

# import necessary libraries
import serial                                     # for serial communication
import serial.tools.list_ports                    # to get Arduino port automatically
import screen_brightness_control as brightness    # to control brightness

# device buadrate (bit per second)
# (change buadrate according to your need)
BUAD_RATE = 9600                                  # Pro Micro's buad rate is 9600 
PORT      = ""

# get sender device port automatically
serial_ports = list(serial.tools.list_ports.comports())  # get list of ports
for s_port in serial_ports:                              # iterate through all ports
    if 'Arduino Micro' in s_port.description:            # look for Pro Micro board
        PORT = str(s_port[0])                            # select first found board and
        break                                            # proceed

# connect with sender device
sender = serial.Serial(PORT, BUAD_RATE)

def map_value(value, in_min=0, in_max=1024, out_min=0, out_max=100):
    """ To map values. Arduio sends values from 0 to 1024. My goal
    is to make them in between 0 to 100."""
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# mainloop
while 1: 
    # convert byte data into string then integer
    sensor_value = int(sender.readline().decode("utf-8"))  # get data
    final_value = map_value(value=sensor_value)            # map value (brightness in percentage)
    #print(sensor_value)
    #print(final_value)
    brightness.set_brightness(final_value)                 # set brightness

# close port properly so that others can use it
sender.close()