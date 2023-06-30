# Custom Parameters Call
from tuya_connector import (
    TuyaOpenAPI,)
import time
import json
import colorsys

ACCESS_ID = "txejpdfda9iwmn5cg2es"
ACCESS_KEY = "46d6072ffd724e0ba5ebeb5cc6b9dce9"
API_ENDPOINT = "https://openapi.tuyaus.com/"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"
API_REGION = "us"


# from file
# f = open('sample.json')
# response = json.load(f)
# list = json.dumps(devices, indent=4)


# Node Server Controller Testing
# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call APIs from Tuya
# Get device information from all devices
response = openapi.get("/v1.0/users/az1610958067414WkfOO/devices")
# print(type(response))

# Save polling data sample
# current = {'timestamp': time.time(), 'devices': response}
response1 = json.dumps(response, indent=4)  # current, indent=4
#print(response1)

# Writing to sample.json
# with open("sample.json", "w") as outfile:
#    outfile.write(str(response1))



########################       Sweeping Robot     ###################################################
# Switch Node
DEVICEBOT_ID = 'eb5add4f3bbf86a94bs3o6'
response = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICEBOT_ID) + "/status/")  # DEVICE_ID

# ['result'][0:1] powergo ("True", "False")
# ['result'][1:2] Mode ("standby","spiral","wall_follow","random","chargego","partial_bow")
# ['result'][1:3] direction_control ("forward", "backward","turn_left","turn_right","stop")
# ['result'][3:4] status range ("standby","smart_clean","wall_clean","spot_clean","goto_charge","charging","charge_done","cleaning","sleep")
# ['result'][4:5] electricity aka battery (0-100 in %)
# ['result'][5:6] Suction range ("gentle", "normal", "strong")
# ['result'][6:7] Clean Time (0-9999 in minutes)
# ['result'][7:8] Fault (in bitmap label? 0-14)
# ['result'][8:9] cistern ("closed","low","high")


#Sweeping Robot
for i in response['result'][3:4]:
    print(i['code'])
    print(i['value'])
    if i['value'] == 'charge_done':
        print('Charged')
    if i['value'] == 'charging':
        print('Charging')
    if i['value'] == 'cleaning':
        print('Cleaning')
    if i['value'] == 'sleep':
        print('Sleep')
    if i['value'] == 'standby':
        print('Standby')
    if i['value'] == 'smart_clean':
        print('Smart Clean')
    if i['value'] == 'wall_clean':
        print('Wall Clean')
    if i['value'] == 'spot_clean':
        print('Spot Clean')
    if i['value'] == 'goto_charge':
        print('Going Home')
    
    
    else:
        print("no")


"""result ={
            "active_time": 1687891468,
            "biz_type": 0,
            "category": "sd",
            "create_time": 1687891468,
            "icon": "smart/icon/ay1534681176370JSCKe/6da3d47ccf759a6261579440f561042f.jpg",
            "id": "eb5add4f3bbf86a94bs3o6",
            "ip": "98.41.236.33",
            "lat": "37.7200",
            "local_key": "?7.Flw'W@~zI3HuR",
            "lon": "-121.4700",
            "model": "BR151R",
            "name": "Sweeping robot",
            "online": True,
            "owner_id": "33161067",
            "product_id": "ela0pxryflaldubr",
            "product_name": "Sweeping robot",
            "status": [
                {
                    "code": "power_go",
                    "value": False
                },
                {
                    "code": "mode",
                    "value": "standby"
                },
                {
                    "code": "direction_control",
                    "value": "forward"
                },
                {
                    "code": "status",
                    "value": "charging"
                },
                {
                    "code": "electricity_left",
                    "value": 69
                },
                {
                    "code": "suction",
                    "value": "normal"
                },
                {
                    "code": "clean_time",
                    "value": 0
                },
                {
                    "code": "fault",
                    "value": 0
                },
                {
                    "code": "cistern",
                    "value": "low"
                }
            ],
            "sub": False,
            "time_zone": "-07:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1687891472,
            "uuid": "853011974bc304be"
        },"""


