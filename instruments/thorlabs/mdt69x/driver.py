# Copyright (C) 2026 Paulo Felipe Jarschel
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

"""
Thorlabs MDT693B / MDT694B Piezo Controller Driver.
Pure Python — no ComfyLAB UI or block dependencies.
Communicates over Virtual COM / ASRL VISA resources.
"""

from typing import Any, Optional
from comfylab.devices.base import BaseInstrumentDriver, extract_float


class ThorlabsMDT69X(BaseInstrumentDriver):
    """
    Driver for Thorlabs MDT693B / MDT694B 3-Axis Piezo Voltage Controllers over VISA ASRL.
    """

    def set_voltage(self, axis: str = "X", voltage: float = 0.0) -> None:
        """Sets output piezo voltage (0 to 75V / 100V) for specified axis ('X', 'Y', or 'Z')."""
        axis_clean = axis.upper()
        if axis_clean not in ("X", "Y", "Z"):
            raise ValueError(f"Invalid axis: {axis}. Must be 'X', 'Y', or 'Z'.")
        self.write(f"{axis_clean.lower()}voltage={voltage}")

    def get_voltage(self, axis: str = "X") -> float:
        """Queries output piezo voltage for specified axis ('X', 'Y', or 'Z')."""
        axis_clean = axis.upper()
        if axis_clean not in ("X", "Y", "Z"):
            raise ValueError(f"Invalid axis: {axis}. Must be 'X', 'Y', or 'Z'.")
        res_str = self.query(f"{axis_clean.lower()}voltage?")
        return extract_float(res_str, default=0.0)

# @creator_identity: 3a61083b4c2ebce87fa7c250b3e64712a457315920952ce920dd8bd88509a022
# @signature: 20G5bLZVaP7C5nBxAJszcDObUqmPdf7ujMsPlI4NgJc7pgHKlmx7eV1mZx8moaPSaC9pa2hiaZIRU4j/XMxGAg==
