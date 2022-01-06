import serial
import os
import http.client
import json
def colorfetch():
    arduino_data_connection = serial.Serial('COM3', 9800)
    datalist = []
    j = True
    i = 0
    while True:
        arduino_data_connection.write(b'1')
        data = arduino_data_connection.readline().decode("utf-8")
        #print(data)
        conn = http.client.HTTPSConnection("getpantry.cloud")
        payload = json.dumps({"current": data})
        headers = {'Content-Type': 'application/json'}
        conn.request("PUT", "/apiv1/pantry/2cb1189d-f1e5-4acb-8fba-c86b8282f25f/basket/DigiGeneV1", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        print(data)
        if data:
            file_1 = open("Current_color.txt", "w")
            file_1.write(data)
            file_1.close()
            i += 1
            if i == 100000:
                break

    arduino_data_connection.close()
    os.remove("Current_color.txt")



colorfetch()


