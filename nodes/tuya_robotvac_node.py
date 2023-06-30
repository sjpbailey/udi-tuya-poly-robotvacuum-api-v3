"""
Polyglot v3 node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 3.0.1 Jun 2023
"""
import asyncio
import colorsys
import udi_interface
import time
import json
from tuya_bulb_control import Bulb
from tuya_connector import (
    TuyaOpenAPI,)


LOGGER = udi_interface.LOGGER


class RobvacNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, new_id, deviceid, apiAccessId, apiSecret, apiEndpoint, apiRegion):
        super(RobvacNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.new_id = new_id
        self.deviceid = deviceid
        self.DEVICEBOT_ID = deviceid
        self.apiAccessId = apiAccessId
        self.ACCESS_ID = apiAccessId
        self.apiSecret = apiSecret
        self.ACCESS_KEY = apiSecret
        self.apiEndpoint = apiEndpoint
        self.API_ENDPOINT = apiEndpoint
        self.apiRegion = apiRegion
        self.API_REGION = apiRegion
        self.SwStat(self)
        self.setDriver('ST', 1)
        
    # Robot On
    def setSwOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEBOT_ID = self.DEVICEBOT_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'power_go', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
        time.sleep(.5)
        self.setDriver('GV2', 1)
        #self.SwStat(self)

    # Robot Off
    def setSwOff(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEBOT_ID = self.DEVICEBOT_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        
        commands = {'commands': [{'code': 'mode', 'value': 'chargego'}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
        time.sleep(.5)
        self.setDriver('GV2', 0)
        #self.SwStat(self)

    # Set Modes
    def modeOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEBOT_ID = self.DEVICEBOT_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.modeOn = int(command.get('value'))
        self.setDriver('GV3', self.modeOn)
        # Charge
        if self.modeOn == 0:
            commands = {'commands': [{'code': 'mode', 'value': 'chargego'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Charge')
            time.sleep(.5)
            self.SwStat(self)
        # Standby
        elif self.modeOn == 1:
            commands = {'commands': [{'code': 'mode', 'value': 'standby'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Standby')
            time.sleep(.5)
            self.SwStat(self)
        # Spiral
        elif self.modeOn == 2:
            commands = {'commands': [{'code': 'mode', 'value': 'spiral'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Spiral')
            time.sleep(.5)
            self.SwStat(self)
        # Wall Follow
        elif self.modeOn == 3:
            commands = {'commands': [{'code': 'mode', 'value': 'wall_follow'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Wall Follow')
            time.sleep(.5)
            self.SwStat(self)
        # Random
        elif self.modeOn == 4:
            commands = {'commands': [{'code': 'mode', 'value': 'random'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Random')
            time.sleep(.5)
            self.SwStat(self)
        # Partial Bow
        elif self.modeOn == 5:
            commands = {'commands': [{'code': 'mode', 'value': 'partial_bow'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Partial Bow')
            time.sleep(.5)
            self.SwStat(self)
        else:
            pass

    # Manual Control
    def modeMan(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEBOT_ID = self.DEVICEBOT_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.modeMan = int(command.get('value'))
        self.setDriver('GV7', self.modeMan)
        
        # Forward
        if self.modeMan == 0:
            commands = {'commands': [{'code': 'direction_control', 'value': 'forward'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Forward')
            time.sleep(.5)
            self.SwStat(self)
        # Backward
        elif self.modeMan == 1:
            commands = {'commands': [{'code': 'direction_control', 'value': 'backward'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Backwards')
            time.sleep(.5)
            self.SwStat(self)
        # Turn Left
        elif self.modeMan == 2:
            commands = {'commands': [{'code': 'direction_control', 'value': 'turn_left'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Turn Left')
            time.sleep(.5)
            self.SwStat(self)
        # Turn Right
        elif self.modeMan == 3:
            commands = {'commands': [{'code': 'direction_control', 'value': 'turn_right'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Turn Right')
            time.sleep(.5)
            self.SwStat(self)
        # Stop
        elif self.modeMan == 4:
            commands = {'commands': [{'code': 'power_go', 'value': False}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Stop')
            time.sleep(.5)
            self.SwStat(self)
        else:
            pass

    # Suction
    def modeSuc(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEBOT_ID = self.DEVICEBOT_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.modeSuc = int(command.get('value'))
        self.setDriver('GV8', self.modeSuc)
    
        # Suction Gentle
        if self.modeSuc == 0:
            commands = {'commands': [{'code': 'suction', 'value': "gentle"}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Suction Gentle')
            time.sleep(.5)
            self.SwStat(self)
        # Suction Normal
        elif self.modeSuc == 1:
            commands = {'commands': [{'code': 'suction', 'value': "normal"}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Suction Normal')
            time.sleep(.5)
            self.SwStat(self)
        # Suction High
        elif self.modeSuc == 2:
            commands = {'commands': [{'code': 'suction', 'value': "strong"}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEBOT_ID), commands)
            LOGGER.info('Suction High')
            time.sleep(.5)
            self.SwStat(self)
        else:
            pass

    def SwStat(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEBOT_ID = self.DEVICEBOT_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        response1 = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICEBOT_ID) + "/status/")
        LOGGER.info(response1)
        for i in response1['result'][0:1]:
            # LOGGER.info(i['value'])
            if i['value'] == True:
                self.setDriver('GV2', 1)
            elif i['value'] == False:
                self.setDriver('GV2', 0)
        for i in response1['result'][4:5]:
            self.setDriver('GV5', i['value'])
            LOGGER.info('Battery %')
        for i in response1['result'][6:7]:
            self.setDriver('TIME', i['value'])
            LOGGER.info('Clean time')
        for i in response1['result'][3:4]:
            LOGGER.info(i['code'])
            LOGGER.info(i['value'])
            if i['value'] == 'standby':
                self.setDriver('GV4',0)
            elif i['value'] == 'smart_clean':
                self.setDriver('GV4',1)
            elif i['value'] == 'wall_clean':
                self.setDriver('GV4',2)
            elif i['value'] == 'spot_clean':
                self.setDriver('GV4',3)
            elif i['value'] == 'goto_charge':
                self.setDriver('GV4',4)
            elif i['value'] == 'charging':
                self.setDriver('GV4',5)
            elif i['value'] == 'charge_done':
                self.setDriver('GV4',6)
            elif i['value'] == 'charging':
                self.setDriver('GV4',5)
            elif i['value'] == 'cleaning':
                self.setDriver('GV4',7)
            elif i['value'] == 'sleep':
                self.setDriver('GV4',8)
            else:
                pass
    
    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            self.SwStat(self)
            self.query(self)
            LOGGER.debug('shortPoll (node)')

    def query(self, command=None):
        self.SwStat(self)
        self.reportDrivers()

    drivers = [
        {'driver': 'GV2', 'value': 0, 'uom': 25},
        {'driver': 'GV3', 'value': 0, 'uom': 25},
        {'driver': 'GV4', 'value': 0, 'uom': 25},
        {'driver': 'GV5', 'value': 0, 'uom': 51},
        {'driver': 'TIME', 'value': 0, 'uom': 56},
        {'driver': 'GV7', 'value': 0, 'uom': 25},
        {'driver': 'GV8', 'value': 0, 'uom': 25},
        {'driver': 'ST', 'value': 1, 'uom': 2},

    ]

    id = 'robvac'

    commands = {
        'BOTON': setSwOn,
        'BOTOF': setSwOff,
        'MODE1': modeOn,
        'MODEM': modeMan,
        'MODES': modeSuc,        
        'QUERY': query,
    }
