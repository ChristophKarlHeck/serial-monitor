# Serial Monitor
A simple Python-based tool for monitoring and logging serial port data with command-line options for Raspberry Pi.

---

## Features

- **Real-Time Serial Monitoring**: Continuously reads and displays data from a specified serial port.
- **Optional Logging**: Logs the received data to `serial_log.txt` when the `--log` option is enabled.
- **Configurable Parameters**:
  - Serial port and baud rate are adjustable via command-line arguments.

---

## Requirements
- **Python**: Version 3.7 or later
- **Libraries**:
  - `pyserial`
  - `logging` (built-in)

Install the required library using pip:

```bash
pip install -r requirements.txt
```

## Usage
### Command-Line Arguments

| **Argument**      | **Required** | **Description**                                                      |
|--------------------|--------------|----------------------------------------------------------------------|
| `-p`, `--port`     | No           | Serial port to connect to (default: `/dev/serial0`).                |
| `-b`, `--baudrate` | No           | Baud rate for the serial connection (default: `115200`).            |
| `-L`, `--log`      | No           | Enable logging to a file (`serial_log.txt`).                        |

## Example Commands
### Monitor Serial Port without Logging
```bash
python3 serial_monitor -p /dev/serial0 -b 115200 
```
### Monitor Serial Port with Logging
```bash
python3 serial_monitor -p /dev/serial0 -b 115200 -L
```

## How It Works

1. **Connect to the Serial Port**:
   - Opens a connection to the specified serial port at the given baud rate.
   - Automatically retries the connection every 5 seconds if an error occurs.

2. **Read and Display Data**:
   - Continuously reads data from the serial port line by line.
   - Prints the received data to the console.

3. **Optional Logging**:
   - If the `--log` option is enabled, all received data is logged to `serial_log.txt`.
   - Logs include timestamps for each line of data.

4. **Error Handling**:
   - Handles errors in serial communication gracefully by reconnecting after a delay.

