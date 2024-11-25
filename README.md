# Serial Monitor
A simple Python-based tool for monitoring and logging serial port data with command-line options for Raspberry Pi.

## Features
- Monitor serial port data in real time.
- Optional logging to a file (`serial_log.txt`).
- Configurable serial port and baud rate.

## Requirements
- Python 3.6+
- `pyserial` library

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/ChristophKarlHeck/serial-monitor
   cd serial-monitor

2. `pip3 install -r requirements.txt`

3. `python3 log.py -p /dev/serial0 -b 9600 -L`
