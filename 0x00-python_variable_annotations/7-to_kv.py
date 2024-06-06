#!/usr/bin/env python3
"""Type-annotated to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple - float and string """
    x = v ** 2
    return (k, x)
