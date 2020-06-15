from waterSys import SDL_Adafruit_ADS1x15

def moisture_readout():
    
    ADS1115 = 0x01  # 16-bit ADC

    gain = 4096 # +/- 4.096v

    sps = 250 # 250 samples per second

    adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)

    Moisture_Raw = adc.readRaw(0, gain, sps)

    if(Moisture_Raw > 0x7FFF):
        Moisture_Raw = 0
    
    Moisture_Raw = Moisture_Raw / 64
    
    return round(Moisture_Raw, 2)
