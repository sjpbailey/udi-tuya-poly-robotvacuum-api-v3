import json


# from file
f = open('snapshot.json')
devices = json.load(f)
list = json.dumps(devices, indent=4)

for i in devices['devices']:
    # name = i['name']
    print(i['name'])
    print(i['id'])
    print(i['key'])
    print(i['ip'])
    print(i['dps'])
if "1" in i["dps"]["dps"]:
    print("SWITCH")
elif "20" in i["dps"]["dps"]:
    print("LED")

# for key in list:
#   print(key)

# for item in devices.items():
# print(str(item))
# print(str(item['devices']))

# for i in devices:
#   print(i.items['id'])
"""    print(i['name'])
    print(i['id'])
    print(i['key'])
    print(i['ip'])
    print(i['dps'])
if "1" in i["dps"]["dps"]:
    print("SWITCH")
elif "20" in i["dps"]["dps"]:
    print("LED")"""

# print("Node DPS {}".format(str(devices['dps'])))

"""for dict_found in [x for x in devices_list if x["id"] == value['gwId']]:
    value['name'] = dict_found['name']
    value['key'] = dict_found['key']
    device_node = self.poly.getNode(device_id)
    LOGGER.info(f"device_node: {device_node}")
    if device_node is None:
    LOGGER.info(
        f"Adding Node: {device_id} - {dict_found['name']}")"""


"""for value in devices():
    name = value['name']
    ip = value['ip']
    device_id = value['gwId']
    key = value['key']
    dps = value['dps']
    ip1 = ip[-3:].lstrip('.')
    address = ip1
    # Information
    print(name)
    print(ip)
    print(device_id)
    print(key)
    print(dps)
    # Take the 'dps' status and separates Device types
    # Currently a value of '1' is for a switch and'20' LED
    if "1" in value["dps"]["dps"]:
        LOGGER.info("SWITCH")
        node = tuya_switch_node.SwitchNode(
            self.poly, self.address, address, name, device_id, ip, key)
        self.poly.addNode(node)
        self.wait_for_node_done()
    elif "20" in value["dps"]["dps"]:
        LOGGER.info("LED")
        node = tuya_light_node.LightNode(
            self.poly, self.address, address, name, device_id, ip, key)
        self.poly.addNode(node)
        self.wait_for_node_done()
    else:
        LOGGER.info("OTHER")
                    #    address = +1
                    #    node = tuya_light_node.LightNode(
                    #        self.poly, self.address, address, value['name'], value['gwId'], value['ip'], value['key'])
                    #    self.poly.addNode(node)
                    #    self.wait_for_node_event()"""
