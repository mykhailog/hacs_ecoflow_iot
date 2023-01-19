# Ecoflow Portable Power Station Integration for Home Assistant 

<img width="461" alt="image" src="https://user-images.githubusercontent.com/1454659/213213276-073f4356-0e05-419b-b38c-1c8e76b1f0cd.png">

With this integration, you can keep track of your Ecoflow portable power station through Home Assistant by utilizing the official IoT cloud API. 

⚠️ This integration doesn't provide control over the battery, such as the ability to turn it on/off or adjust the power level.

 For more advanced functionality, you may want to consider using the [hassio-ecoflow  integration](https://github.com/vwt12eh8/hassio-ecoflow), which utilizes a local API.

## Installation

### HACS
If you use [HACS](https://hacs.xyz/) you can install and update this component.

1. Go into HACS -> CUSTOM REPOSITORIES and add url: https://github.com/mykhailog/hacs_ecoflow_iot with type "integration"
2. Go to integration, search "ecoflow_iot" and click *Install*.


## Configuration 
Please be aware that the `app_key` and `secret_key` are necessary for this integration to function properly and must be obtained from Ecoflow. To acquire these credentials, reach out to Ecoflow support at support@ecoflow.com and they will assist you. 

Additionally, the serial number of your Ecoflow device can be found on the back of the device.

Add the following to your `configuration.yaml` file:

```yaml
ecoflow_iot:
  app_key: 'APP_KEY'
  secret_key: 'SECRET_KEY'
  devices:
    - name: Device name
      serial_number: 'SERIAL_NUMBER_1'
```

Sample:

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




## License
MIT License 2023
