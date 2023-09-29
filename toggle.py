from machine import Pin
led1 = Pin(18, Pin.OUT)
sw5 = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
	if sw5.value() == 1:
		led1.toggle()