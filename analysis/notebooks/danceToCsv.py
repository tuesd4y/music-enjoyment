from HIMUServer import HIMUServer
from datetime import datetime
import csv

filename = str(datetime.now()) + ".csv"

#An example of listener implementation.
class SimplePrintListener:
    def __init__(self, serverInstance):
        self.__server = serverInstance
        f = open(filename,'w')
        f.write("TODO\n")
        f.close()


    def notify (self, sensorData):
        line = ''
        sensors = sensorData[0]

        for sensor in sensors:
            for field in sensor:
                line += field + ','
        line += '\n'

        f = open(filename,'a')
        f.write(line)
        f.close()

        HIMUServer.printSensorsData(sensorData)

		#for a string-to-float conversion, try HIMUServer.strings2Floats()

#HIMUServer instance:
myHIMUServer = HIMUServer()

#Creating listener and adding it to the server instance:
myListener = SimplePrintListener(myHIMUServer)
myHIMUServer.addListener(myListener)


#Change the timeout (in seconds) :
myHIMUServer.timeout = 2

#Launch acquisition via TCP on port 2055:
myHIMUServer.start("TCP", 2055)

#Launch acquisition via UDP on port 2055:
#myHIMUServer.start("UDP", 2055)

#Launch acquisition from local file:
#myHIMUServer.start("FILE", "HIMU-filetest.csv")
