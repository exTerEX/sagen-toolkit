#!/usr/bin/env python3


def valid(sequence: str, bases: list = ("A", "T", "G", "C")) -> bool:
    """Check if sequence only contain bases.

    Args:
        sequence (str): Sequence to check
        bases (list, optional): Valid bases. Defaults to ("A", "T", "G", "C").

    Raises:
        TypeError: If sequence isn't string
        TypeError: If bases isn't a list or tuple
        TypeError: If a base isn't a strings
        ValueError: If a base in bases are longer then 1

    Returns:
        bool: True if sequence is valid (only containing bases)
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be str")

    if not isinstance(bases, (list, tuple)):
        raise TypeError("Bases must be list or tuple")

    for base in bases:
        if not isinstance(base, str):
            raise TypeError("Bases must contain strings")
        if len(base) != 1:
            raise ValueError("Bases must have length of 1")

    for base in sequence:
        if base not in bases:
            return False

    return True


def ratios(sequence: str, bases: list = ("A", "T", "G", "C")) -> tuple:
    """Find ratio of nucleobases in sequence.

    Args:
        sequence (str): Sequence to be checked
        bases (list, optional): Bases to be counted. Defaults to ("A", "T", "G", "C").

    Raises:
        TypeError: If sequence isn't string
        TypeError: If bases isn't a list or tuple
        TypeError: If a base isn't a strings
        ValueError: If a base in bases are longer then 1

    Returns:
        tuple: Tuple with ratios on same form as bases
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be str")

    if not isinstance(bases, (list, tuple)):
        raise TypeError("Bases must be list or tuple")

    for base in bases:
        if not isinstance(base, str):
            raise TypeError("Bases must contain strings")
        if len(base) != 1:
            raise ValueError("Bases must have length of 1")

    ratio = {base: 0 for base in bases}

    for base in sequence:
        ratio[base] += 1 / len(sequence)

    return tuple(ratio.values())


def kmers(sequence: str, k: int) -> tuple:
    """Find k-mers of sequence

    Args:
        sequence (str): Sequence to be subsequenced
        k (int): Length of subsequences

    Raises:
        TypeError: If sequence isn't string
        ValueError: If k is bigger then sequence
        TypeError: If k isn't int

    Returns:
        tuple: [description]
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be str")

    if k > len(sequence):
        raise ValueError("k cannot be longer then the sequence")

    if not isinstance(k, int):
        raise TypeError("k must be int")

    kms = [sequence[i:i + k] for i in range(0, len(sequence) - k + 1)]

    return tuple(kms)
