import RPi.GPIO as GPIO
import time

# Set up GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pin mappings for each junction
pins = {
    'A': [14, 15, 18],
    'B': [23, 24, 25],
    'C': [8, 7, 1],
    'D': [16, 20, 21]
}

# Set up each pin as an output
for pin_set in pins.values():
    for pin in pin_set:
        GPIO.setup(pin, GPIO.OUT)

# Initialize all LEDs to red (last pin in each set)
for pin_set in pins.values():
    GPIO.output(pin_set[-1], GPIO.HIGH)

def light(pins):
    """
    Control the LEDs connected to the given pins with a specific light pattern.
    
    Args:
        pins (list): List of GPIO pins to control. The list should contain three pins.
    """
    # Set the pattern for the LEDs
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)
    time.sleep(2)
    
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.LOW)
    time.sleep(1)
    
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.LOW)
    time.sleep(1)
    
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)

def compute_green_time(intensity):
    """
    Compute the duration the light should stay green based on traffic intensity.
    
    Args:
        intensity (int): Traffic intensity of the junction.
    
    Returns:
        float: Duration (in seconds) for the light to stay green.
    """
    # Example function: the light stays green for intensity / 10 seconds.
    # You can adjust this function based on your specific requirements.
    return intensity / 10.0

def perform_lighting(A, B, C, D):
    """
    Perform lighting sequences based on the traffic intensity of each junction.
    
    Args:
        A (int): Traffic intensity for Junction A.
        B (int): Traffic intensity for Junction B.
        C (int): Traffic intensity for Junction C.
        D (int): Traffic intensity for Junction D.
    """
    # Keep track of traffic intensities in a dictionary
    intensities = {'A': A, 'B': B, 'C': C, 'D': D}
    
    while any(intensities[junction] > 0 for junction in intensities):
        # Determine the junction with the highest intensity
        max_junction = max(intensities, key=intensities.get)
        max_intensity = intensities[max_junction]
        
        # Light the junction with the highest intensity
        light(pins[max_junction])
        print(f"{max_junction} - intensity: {max_intensity}")

        # Compute the duration the light should stay green
        green_time = compute_green_time(max_intensity)
        time.sleep(green_time)
        
        # Simulate processing of cars
        # Decrease the traffic intensity based on the green time
        # Example: if green time is 10 seconds, assume 10 cars were processed
        # Adjust this logic based on your specific requirements
        processed_cars = green_time * 10  # Assuming 10 cars per second
        intensities[max_junction] = max(0, intensities[max_junction] - processed_cars)
    
    print("All done")

# Get user input for traffic intensity
A = int(input("Enter traffic intensity for Junction A: "))
B = int(input("Enter traffic intensity for Junction B: "))
C = int(input("Enter traffic intensity for Junction C: "))
D = int(input("Enter traffic intensity for Junction D: "))

# Perform lighting based on user input
perform_lighting(A, B, C, D)

# Clean up GPIO settings to reset pins to default state
GPIO.cleanup()
