# Copyright (C) 2020-2021 Dimitrios-Georgios Akestoridis
#
# This file is part of Zigator.
#
# Zigator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 only,
# as published by the Free Software Foundation.
#
# Zigator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zigator. If not, see <https://www.gnu.org/licenses/>.

"""
Zigator: Security analysis tool for Zigbee networks
===================================================

Disclaimer
----------

Zigator is a software tool that analyzes the security of Zigbee networks,
which is made available for benign research purposes only. The users of this
tool are responsible for making sure that they are compliant with their local
laws and that they have proper permission from the affected network owners.

Features
--------

Zigator enables its users to do the following:

* Derive preconfigured Trust Center link keys from install codes
* Decrypt and verify Zigbee packets
* Encrypt and authenticate Zigbee packets
* Parse almost all the header fields of Zigbee packets up to the APS layer
* Infer information from captured Zigbee packets
* Produce statistics from a database of Zigbee packets
* Visualize data from a database of Zigbee packets
* Train decision tree classifiers from a database of Zigbee packets
* Inject forged packets over UDP and SLL
* Launch selective jamming and spoofing attacks with an ATUSB
* Deploy stand-alone WIDS sensors


License
-------

Copyright (C) 2020-2021 Dimitrios-Georgios Akestoridis

This project is licensed under the terms of the GNU General Public License
version 2 only (GPL-2.0-only).
"""

import os

from . import (
    cli,
    config,
)
from ._metadata import (
    __author__,
    __author_email__,
    __classifiers__,
    __copyright__,
    __description__,
    __entry_points__,
    __install_requires__,
    __keywords__,
    __license__,
    __python_requires__,
    __title__,
    __url__,
)
from ._version import get_version
from .main import main

__version__ = get_version(os.path.dirname(os.path.abspath(__file__)))
__all__ = ["main"]

cli.init(__version__)
config.init(__version__)
