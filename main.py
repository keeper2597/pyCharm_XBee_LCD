"""Implements a HD44780 character LCD connected via PCF8574T on I2C.
   This code was based on pyb_i2c_adafruit_lcd.py at https://github.com/dhylands/python_lcd/blob/master/lcd/pyb_i2c_adafruit_lcd_test.py"""

from machine import I2C, Pin
import utime
from xbee_i2c_adafruit_lcd import I2cLcd


DEFAULT_I2C_ADDR = 0x27

print("Running test_main")
i2c = I2C(1)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)
lcd.backlight_off()
utime.sleep_ms(250)
lcd.backlight_on()
utime.sleep_ms(250)
lcd.backlight_off()
utime.sleep_ms(250)
lcd.backlight_on()
utime.sleep_ms(250)
count = 0
lcd.move_to(0, 0)
lcd.custom_char(0, bytearray([0x0E,0x1B,0x11,0x11,0x11,0x11,0x11,0x1F]))  # 0% Empty
lcd.custom_char(1, bytearray([0x0E,0x1B,0x11,0x11,0x11,0x11,0x1F,0x1F]))  # 16%
lcd.custom_char(2, bytearray([0x0E,0x1B,0x11,0x11,0x11,0x1F,0x1F,0x1F]))  # 33%
lcd.custom_char(3, bytearray([0x0E,0x1B,0x11,0x11,0x1F,0x1F,0x1F,0x1F]))  # 50%
lcd.custom_char(4, bytearray([0x0E,0x1B,0x11,0x1F,0x1F,0x1F,0x1F,0x1F]))  # 66%
lcd.custom_char(5, bytearray([0x0E,0x1B,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F]))  # 83%
lcd.custom_char(6, bytearray([0x0E,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F]))  # 100% Full
lcd.custom_char(7, bytearray([0x0E,0x1F,0x1B,0x1B,0x1B,0x1F,0x1B,0x1F]))  # ! Error
for i in range(8):
    lcd.putchar(chr(i))
utime.sleep(3)
lcd.clear()
lcd.putstr("It Works!\nSecond Line\nThird\n")
while True:


    lcd.move_to(0,3)
    lcd.putstr("%4d" % (utime.ticks_ms() // 1000))
    # utime.sleep_ms(10000)
    #lcd.clear()
    #lcd.move_to(0, 0)
    #lcd.putstr("%7d" % (utime.ticks_ms() // 1000))
    # utime.sleep_ms(10000)

    # lcd.clear()
    # count += 1
    # if count % 10 == 3:
    #     print("Turning backlight off")
    #     lcd.backlight_off()
    # if count % 10 == 4:
    #     print("Turning backlight on")
    #     lcd.backlight_on()
    # if count % 10 == 5:
    #     print("Turning display off")
    #     lcd.display_off()
    # if count % 10 == 6:
    #     print("Turning display on")
    #     lcd.display_on()
    # if count % 10 == 7:
    #     print("Turning display & backlight off")
    #     lcd.backlight_off()
    #     lcd.display_off()
    # if count % 10 == 8:
    #     print("Turning display & backlight on")
    #     lcd.backlight_on()
    #     lcd.display_on()