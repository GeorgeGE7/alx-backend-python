#!/usr/bin/env python3
"""Type-annotated make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier function return lambda"""
    return lambda x: x * multiplier
