#!/usr/bin/python3
"""This module defines a rebellious integer class MyInt."""


class MyInt(int):
    """A class representing a rebel
    integer that inverts == and != operators."""

    def __eq__(self, other):
        """Override == operator to behave as !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to behave as ==."""
        return super().__eq__(other)
