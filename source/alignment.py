#!/usr/bin/env python3
"""Algorithm implementation of different sequence alignment methods"""

import numpy

default = {
    "match": 1,
    "mismatch": -1,
    "gap": -2
}


def needleman_wunsch(*seq: str, **kwargs) -> numpy.ndarray:
    """A simple implementation of Needleman–Wunsch algorithm.

    Raises:
        ValueError: If more or less then two strings are given
        TypeError: If any element given to align isn't a string

    Returns:
        numpy.ndarray: Calculated alignment matrix
    """
    if len(seq) != 2:
        raise ValueError("Only support two strings to align.")

    for element in seq:
        if not isinstance(element, str):
            raise TypeError("Only support string values")

    kwargs = {**default, **kwargs}

    matrix = numpy.zeros([len(seq[0]) + 1, len(seq[1]) + 1], dtype=int)

    for index in range(1, len(seq[0]) + 1):
        matrix[index][0] = int(kwargs["gap"] * index)

    for jndex in range(1, len(seq[1]) + 1):
        matrix[0][jndex] = int(kwargs["gap"] * jndex)

    for index in range(1, len(seq[0])+1):
        for jndex in range(1, len(seq[1])+1):
            score_left = matrix[index][jndex-1]
            score_above = matrix[index-1][jndex]
            score_diagonal = matrix[index-1][jndex-1]

            if seq[0][index-1] == seq[1][jndex-1]:
                score_diagonal += kwargs["match"]
            else:
                score_diagonal += kwargs["mismatch"]

            score_left += kwargs["gap"]
            score_above += kwargs["gap"]

            score = int(max(score_left, score_above, score_diagonal))
            matrix[index][jndex] = score

    return matrix


def smith_waterman(*seq: str, **kwargs) -> numpy.ndarray:
    """A simple implementation of Smith–Waterman algorithm.

    Raises:
        ValueError: If more or less then two strings are given
        TypeError: If any element given to align isn't a string

    Returns:
        numpy.ndarray: Calculated alignment matrix
    """
    if len(seq) != 2:
        raise ValueError("Only support two strings to align.")

    for element in seq:
        if not isinstance(element, str):
            raise TypeError("Only support string values")

    kwargs = {**default, **kwargs}

    matrix = numpy.zeros([len(seq[0]) + 1, len(seq[1]) + 1], dtype=int)

    for index in range(1, len(seq[0]) + 1):
        matrix[index][0] = int(0)

    for jndex in range(1, len(seq[1]) + 1):
        matrix[0][jndex] = int(0)

    for index in range(1, len(seq[0])+1):
        for jndex in range(1, len(seq[1])+1):
            score_left = matrix[index][jndex-1]
            score_above = matrix[index-1][jndex]
            score_diagonal = matrix[index-1][jndex-1]

            if seq[0][index-1] == seq[1][jndex-1]:
                score_diagonal += kwargs["match"]
            else:
                score_diagonal += kwargs["mismatch"]

            score_left += kwargs["gap"]
            score_above += kwargs["gap"]

            score = int(max(score_left, score_above, score_diagonal, 0))
            matrix[index][jndex] = score

    return matrix
