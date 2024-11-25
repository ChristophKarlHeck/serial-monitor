import serial
import time
import argparse
import logging

# Configure argparse for command-line arguments
parser = argparse.ArgumentParser(description="Serial Monitor with optional logging.")
parser.add_argument(
    "-L",
    "--log",
    action="store_true",
    help="Enable logging to a file (serial_log.txt)",
)
parser.add_argument(
    "-p",
    "--port",
    type=str,
    default="/dev/serial0",
    help="Serial port to connect to (default: /dev/serial0)",
)
parser.add_argument(
    "-b",
    "--baudrate",
    type=int,
    default=115200,
    help="Baud rate for the serial connection (default: 115200)",
)
args = parser.parse_args()

# Configure logging if the -L option is passed
if args.log:
    LOG_FILENAME = "serial_log.txt"
    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

# Serial port configuration
port = args.port
baud_rate = args.baudrate

def log_and_print(message):
    """Logs a message if logging is enabled and prints it to the console."""
    if args.log:
        logging.info(message)  # Log the message to the file
    print(message)  # Always print the message to the console

while True:
    try:
        # Attempt to open the serial connection
        ser = serial.Serial(port, baud_rate, timeout=1)
        log_and_print(f"Connected to {port} at {baud_rate} baud.")
        
        while True:
            try:
                line = ser.readline().decode('utf-8', errors='replace').strip()
                if line:
                    log_and_print(repr(line))  # Log and print serial data
            except serial.SerialException as e:
                log_and_print(f"Serial read error: {e}")
                break  # Break inner loop to reconnect
    except serial.SerialException as e:
        log_and_print(f"Serial connection error: {e}")
    time.sleep(5)  # Wait before retrying
