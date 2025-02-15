<img src="https://github.com/akestoridis/zigator/raw/27dfb2fa3022d7886bef3050c2637473bb4e5995/zigator-header.png">

# zigator

Zigator: Security analysis tool for Zigbee networks

<!-- START OF BADGES -->
![Status of tests workflow](https://img.shields.io/github/workflow/status/akestoridis/zigator/wf01-tests?label=tests)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/akestoridis/zigator)
![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/akestoridis/zigator/latest)
![Python version requirement](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
![License](https://img.shields.io/badge/license-GPL--2.0--only-blue)
<!-- END OF BADGES -->


## Disclaimer

Zigator is a software tool that analyzes the security of Zigbee networks, which is made available for benign research purposes only.
The users of this tool are responsible for making sure that they are compliant with their local laws and that they have proper permission from the affected network owners.


## Installation

You can install Zigator in a Python 3 virtual environment using pip as follows:
```console
$ git clone https://github.com/akestoridis/zigator.git
$ cd zigator/
$ python3 -m venv venv/
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install .
```

The following command should display the version of Zigator that you installed:
```console
(venv) $ zigator -v
```

If you get an error message that the `zigator` command was not found, make sure that your system's PATH environment variable includes the directory of the installed executable.
For example, if it was installed in `~/.local/bin`, add the following line at the end of your `~/.bashrc` file:
```bash
export PATH=$PATH:~/.local/bin
```

After reloading your `~/.bashrc` file, you should be able to find the `zigator` command.


## Features

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


## Getting Started

If you cannot capture your own Zigbee packets, you may use the pcap files of the [CRAWDAD dataset cmu/zigbee-smarthome](https://doi.org/10.15783/c7-nvc6-4q28) for your analysis.
More specifically, registered users of [CRAWDAD](https://crawdad.org) can download the following zip files:

* https://crawdad.org/download/cmu/zigbee-smarthome/sth3-room.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth2-room.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth3-duos.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth2-duos.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth3-house.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth2-house.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth3-trios.zip
* https://crawdad.org/download/cmu/zigbee-smarthome/sth2-trios.zip

Each of these zip files contains a pcap file of captured Zigbee packets and a text file that provides a description of the experimental setup and the keys that were used to encrypt and authenticate them.

You can view a synopsis of all the subcommands that Zigator supports as follows:
```console
(venv) $ zigator -h
```

The `-h` flag can also be used to view the supported arguments of different Zigator subcommands.
For example, the following command displays the supported arguments of the `inject` subcommand:
```console
(venv) $ zigator inject -h
```

Similarly, you can view the supported arguments of the `inject` subcommand for the forging of a beacon, before forwarding it for injection over UDP, with the following command:
```console
(venv) $ zigator inject udp beacon -h
```


## Publications

Zigator was used in the following publications:

* D.-G. Akestoridis and P. Tague, “HiveGuard: A network security monitoring architecture for Zigbee networks,” to appear in Proc. IEEE CNS’21.
* D.-G. Akestoridis, M. Harishankar, M. Weber, and P. Tague, “Zigator: Analyzing the security of Zigbee-enabled smart homes,” in *Proc. ACM WiSec’20*, 2020, pp. 77–88, doi: [10.1145/3395351.3399363](https://doi.org/10.1145/3395351.3399363).


## License

Copyright (C) 2020-2021 Dimitrios-Georgios Akestoridis

This project is licensed under the terms of the GNU General Public License version 2 only (GPL-2.0-only).
