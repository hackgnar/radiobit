from microbit import *
import radio

radio.on()
#radio.config(data_rate=radio.RATE_250KBIT, channel=74)
radio.config(data_rate=radio.RATE_1MBIT, channel=74, raw=1)
#radio.config(data_rate=radio.RATE_2MBIT, channel=74)
#radio.ble()
radio.sniff_on()

while True:
    for i in range(100):
        radio.config(channel=i)
        pkt = radio.sniff()
        if pkt is not None:
            data = ' '.join(['%02x'%c for c in pkt])
            print(data)
            del data
        del pkt
