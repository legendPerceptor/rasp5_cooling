# Raspberry Pi 5 cooling system

The code works with the RGB Cooling HAT manufactured by Yahboom. The code provided by the company only works with the older raspberry pi like Raspberry Pi 3. It is mainly because of the deprecation of the [Adafruit_Python_GPIO](https://github.com/adafruit/Adafruit_Python_GPIO?tab=readme-ov-file) package. It is related to the OLED screen info display. I update the package to [Adafruit_Blinka](https://github.com/adafruit/Adafruit_Blinka). The code was tested on Raspberry Pi with Ubuntu 24.04 installed.


```python3
# Initialize the OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C, reset=None)
# ... more code to create the image
oled.image(image)
oled.show()
```