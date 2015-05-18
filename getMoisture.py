from __future__ import division
import mcp3008
import sys

def ConvertTemp(data,places):
	temp = ((data *  330)/float(1023))-50
	temp = round(temp,places)
	return temp

def ConvertTempCtoF(data):
	temp = (((data * 9) / 5) + 32)
	return temp

def ConvertMoistureToPercent(data):
	percent = ((data / 1024) * 100)
	return percent

temp_channel=0
moisture_channel=1
light_channel=2


sensorVal = mcp3008.readadc(1)
sensorPrcnt = ConvertMoistureToPercent(sensorVal)

print "Sensor Value: ", sensorVal
print "Sensor Percent: ", sensorPrcnt

