######################################
#
# temperature
#
# testing modules
#
######################################
"""
This module contains functions for converting
temperatures between degrees F and degrees C
"""
def to_celsius(fahrenheit):
    """
    :param fahrenheit:
    :return: celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_farenheit(celcius):
    """
    :param celcius:
    :return: fahrenheit
    """
    farenheit = celcius * 9/5 + 32
    return farenheit

