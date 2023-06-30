"""
Polyglot v3 node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 3.0.1 Jun 2023
"""
import udi_interface
import time
import json
from tuya_connector import (
    TuyaOpenAPI,)

LOGGER = udi_interface.LOGGER


class RelayNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, new_id, deviceid, apiAccessId, apiSecret, apiEndpoint):
        super(RelayNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)  # address,name
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.new_id = new_id
        self.deviceid = deviceid
        self.DEVICESW_ID = deviceid
        self.apiAccessId = apiAccessId
        self.ACCESS_ID = apiAccessId
        self.apiSecret = apiSecret
        self.ACCESS_KEY = apiSecret
        self.apiEndpoint = apiEndpoint
        self.API_ENDPOINT = apiEndpoint
        self.SwStat(self)
        self.setDriver('ST', 1)

    def setSwOn1(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_1', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOff1(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_1', 'value': False}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOn2(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_2', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOff2(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_2', 'value': False}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOn3(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_3', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOff3(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_3', 'value': False}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOn4(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_4', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def setSwOff4(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_4', 'value': False}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
        time.sleep(.5)
        self.SwStat(self)

    def SwStat(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        response1 = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")  # DEVICE_ID
        LOGGER.info(response1)

        for i in response1['result'][0:1]:
            LOGGER.info(i['value'])
            if i['value'] == True:
                self.setDriver('GV2', 1)
            elif i['value'] == False:
                self.setDriver('GV2', 0)
            pass
        for i in response1['result'][1:2]:
            LOGGER.info(i['value'])
            if i['value'] == True:
                self.setDriver('GV3', 1)
            elif i['value'] == False:
                self.setDriver('GV3', 0)
            pass
        for i in response1['result'][2:3]:
            LOGGER.info(i['value'])
            if i['value'] == True:
                self.setDriver('GV4', 1)
            elif i['value'] == False:
                self.setDriver('GV4', 0)
            pass
        for i in response1['result'][3:4]:
            LOGGER.info(i['value'])
            if i['value'] == True:
                self.setDriver('GV5', 1)
            elif i['value'] == False:
                self.setDriver('GV5', 0)
            pass

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            self.query(self)
            self.SwStat(self)
            LOGGER.debug('shortPoll (node)')

    def query(self, command=None):
        self.SwStat(self)
        self.reportDrivers()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2},
        {'driver': 'GV2', 'value': 0, 'uom': 2},
        {'driver': 'GV3', 'value': 0, 'uom': 2},
        {'driver': 'GV4', 'value': 0, 'uom': 2},
        {'driver': 'GV5', 'value': 0, 'uom': 2},
    ]

    id = 'relay'

    commands = {
        'SWTON1': setSwOn1,
        'SWTOF1': setSwOff1,
        'SWTON2': setSwOn2,
        'SWTOF2': setSwOff2,
        'SWTON3': setSwOn3,
        'SWTOF3': setSwOff3,
        'SWTON4': setSwOn4,
        'SWTOF4': setSwOff4,

        'QUERY': query
    }
