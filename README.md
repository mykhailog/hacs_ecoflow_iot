# Ecoflow Power Stations Home Assistant Integration

<img width="461" alt="image" src="https://user-images.githubusercontent.com/1454659/213213276-073f4356-0e05-419b-b38c-1c8e76b1f0cd.png">


This integration allows you to monitor Ecoflow power stations state using Home Assistant.

It uses the Ecoflow IoT REST API to retrieve data from the devices and make it available in Home Assistant.


## Warning

This integration provides only basic information about Ecoflow devices and doesn't allow you to do any control like turn on or turn off sockets.

## Installation

### HACS
If you use [HACS](https://hacs.xyz/) you can install and update this component.

1. Go into HACS -> CUSTOM REPOSITORIES and add url: https://github.com/mykhailog/hacs_ecoflow_iot with type "integration"
2. Go to integration, search "ecoflow_iot" and click *Install*.




## Configuration 

It is important to note that the *app_key* and *secret_key* required for this integration to work need to be obtained from Ecoflow.

To get your *app_key* and *secret_key*, please contact Ecoflow support at support@ecoflow.com. They will provide you with the necessary credentials to use this integration. 

The serial number of your Ecoflow device is located on the back side of the device. 

Here is example of configuration.yaml file:

```yaml 

sensor:
  - platform: ecoflow_iot
    app_key: 'a8f5f167f44f4964e6c998dee827110c'  
    secret_key: 'a3dcb4d229de6fde0db5686dee47145d' 
    devices:
      - name: Ecoflow Max
        serial_number: 'R632ABZ3XAC21810'
      - name: Ecoflow Mini
        serial_number: 'R612DAD3AAC20292'
```

Restart Home Assistant.



## License
MIT License 2023
