## import spidev

# Set up SPI communication
## spi = spidev.SpiDev()
## spi.open(0, 0)  # spi.open(bus, device)

    # MCP3008 command format: [start bit, single-ended/differential, channel number, 'don't care' bit]
# def read_potentiometer():
#     command = [1, (8 + 0) << 4, 0]
#     # Send the command and receive the response
# 
#     response = spi.xfer2(command)    # Extract the ADC value from the response
#     adc_value = ((response[1] & 3) << 8) + response[2]
# 
# 
#     # Convert the ADC value to a voltage (assuming 3.3V reference voltage)
#     voltage = adc_value * 3.3 / 1023
# 
#     # Return the voltage value
#     return voltage

# while True:
#    pot_value = read_potentiometer()
#    print("Potentiometer Value: {:.2f}V".format(pot_value))