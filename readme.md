# Raspberry Pi 5 cooling system

The code works with the RGB Cooling HAT manufactured by Yahboom. The code provided by the company only works with the older raspberry pi like Raspberry Pi 3. It is mainly because of the deprecation of the [Adafruit_Python_GPIO](https://github.com/adafruit/Adafruit_Python_GPIO?tab=readme-ov-file) package. It is related to the OLED screen info display. I update the package to [Adafruit_Blinka](https://github.com/adafruit/Adafruit_Blinka). The code was tested on Raspberry Pi with Ubuntu 24.04 installed.


## Get started

We recommend creating a virtual environment for the dependencies and create a system service for automatic start fan cooling and information display.

```bash
python3 -m venv lab_venv
source lab_venv/bin/activate
pip install -r requirements.txt
```

Change the paths in the `fan_control.service` to your correct path and put the file under `/etc/systemd/system/fan_control.service`.

Then you can reload systemd to recognize the new service.

```bash
sudo systemctl daemon-reload
```

Enable the service to run at startup:

```bash
sudo systemctl enable fan_control.service
```

Start the service manually to test it.

```bash
sudo systemctl start fan_control.service
```

In our code, we will display the following information:
- CPU load percentage
- temperature
- RAM: used / total
- Disk: used / total
- wlan ip address

If everything runs correctly, you should be able to see the information displayed on the OLED screen and the fan should engage when the temperature is above 55 degrees celcius.

You can check the status with the following command.

```bash
sudo systemctl status fan_control.service
```

We display the system information using OLED display. We use the new adafruit_ssd1306 package. The idea will be something like the following. You can change the image content to other stuff that is important to you.

```python3
# Initialize the OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C, reset=None)
# ... more code to create the image
oled.image(image)
oled.show()
```