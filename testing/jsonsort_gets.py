# Custom Parameters Call
from tuya_connector import (
    TuyaOpenAPI,)
import time
import json
import colorsys
from tuya_bulb_control import Bulb

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


################################## LED RGB TEST ###############################
# 'ebe097c0407da32084kvtr'  # 'ebfc16d57ed374932cjqfk' # 804076608caab5d8ff58
DEVICELED_ID = 'ebfc16d57ed374932cjqfk'

bulb = Bulb(
            client_id=ACCESS_ID,
            secret_key=ACCESS_KEY,
            device_id=DEVICELED_ID,
            region_key=API_REGION,
)
current_colour = json.loads(bulb.current_value("scene_data_v2")) #colour_data_v2 #bright_value_v2
print(current_colour)
for i in current_colour['scene_units']:
    print(i['bright'])            

#commands = {'commands': [{'code': 'colour_data_v2', 'value': '{\"h\":0,\"s\":1000,\"v\":1000}'}]}
#openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
# (255, 0, 0)
#print('Red')
#print(current_colour)"""
new_lvl = int(10) #int(new_lvl)*10
commands = {'commands': [{'code': 'temp_value_v2', 'value':int(new_lvl) }]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
bri_lvl = int(1000) #int(new_lvl)*10
commands = {'commands': [{'code': 'bright_value_v2', 'value':int(bri_lvl) }]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
#current_rgb = tuple(map(lambda x:int(1000), current_colour))
#print('????')



"""            # Conversion current HSV to RGB
current_colour = colorsys.hsv_to_rgb(
    h=current_colour["h"] / 360,
    s=current_colour["s"] / 1000,
    v=current_colour["v"] / 1000,
    )
print("current color h s v")
print(current_colour)
# Convert the current RGB to format 0-255
current_rgb = tuple(map(lambda x: int(x * 255), current_colour))
print("current color r g b" )
#print(current_rgb)

rainbow = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0], "green": [
            0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95], "violet": [139, 0, 255], "white": [255, 255, 255]}

        
r = (255)
g = (0)
b = (100)

new_colour = (r, g, b)
# Convert RGB coordinates to int
new_colour = tuple(map(lambda x: int(x), new_colour))
print(new_colour)
# Set colour ✨
bulb.set_colour_v2(new_colour)
time.sleep(2)

h = float(0)
s = float(0)
v = float(15)
new_hsv = (h, s, v)
new_hsv = tuple(map(lambda x: float(x * 1), new_hsv))
print(new_hsv)
bulb.set_colour_v2(new_hsv)

new_lvl = tuple(map(lambda x: float(x * 1), new_hsv))
bulb.scene_data_v2(new_lvl)

## Brightness
#commands = {'commands': [{'code': 'colour_data_v2', 'value': '{\"bright\":1000'}]}
#openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
#time.sleep(2)
new_lvl = int(1000)
#commands = {'commands': [{'code': 'temp_value_v2', 'value': int(new_lvl)*10}]}
#openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
#commands = {'commands': [{'code': 'bright_value_v2', 'value': 1000}]}
#openapi.post(
#    '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
#commands = {'commands': [
#                {'code': 'colour_data_v2', 'value': '{\"h\":0,\"s\":1000,\"v\":new_lvl}'}]}"""
#



"""cmd_code = 'colour_data_v2'

def set_color(rgb):
    hsv = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
    commands = {
        'commands': [{
            'code': cmd_code,
            'value': {
                "h": int(hsv[0] * 360),
                "s": int(hsv[1] * 1000),
                "v": int(hsv[2] * 1000)
            }
        }]
    }

#hsv = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
#print(hsv)
# '{\"h\":255,\"s\":0,\"v\":10}'}]}  # \"h\":272,\"s\":1000,

#c.sendcommand(id, commands)


# Rainbow values
rainbow = {"red": (255, 0, 0), "orange": (255, 127, 0), "yellow": (255, 200, 0),
           "green": (0, 255, 0), "blue": (0, 0, 255), "indigo": (46, 43, 95),
           "violet": (139, 0, 255), "white": (255, 255, 255)}

# Rotate through the rainbow
for color in rainbow:
    print("Changing color to %s" % color)
    set_color(rainbow[color])
    time.sleep(5)"""

"""{
            "active_time": 1610958307,
            "biz_type": 0,
            "category": "dj",
            "create_time": 1610825045,
            "icon": "smart/icon/ay1526363067472WHq8d/b354bef20490dfd22c5a3d4c89b6269c.png",
            "id": "ebfc16d57ed374932cjqfk",
            "ip": "98.41.236.33",
            "lat": "37.7182",
            "local_key": "805217605357161b",
            "lon": "-121.4700",
            "model": "SL10",
            "name": "LED Office",
            "online": true,
            "owner_id": "33161067",
            "product_id": "vcbxdeohrcq4tcpq",
            "product_name": "Smart Bulb-SL10",
            "status": [
                {
                    "code": "switch_led",
                    "value": true
                },
                {
                    "code": "work_mode",
                    "value": "colour"
                },
                {
                    "code": "bright_value_v2",
                    "value": 1000
                },
                {
                    "code": "temp_value_v2",
                    "value": 120
                },
                {
                    "code": "colour_data_v2",
                    "value": "{\"h\":240,\"s\":1000,\"v\":196}"
                },
                {
                    "code": "scene_data_v2",
                    "value": "{\"scene_num\":2,\"scene_units\":[{\"bright\":100,\"h\":0,\"s\":0,\"temperature\":1000,\"unit_change_mode\":\"static\",\"unit_gradient_duration\":13,\"unit_switch_duration\":14,\"v\":0}]}"
                },
                {
                    "code": "countdown_1",
                    "value": 0
                },
                {
                    "code": "music_data",
                    "value": ""
                },
                {
                    "code": "control_data",
                    "value": ""
                },
                {
                    "code": "rhythm_mode",
                    "value": "AAAAAAA="
                },
                {
                    "code": "sleep_mode",
                    "value": "AAA="
                },
                {
                    "code": "wakeup_mode",
                    "value": "AAA="
                }
            ],
            "sub": false,
            "time_zone": "-08:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1687949619,
            "uuid": "8d46651d2af2bb95"
        },"""



############################### Device ID's ###################################
"""# 'ebe097c0407da32084kvtr'  # 'ebfc16d57ed374932cjqfk' # 804076608caab5d8ff58
DEVICELED_ID = 'ebe097c0407da32084kvtr'

# Switch Node
DEVICESW_ID = '68635610e8db84fff7ea'

# Switch Node
DEVICEPIR_ID = 'eb29412a460a068676g8cv'"""

# Node Server Node Light Testing
# API will be passed from controller
#openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
#openapi.connect()



# do not run it just keeps going and going lol
"""starttime = time.time()
while True:
    print("tick")
    time.sleep(1.5 - ((time.time() - starttime) % 1.5))"""

"""for i in response['result']:
    name = i['name']
    model = i['model']
    print(name)
    print(model)"""


# PIR
"""{
            "active_time": 1686981690,
            "biz_type": 0,
            "category": "pir",
            "create_time": 1686981690,
            "icon": "smart/icon/ay15554925906369PM9S/131d393c8aa546206ffcf603f38ceb54.png",
            "id": "eb29412a460a068676g8cv",
            "ip": "98.41.236.33",
            "lat": "37.7200",
            "local_key": "~M0kO};;9R$d'wqL",
            "lon": "-121.4700",
            "model": "PIR-wifi-V01",
            "name": "PIR",
            "online": false,
            "owner_id": "33161067",
            "product_id": "o1l76njefmksbgkk",
            "product_name": "PIR",
            "status": [
                {
                    "code": "pir",
                    "value": "none"
                },
                {
                    "code": "battery_percentage",
                    "value": 100
                }
            ],
            "sub": false,
            "time_zone": "-07:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1687288443,
            "uuid": "8390601eff14128c"
        },"""


# Four Channel Relay Json Model Number-"TY-DIY-S04"
"""commands = {'commands': [{'code': 'switch_1', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_1', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
commands = {'commands': [{'code': 'switch_2', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_2', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
commands = {'commands': [{'code': 'switch_3', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_3', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
commands = {'commands': [{'code': 'switch_4', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_4', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
print(response)
time.sleep(2)
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
print(response)"""

"""response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")  # DEVICE_ID
for i in response1['result'][3:4]:
    print(i['value'])
    if i['value'] == True:
        print('gotya')"""

"""# Need to GET switch status Query NS
print('\n''GET Response Switch Statuses''\n')
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()
response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")  # DEVICE_ID
print(response1)
for i in response1['result'][0:1]:
    # print(i)
    print(i['value'])
# print("\n")
# print(response1)"""


"""{
    "result": [
        {
            "active_time": 1687404896,
            "biz_type": 0,
            "category": "kg",
            "create_time": 1687404896,
            "icon": "smart/icon/ay1525015673758Ghvpg/2587b975a6b0645e83559835ef7c7eef.png",
            "id": "68635610e8db84fff7ea",
            "ip": "98.41.236.33",
            "lat": "",
            "local_key": "#r0>b64A>a7<w_O:",
            "lon": "",
            "model": "TY-DIY-S04",
            "name": "WiFi switch-4CH",
            "online": true,
            "owner_id": "33161067",
            "product_id": "waq2wj9pjadcg1qc",
            "product_name": "WiFi switch-4CH",
            "status": [
                {
                    "code": "switch_1",
                    "value": false
                },
                {
                    "code": "switch_2",
                    "value": false
                },
                {
                    "code": "switch_3",
                    "value": false
                },
                {
                    "code": "switch_4",
                    "value": false
                },
                {
                    "code": "countdown_1",
                    "value": 0
                },
                {
                    "code": "countdown_2",
                    "value": 0
                },
                {
                    "code": "countdown_3",
                    "value": 0
                },
                {
                    "code": "countdown_4",
                    "value": 0
                },
                {
                    "code": "switch",
                    "value": false
                }
            ],
            "sub": false,
            "time_zone": "-08:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1687404903,
            "uuid": "68635610e8db84fff7ea"
        },"""


# Test LED On, Off and color change
"""commands = {'commands': [{'code': 'switch_led', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
commands = {'commands': [{'code': 'switch_led', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
commands = {'commands': [{'code': 'work_mode', 'value': 'colour'}]}
commands = {'commands': [{'code': 'colour_data_v2',
                          'value': '{\"h\":160,\"s\":1000,\"v\":1000}'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
commands = {'commands': [{'code': 'colour_data_v2',
                          'value': '{\"h\":240,\"s\":0,\"v\":1000}'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
commands = {'commands': [{'code': 'work_mode', 'value': 'red'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
# Dim
commands = {'commands': [{'code': 'colour_data_v2',
                          'value': '{\"h\":255,\"s\":0,\"v\":1000}'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)"""

# V2 Commands

# Bright
# commands = {'commands': [{'code': 'bright_value_v2', 'value': int(percent)*10}]}
# openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)

# commands = {'commands': [{'code': 'colour_data_v2',
#                          'value': '{\"h\":272,\"s\":1000,\"v\":1000}'}]}
# openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)

# V2
# Green = 120 1000 1000
# Red = 0 1000 1000
# Orange = 29 1000 1000
# Yellow = 47 1000 1000
# Blue = 240 1000 1000
# Indigo = 243 547 1000
# Violet = 272 1000 1000
# White = 272 1000 1000


# V1 Commands

# commands = {'commands': [{'code': 'colour_data',
#                          'value': '{\"h\":272,\"s\":1000,\"v\":1000}'}]}
# openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)

# V1
# Green = 120 1000 1000
# Red = 0 1000 1000
# Orange = 29 1000 1000
# Yellow = 47 1000 1000
# Blue = 240 1000 1000
# Indigo = 243 547 1000
# Violet = 272 1000 1000
# White = 272 1000 1000

# Need to GET led statuses Query NS
"""print('\n''GET Response LED Statuses''\n')
response0 = openapi.get(
    '/v1.0/iot-03/devices/' + DEVICELED_ID + '/status/')  # DEVICE_ID
response1 = json.dumps(response0, indent=4)
print(response1)
time.sleep(1)

current_colour = json.loads(response0.current_value(
    "colour_data"))  # For Version 2 # new_colour_v2
print(current_colour)"""


"""for i in response1[1:1]:
    pass
    print(i)
    print('dumps')
    # print(i['value'])
    # print(type(i['value']))
    # print(int(i['value']))
    # print(i['code']['switch_led'])


for k in response0['result'][2:3]:
    print(k['code'])
    print(k['value'])
    print(k['value'])
    print(type(['value']))"""


"""# range 10-1000
commands = {'commands': [{'code': 'bright_value_1', 'value': 0}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(1)
# "incandescent" # "halogen" # "led"
commands = {'commands': [{'code': 'led_type_1', 'value': 'halogen'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(1)
print('\n''GET Response LED Statuses''\n')
response0 = openapi.get(
    '/v1.0/iot-03/devices/' + DEVICELED_ID + '/status/')  # DEVICE_ID
print(response0)
# time.sleep(1)"""


"""{
                    "code": "led_type_1",
                    "value": "LED"
                }"""

"""commands = {'commands': [{'code': 'switch_led1', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
commands = {'commands': [{'code': 'switch_led1', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)

# commands = {'commands': [{'code': 'colour_data',
#                          'value': '{\"h\":100,\"s\":1000,\"v\":1000}'}]}
# openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)

response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICELED_ID) + "/status/")  # DEVICE_ID
# print(response1)"""

"""for k in response1['result'][slice(4)][1:3]:
    print('K')
    print(k['value'])
    # if k['code'][0]['bright_value_v2'] is True:
    #    print('Yes')
    # else:
    #    print('No')
d = response0

for i in response0['result'][2:3]:
    pass
    print(i['value'])
    # print(type(i['value']))
    # print(int(i['value']))
    # print(i['code']['switch_led'])
print("\n")
# print(response0)
print("\n")
time.sleep(5)"""

"""time.sleep(2)
# colour adjust bright # scene # music
commands = {'commands': [{'code': 'switch_led', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(1)
commands = {'commands': [{'code': 'switch_led', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(1)
commands = {'commands': [{'code': 'colour_data_v2',
                          'value': '{\"h\":272,\"s\":1000,\"v\":10}'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(2)
commands = {'commands': [{'code': 'colour_data_v2',
                          'value': '{\"h\":272,\"s\":1000,\"v\":1000}'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(5)
commands = {'commands': [{'code': 'work_mode', 'value': 'scene'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
time.sleep(1)
commands = {'commands': [{'code': 'temp_value_v2', 'value': '1000'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)"""

"""{
    "scene_num": 2,
    "scene_units": [
        {
            "bright": 100,
            "h": 0,
            "s": 0,
            "temperature": 1000,
            "unit_change_mode": "static",
            "unit_gradient_duration": 13,
            "unit_switch_duration": 14,
            "v": 0
        }
    ]
}"""


# Switch Node
DEVICESW_ID = 'eb29412a460a068676g8cv'


"""commands = {'commands': [{'code': 'switch_1', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_1', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)"""

"""# Need to GET switch status Query NS
print('\n''GET Response Switch Statuses''\n')
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()
response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")  # DEVICE_ID
print(response1)
for i in response1['result'][0:1]:
    # print(i)
    print(i['value'])
# print("\n")
# print(response1)"""

"""# Status for Switch
print("\nDone.\n")
response0 = {'result': [{'code': 'switch_1', 'value': False}, {'code': 'countdown_1', 'value': 0}],
             'success': True, 't': 1686947738881, 'tid': '5acc92200c8511eea9198a65b56d89fe'}

response2 = {'result': [{'code': 'switch_led', 'value': False}, {'code': 'work_mode', 'value': 'white'}, {'code': 'bright_value_v2', 'value': 712}, {'code': 'temp_value_v2', 'value': 1000}, {'code': 'colour_data_v2', 'value': '{"h":240,"s":1000,"v":1000}'}, {'code': 'scene_data_v2', 'value': '{"scene_num":3,"scene_units":[{"bright":25,"h":0,"s":0,"temperature":1000,"unit_change_mode":"static","unit_gradient_duration":13,"unit_switch_duration":13,"v":0}]}'}, {
    'code': 'countdown_1', 'value': 0}, {'code': 'music_data', 'value': ''}, {'code': 'control_data', 'value': ''}, {'code': 'rhythm_mode', 'value': 'AAAAAAA='}, {'code': 'sleep_mode', 'value': 'AAA='}, {'code': 'wakeup_mode', 'value': 'AAA='}], 'success': True, 't': 1686946451938, 'tid': '5bb819740c8211ee9d71220dd637f8d3'}
# print(type(response0))
# keysList = list(response.keys())
# print(keysList)

for i in response0['result'][0:1]:
    print(i['value'])
    # print(i['value'])"""



"""############################## Device Type decider add Node   #########################################

for i in response['result']:  
    print(i['model'])
    if i['model'] == "\u706f\u5e26\u63a7\u5236\u5668\uff08BK\uff09":
        print('LED-V1')
    if i['model'] == "SL10":
        print('LED-V2')
    if i['model'] == "SS01S\uff08\u706b\u7ebf\u8d1f\u8f7d\u7ebf\u4e0d\u5206\u7248\u672c\uff09BK\u7248\u672c":
        print('Switch-V0')
    if i['model'] == "SS01S(\u4e0d\u5206\u8d1f\u8f7d)\u4e50\u946b":
        print('Switch-V1')
    if i['model'] == "\u5f00\u5173(\u84dd\u7259+Wi-Fi)":
        print('Switch-V2')
    if i['model'] == "PIR-wifi-V01":
        print('PIR')


print('\n''Devices Sorted for ADD Node''\n')
for i in response['result']:
    # print(i)
    print('Name')
    print(i['name'])
    print('ID')
    print(i['id'])
    # print(i['status'])
    print('Status')
    print(i['status'][0]['value'])
# Incrementing addressing for Node Server ID
    print(i['id'])
    id = i['id']
    id1 = id[-7:].lstrip('.')
    address = id1
    print('Address')
    print(address)
    if "switch_1" in i['status'][0]['code']:
        print('Device Type')
        print("SWITCH")
        print('\n')
    elif i['model'] == "SL10":
        print('Device Type')
        print("LED-V2")
        print('\n')
    elif i['model'] == "\u706f\u5e26\u63a7\u5236\u5668\uff08BK\uff09":
        print('Device Type')
        print("LED-V1")
        print('\n')
    elif i['model'] == "PIR-wifi-V01":
        print('Device Type')
        print("PIR")
        print('\n')
    else:
        print("OTHER DEVICE")
        print('\n')"""


"""# ADD Node Sorted Data for Switch and Light
for i in response['result']:
    print(i['name'])
    # print(i['status'])
    print(i['status'][0]['value'])
### Incrementing addressing for Node Server ID        
    print(i['id'])
    id = i['id']
    id1 = id[-7:].lstrip('.')
    address = id1
    print(address)
    print('\n')    
#### Currently a value of 'switch_1' is for a switch and 'switch_led' is for an LED
### access_id, access_key and api_endpoint are passed from custom parameters
    if "switch_1" in i['status'][0]['code']:
        LOGGER.info("SWITCH")
        node = tuya_switch_node.SwitchNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
        self.poly.addNode(node)
        self.wait_for_node_done()
    elif "switch_led" in i['status'][0]['code']:
        LOGGER.info("LED")
        node = tuya_light_node.LightNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
        self.poly.addNode(node)
        self.wait_for_node_done()
    else:
        LOGGER.info("OTHER")
                    #    address = +1
                    #    node = tuya_light_node.LightNode(
                    #        self.poly, self.address, address, value['name'], value['gwId'], value['ip'], value['key'])
                    #    self.poly.addNode(node)
                    #    self.wait_for_node_event()"""
                    
                    

"""
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


result ={
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
