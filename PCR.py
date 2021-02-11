#!/usr/bin/env python3
"""Helpful algorithms when working with PCR"""


def compute_melting_temperature(*args) -> float:
    """Calculate meltingpoint of DNA sequence

    Input-on-form: Arginine, Thymine, Guanine, Cytosine

    Raises:
        TypeError: If an argument isn't int or float
        ValueError: If not 4 input arguments

    Returns:
        float: Temperature of
    """
    for element in args:
        if not isinstance(element, (int, float)):
            raise TypeError("Only support int or float values")

    if len(args) != 4:
        raise ValueError("Require 4 arguments")

    A, T, G, C = args

    return float(2 * (A + T) + 4 * (G + C))
