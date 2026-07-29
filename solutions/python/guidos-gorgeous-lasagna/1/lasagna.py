"""Functions for baking Guido's gorgeous lasagna.

Useful constants and functions to allow the user to easily 
calculate baking times, preparation times, and total elapsed times.
"""

# Не забудь проверить, что эта константа у тебя определена в самом верху:
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes) based on 2 minutes per layer.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
