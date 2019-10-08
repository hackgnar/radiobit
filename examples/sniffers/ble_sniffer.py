from microbit import *
import radio

radio.on()
radio.config(channel=38)
radio.ble()

while True:
    for i in range(100):
        radio.config(channel=i)
        pkt = radio.receive_bytes()
        if pkt is not None:
            data = ' '.join(['%02x'%c for c in pkt])
            print(data)
            del data
        del pkt
