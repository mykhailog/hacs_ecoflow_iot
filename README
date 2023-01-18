# Ecoflow IoT Home Assistant Integration

<img width="457" alt="image" src="https://user-images.githubusercontent.com/1454659/213209294-f0cbf4ab-1f2d-431b-b249-b4f9f1007499.png">

This integration allows you to monitor devices connected to the Ecoflow IoT platform using Home Assistant.
It uses the Ecoflow REST API to retrieve data from the devices and make it available in Home Assistant.


## Warning

This integration provides only basic information about Ecoflow devices and doesn't allow you to do any control like turn on or turn off sockets.

## Installation

### HACS
If you use [HACS](https://hacs.xyz/) you can install and update this component.

1. Go into HACS -> CUSTOM REPOSITORIES and add url: https://github.com/mykhailog/hacs_ecoflow_iot with type "integration"
2. Go to integration, search "ecoflow_iot" and click *Install*.


### Manual
Copy the custom_components directory to your Home Assistant configuration directory.


## Configuration 

It is important to note that the APP_KEY and SECRET_KEY required for this integration to work need to be obtained from Ecoflow.
To get your APP_KEY and SECRET_KEY, please contact Ecoflow support at support@ecoflow.com. 
They will provide you with the necessary credentials to use this integration. 
Without the proper app_key and secret_key, the plugin will not be able to communicate with the Ecoflow API and the devices will not be available in Home Assistant.

Add the following to your configuration.yaml file:

```
- platform: ecoflow_iot
  app_key: 'APP_KEY'
  secret_key: 'SECRET_KEY'
  devices:
    - name: Ecoflow Max
      serial_number: 'SERIAL_NUMBER_1'
    - name: Ecoflow Mini
      serial_number: 'SERIAL_NUMBER_2'
```
Replace SERIAL_NUMBER_1 and SERIAL_NUMBER_2 with the serial numbers of the devices you want to monitor.

Restart Home Assistant.

## License
MIT License 2023