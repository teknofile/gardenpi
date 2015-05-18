from time import sleep
import MySQLdb
import mcp3008
import sys

def ConvertTemp(data,places):
	temp = ((data *  330)/float(1023))-50
	temp = round(temp,places)
	return temp

def ConvertTempCtoF(data):
	temp = (((data * 9) / 5) + 32)
	return temp

temp_channel=0
moisture_channel=1
light_channel=2
sleepVal=60

mysql_host='gardenpi1.lgmt.teknofile.net'
mysql_port=3306
mysql_user='gardenpi1'
mysql_pass='temppass'
mysql_db='garden'

# Clear the screen and put the cursor at the top
#print '\x1b[2J\x1b[H'
#print 'Moisture sensor'
#print '===============\n'

while True:
	tempVal = mcp3008.readadc(temp_channel)
	moistureVal = mcp3008.readadc(moisture_channel)

	print "Temp Value: ", tempVal
	print "Moisture Value: ", moistureVal

	db = MySQLdb.connect("elk.lgmt.teknofile.net", "gardenpi1", "temppass", "garden");
	cur = db.cursor()
	insert_query = (
		"INSERT INTO sensor_data (sensor_name, sensor_type, sensor_val) "
		"VALUES('gardenpitemp', 'temp', " + str(tempVal) + ")")

	cur.execute(insert_query)

	insert_query = (
		"INSERT INTO sensor_data (sensor_name, sensor_type, sensor_val) "
		"VALUES('gardenpimoisture', 'moisture', " + str(moistureVal) + ")")
	cur.execute(insert_query)

	#cur.execute(insert_query, ('gardenpi1_moist', 'moisture', moistureVal))
	db.commit()
	db.close()
		
	sleep(sleepVal)

