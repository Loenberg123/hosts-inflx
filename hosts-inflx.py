#!/usr/bin/python
import os,sys,subprocess,argparse,json

# Get hosts sending data to a influxDB database

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--secure", help="Usar https en lugar de http", const="https", default="http", action="store_const")
parser.add_argument("-i", "--ip", help="Indica la ip de InfluxDB")
parser.add_argument("-d", "--database", help="Indica la base de datos para la consulta")
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()

q = "curl -s -G "+args.secure+"://"+args.ip+":8086/query --data-urlencode db=\""+args.database+"\" --data-urlencode \"q=SHOW TAG VALUES WITH KEY = host\""
result = subprocess.check_output(q, shell=True)
#print result

resp_dict = json.loads(result)
data = resp_dict['results'][0]['series'][0]['values']
n = len(data)
for i in range(0,n):
	form = data[i]
	form = str(form)
	form = form.split("'")[3]
	print form
