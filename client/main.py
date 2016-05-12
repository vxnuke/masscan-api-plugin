import os
import subprocess
import httplib
import json
import time
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.cfg')
server = config.get('Main', 'server')
proto = config.get('Main', 'proto')
output_dir = config.get('Main', 'output_dir')
rate = config.get('Main', 'rate')

i = 1
while True:
	while os.path.exists(output_dir+str(i)+".xml") == True:
		i = i + 1
	if (os.path.exists("./stop")):
		exit("Detected exit file")
	print "Connecting..."
	conn = httplib.HTTPSConnection(server)
	conn.request("GET", "/api/request.php?get=host")
	r1 = conn.getresponse()
	if (str(r1.status)+" "+str(r1.reason) == '404 Not Found'):
		print "Server not configured correctly recieved: \nError 404 Not Found\nExiting..."
		conn.close()
		exit()
	if (str(r1.status)+" "+str(r1.reason) == '522 Origin Connection Time-out'):
		print "522 Origin Connection Time-out\nExiting..."
		conn.close()
		exit()
	print r1.status, r1.reason
	data1 = r1.read()
	if (str(data1) == 'No jobs available at this time{"host" : "", "port" : "", "shard" : ""}'):
		print "No more jobs queued\nExiting..."
		conn.close()
		exit()
	j = json.loads(str(data1))
	host = str(j['host'])
	port = str(j['port'])
	shard = str(j['shard'])
	#print "Recieved: "+data1
	print "Scanning range: "+host+" Port: "+port+" Shard: "+shard
	## EXECUTE HERE
	subprocess.call(['masscan', '-p '+port, host, '--banners', '-oX', './output/'+str(i)+'.xml', '--shards', shard, '--rate', rate, '--exclude', '255.255.255.255'])
	##END EXECUTE
	print "Shard Complete!"
	print "Sleeping 3 seconds..."
	time.sleep(3)
	print "Marking shard as complete.\nConnecting..."
	conn.request("GET", proto+"://"+server+"/api/request.php?complete=yes&host="+host+"&port="+port+"&shard="+shard)
	r2 = conn.getresponse()
	print r2.status, r2.reason
	data2 = r2.read()
	print "Completed range: "+host+" Port: "+port+" Shard: "+shard
	conn.close()
	print "Sleeping 5 seconds..."
	time.sleep(5)
	print "Starting next job."
