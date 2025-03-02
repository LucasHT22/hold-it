from mq2 import MQ2
import utime

pin=26

sensor = MQ2(pinData = pin, baseVoltage = 3.3)

print("Calibrating")
sensor.calibrate()
print("Calibration completed")
print("Base resistance:{0}".format(sensor._ro))

while True:
    print("FART!!".format(sensor.readMethane())+" - ", end="")
    utime.sleep(0.5)
