# Traffic Light Control System for Raspberry Pi

This project is a traffic light control system implemented using a Raspberry Pi and the Python `RPi.GPIO` library. It manages traffic lights at four junctions based on user-provided traffic intensities.

## Features

- Controls LEDs connected to GPIO pins of the Raspberry Pi to simulate traffic lights.
- Adjusts the duration of green light based on traffic intensity.
- Provides a simple traffic light pattern for demonstration.

## Components

- **Raspberry Pi** (any model with GPIO pins)
- **LEDs** (for traffic light simulation)
- **Resistors** (to limit current through LEDs)
- **Breadboard** and **Jumper Wires**

## Installation

1. **Set up Raspberry Pi:**

   - Ensure you have Raspbian (or any compatible OS) installed on your Raspberry Pi.
   - Ensure your system is updated:
     ```bash
     sudo apt-get update
     sudo apt-get upgrade
     ```

2. **Install the `RPi.GPIO` library:**
   The library is usually pre-installed. If not, install it using:
   ```bash
   sudo apt-get install python3-rpi.gpio
   ```

3. **Clone this repository:**
   ```bash
   git clone https://github.com/Gunjit27/Automated_Traffic_Light.git
   ```

4. **Navigate to the project directory:**
   ```bash
   cd Automated_Traffic_Light
   ```

## Usage

1. **Connect LEDs to GPIO pins:**

   - **Junction A:** GPIO 14, GPIO 15, GPIO 18
   - **Junction B:** GPIO 23, GPIO 24, GPIO 25
   - **Junction C:** GPIO 8, GPIO 7, GPIO 1
   - **Junction D:** GPIO 16, GPIO 20, GPIO 21

   Connect each LED to the corresponding GPIO pin and a ground pin through a resistor.

2. **Run the script:**

   Execute the script to start the traffic light control system:
   ```bash
   python3 traffic_light_control.py
   ```

3. **Provide traffic intensity:**

   - When prompted, enter the traffic intensity (an integer value) for each junction.

   Example:
   ```
   Enter traffic intensity for Junction A: 50
   Enter traffic intensity for Junction B: 30
   Enter traffic intensity for Junction C: 10
   Enter traffic intensity for Junction D: 20
   ```

## Script Overview

- **`light(pins)`**: Controls the LEDs connected to the specified pins to show a traffic light pattern.
- **`compute_green_time(intensity)`**: Calculates the green light duration based on traffic intensity.
- **`perform_lighting(A, B, C, D)`**: Manages the lighting sequence based on the provided traffic intensities.

## GPIO Pin Mappings

| Junction | GPIO Pins        |
|----------|------------------|
| A        | 14, 15, 18       |
| B        | 23, 24, 25       |
| C        | 8, 7, 1          |
| D        | 16, 20, 21       |
