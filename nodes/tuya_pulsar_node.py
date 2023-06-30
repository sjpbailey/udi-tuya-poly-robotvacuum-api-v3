"""
Polyglot v3 node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 3.0.1 Jun 2023
"""
import asyncio
import udi_interface
import time
import json
import logging
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,)

LOGGER = udi_interface.LOGGER


class PullNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, new_id, deviceid, apiAccessId, apiSecret, apiEndpoint, apiMq):
        super(PullNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
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
        self.apiMq = apiMq
        self.API_MQ = apiMq
        self.setDriver('ST', 1)

    def logPulsarOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        ACCESS_MQ = self.API_MQ
        LOGGER.info(ACCESS_MQ)
        if ACCESS_MQ is not None:
            self.setDriver('GV2', 1)
        # Enable debug log
        TUYA_LOGGER.setLevel(logging.DEBUG)

        # Init openapi and connect
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        # Init Message Queue
        open_pulsar = TuyaOpenPulsar(ACCESS_ID, ACCESS_KEY, ACCESS_MQ, TuyaCloudPulsarTopic.PROD)
        time.sleep(15)
        open_pulsar.start()

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            self.query(self)
            self.SwStat(self)
            LOGGER.debug('shortPoll (node)')

    def query(self, command=None):
        self.reportDrivers()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2},
        {'driver': 'GV2', 'value': 0, 'uom': 2},
        #{'driver': 'GV3', 'value': 0, 'uom': 51},
    ]

    id = 'pulsa'

    commands = {
        'SWTON': logPulsarOn,
        'QUERY': query
    }
