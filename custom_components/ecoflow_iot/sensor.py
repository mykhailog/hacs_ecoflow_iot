"""Ecoflow IoT"""
import logging

import asyncio
from homeassistant.const import CONF_NAME
from aiohttp_requests import requests
from homeassistant.components.sensor import PLATFORM_SCHEMA
try:
    from homeassistant.components.sensor import SensorEntity
except ImportError:
    from homeassistant.components.sensor import SensorDevice as SensorEntity

import voluptuous as vol

_LOGGER = logging.getLogger(__name__)
DOMAIN = "ecoflow_iot"
CONF_DOMAIN = DOMAIN
CONF_APP_KEY = 'app_key' 
CONF_SECRET_KEY = 'secret_key' 
CONF_SERIAL_NUMBER = 'serial_number' 
CONF_DEVICES = 'devices'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    # vol.Required(CONF_DOMAIN): vol.Schema({
        vol.Required(CONF_APP_KEY): vol.All(str),
        vol.Required(CONF_SECRET_KEY): vol.All(str),
        vol.Required(CONF_DEVICES): vol.All(list, [{
            vol.Optional(CONF_NAME): vol.All(str),
            vol.Required(CONF_SERIAL_NUMBER): vol.All(str)
        }])
    # })
})

@asyncio.coroutine
async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    # config = config[CONF_DOMAIN]
    
    app_key = config[CONF_APP_KEY]
    secret_key = config[CONF_SECRET_KEY]
    devices = config[CONF_DEVICES]

    ecoflow_devices = []
    for device in devices:
        ecoflow_devices.append(EcoflowDevice(device, app_key, secret_key))

    async_add_entities(ecoflow_devices,True)

class EcoflowDevice(SensorEntity):
    def __init__(self, device_config, app_key, secret_key):
        self._name = device_config.get(CONF_NAME, f"Ecoflow {device_config[CONF_SERIAL_NUMBER]}")
        self._serial_number = device_config[CONF_SERIAL_NUMBER]
        self._app_key = app_key
        self._secret_key = secret_key
        self._state = None
        self._message = None
        self._soc = None
        self._remain_time = None
        self._watts_out_sum = None
        self._watts_in_sum = None
        self._charging = None
        self._charging_time = None
        self._discharging_time = None
        self._status = None
        self._available = False
        self._entities = []
        self._state_attrs = {}
    @property
    def available(self):
        """Return true when state is known."""
        return self._available

    @asyncio.coroutine  
    async def async_update(self):
        try:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "appKey": self._app_key,
                "secretKey": self._secret_key
            }
            url = f"https://api.ecoflow.com/iot-service/open/api/device/queryDeviceQuota?sn={self._serial_number}"
            response = await requests.get(url, headers=headers)
            data = await response.json()
            code = data["code"]
            self._message = data["message"]
            if code == "0":
                self._soc = data["data"]["soc"]
                self._remain_time = data["data"]["remainTime"]
                self._watts_out_sum = data["data"]["wattsOutSum"]
                self._watts_in_sum = data["data"]["wattsInSum"]
                self._charging = self._watts_in_sum > self._watts_out_sum 

                if self._watts_out_sum > 0 and self._watts_in_sum == 0:
                    self._status = "discharging"
                    self._charging_time = None
                    self._discharging_time = self._remain_time
                elif self._watts_in_sum == self._watts_out_sum:
                    self._status = "bypass"
                    self._charging_time = None
                    self._discharging_time = None
                elif self._charging:
                    self._charging_time = self._remain_time
                    self._discharging_time = 0
                    self._status = "charging"
                else:
                    self._discharging_time = self._remain_time
                    self._charging_time = None
                    self._status = "idle"
                self._available = True
                
                # self._entities = [
                #     EcoflowAttribute(f'{self._name} SOC', self._soc, '%'),
                #     EcoflowAttribute(f'{self._name} remainTime', self._remain_time, 'seconds'),
                #     EcoflowAttribute(f'{self._name} wattsOutSum', self._watts_out_sum, 'W'),
                #     EcoflowAttribute(f'{self._name} wattsInSum', self._watts_in_sum, 'W'),
                #     EcoflowAttribute(f'{self._name} charging', self._charging, None),
                #     EcoflowAttribute(f'{self._name} charging_time', self._charging_time, 'seconds'),
                #     EcoflowAttribute(f'{self._name} discharging_time', self._discharging_time, 'seconds'),
                #     EcoflowAttribute(f'{self._name} status', self._status, None)
                # ]
            else:
                _LOGGER.error("Error connecting to Ecoflow, code: %s, message: %s", code, self._message)
                self._status = "error"
                self._available = False
                self._entities = []
        except requests.exceptions.RequestException as e:
            _LOGGER.error(f"Error updating device {self._name}: {e}")
            self._status = "error"
            self._available = False
            self._entities = []  
    
    @property
    def extra_state_attributes(self):
        """Return the state attributes of the device."""
        return {
            'status': self._status,
            'charging': self._charging,
            'charging_time': self._charging_time,
            'discharging_time': self._discharging_time,
            'remain_time': self._remain_time,
            'watts_out': self._watts_out_sum,
            'watts_in': self._watts_in_sum
        }
    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._soc

    @property
    def message(self):
        return self._message

    @property
    def entities(self):
        return self._entities

    @property
    def device_class(self):
        return 'battery'


class EcoflowAttribute(SensorEntity):
    def __init__(self, name, state, unit):
        self._name = name
        self._state = state
        self._unit = unit

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

