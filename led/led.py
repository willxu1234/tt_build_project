import time
import RPi.GPIO as GPIO

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Number of LEDs.
PIXEL_COUNT = 160
PIXEL_ROW = 8
PIXEL_COL = 10

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

# Sets the colors of one side of the wood panel to red and everything else to green.
def one_side(pixels):
	for i in range(pixels.count()):
		if i % 20 <= 10:
			pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))
		else:
			pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 255, 0))
	pixels.show()

if __name__ == "__main__":
	pixels.clear()
	one_side(pixels)
