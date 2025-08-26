"""
Utility functions for simulating a smart inverter (DER)
"""

def get_inverter_status():
    """Simulate reading the inverter's current status."""
    return {
        "power": 5000,  # Watts
        "voltage": 240, # Volts
        "status": "ON"
    }
