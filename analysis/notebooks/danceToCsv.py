from HIMUServer import HIMUServer
from datetime import datetime
import csv

filename = str(datetime.now()) + ".csv"


# An example of listener implementation.
class SimplePrintListener:
    def __init__(self, serverInstance):
        self.__server = serverInstance
        f = open(filename, 'w')
        f.write("@ HyperIMU - ianovir\n\
@ Date:Thu May 21 15:07:17 GMT+02:00 2020, Sampling Rate:20ms\n\
@ chris dancing, Ed Sheeran - Shape of You\n\
\n\
timestamp,accelerometer_lsm6ds3_c.x,accelerometer_lsm6ds3_c.y,accelerometer_lsm6ds3_c.z,als_B.x,als_B.y,als_B.z,linear_Acceleration.x,linear_Acceleration.y,linear_Acceleration.z,rotation_Vector.x,rotation_Vector.y,rotation_Vector.z\n\
\n")
        f.close()

    def notify(self, sensorData):
        line = ''
        if len(sensorData) == 0:
            return
        sensors = sensorData[0]

        for sensor in sensors:
            for field in sensor:
                if isinstance(field, str):
                    line += '%s,' % field
                elif isinstance(field, float):
                    line += '%f,' % field
                else:
                    line += field
        line += '\n'

        f = open(filename, 'a')
        f.write(line)
        f.close()

        HIMUServer.printSensorsData(sensorData)

    # for a string-to-float conversion, try HIMUServer.strings2Floats()


# HIMUServer instance:
myHIMUServer = HIMUServer()

# Creating listener and adding it to the server instance:
myListener = SimplePrintListener(myHIMUServer)
myHIMUServer.addListener(myListener)

# Change the timeout (in seconds) :
myHIMUServer.timeout = 10

# Launch acquisition via TCP on port 2055:
myHIMUServer.start("TCP", 2055)

# Launch acquisition via UDP on port 2055:
# myHIMUServer.start("UDP", 2055)

# Launch acquisition from local file:
# myHIMUServer.start("FILE", "HIMU-filetest.csv")
