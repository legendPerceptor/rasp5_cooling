import board
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Define the Reset Pin
# oled_reset = digitalio.DigitalInOut(board.D4)

# Initialize the I2C bus
i2c = board.I2C()

# Initialize the OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=None)

# Clear the display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
width = oled.width
height = oled.height
image = Image.new("1", (width, height))

# Get drawing object to draw on the image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

# Draw some text.
text = "Hello, Raspberry Pi 5!"
# Calculate text size using getbbox
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Position the text in the center of the display
x = (width - text_width) // 2
y = (height - text_height) // 2
draw.text((x, y), text, font=font, fill=255)

# Display image.
oled.image(image)
oled.show()
