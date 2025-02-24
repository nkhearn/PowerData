import subprocess
import requests
import json

NODE = "Inverter"
MPP_SOLAR_PATH = "/home/pi/.local/bin/mpp-solar"

# Analogue sensor script, outputs a numeric value.
ADC_PATH = "/home/pi/adc.py"

HOST = "127.0.0.1"
PROTOCOL = "http"
GETURL = "input/post"
APIKEY = ""

EMON_URL = f"{PROTOCOL}://{HOST}/{GETURL}"
MD_URL = "https://trigger.macrodroid.com/[UUID]/power"
PYA_URL = "https://[username].eu.pythonanywhere.com/store/"

try:
    # Get JSON data from mpp-solar
    mpp_solar_process = subprocess.run(
        [MPP_SOLAR_PATH, "-p", "/dev/hidraw0", "-c", "QPIGS", "-o", "json", "--exclfilter", "command"],
        capture_output=True,
        text=True,
        check=True,
    )
    JSONDATA = mpp_solar_process.stdout.strip()
    data_dict = json.loads(JSONDATA) # load the json data into a dictionary

    # Optionally include data from an analogue sensor
    # Get PV value from adc.py
    adc_process = subprocess.run(
        ["python", ADC_PATH], capture_output=True, text=True, check=True
    )
    PV = adc_process.stdout.strip()

    # Merge PV data into the existing JSON dictionary
    data_dict["PV1"] = int(PV)
    merged_json = json.dumps(data_dict) # convert back to json

    # Send merged JSON data to the EMON URL
    data1 = {"node": NODE, "apikey": APIKEY, "data": merged_json}
    requests.post(EMON_URL, data=data1)

    # Send merged JSON data to the PythonAnywhere URL with JSON content type
    headers = {"Content-Type": "application/json"}
    requests.post(PYA_URL, data=merged_json, headers=headers)

    # Send merged JSON data to the MacroDroid URL using wget equivalent
    requests.get(f"{MD_URL}?DATA={merged_json}")

except subprocess.CalledProcessError as e:
    print(f"Error executing subprocess: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error making HTTP request: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
