import serial, time, requests
import json

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
        
ser = serial.Serial('/dev/ttyACM2', 115200)

url='FARMOS_URL'

headers = {
        'Content-Type': 'application/json',
    }

#serial_line='23.2'

#r = requests.post(url, headers=headers, json={"a2_temp": serial_line})

while True:

    ser.flushInput()
    time.sleep(2)

    serial_line = ser.readline().strip()
    
#    if(serial_line.strip()>3):
#        print("yeah")

    if isFloat(serial_line):
        print(serial_line)
        r = requests.post(url, headers=headers, json={"a2_temp": serial_line})
        print(r)
        time.sleep(120)
                
#    print(serial_line) # If using Python 2.x use: print serial_line

    #payload = {
    #    'a2_temp': serial_line
    #}
    
    #r = requests.post('https://en7bg6rby7twn.x.pipedream.net', json={"a2_temp": serial_line})
    #r = requests.post(url, headers=headers, json={"a2_temp": serial_line})
    #response = requests.post(url, headers=headers, data=json.dumps(payload))
    #print(r)
#    time.sleep(5) # sleep 5 minutes
