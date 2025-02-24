# PowerData

This project provides Python scripts for exporting data from MPP Solar inverters to custom locations, such as EmonCMS or other custom data sinks, leveraging the `mpp-solar` software.

## Description

This repository contains tools and scripts to collect data from MPP Solar inverters and forward it to user-defined destinations. It focuses on flexibility and allows for integration with various data logging and monitoring systems.

**Key Features:**

* Data retrieval using `mpp-solar`.
* Customizable data formatting and export.
* Support for exporting to EmonCMS (example provided).
* Extensible architecture for adding support for other data destinations.
* Focus on real-time data forwarding.

## Prerequisites

Before running the scripts, ensure you have the following installed:

* **Python 3.6+:** Python is required to run the scripts.
* **`mpp-solar`:** This software is essential for communicating with your MPP Solar inverter. Install it according to its documentation.
    * You can install it via pip: `pip install mpp-solar`
* **Python Libraries:** Install the required Python libraries using pip:

    ```bash
    pip install requests mpp-solar json subprocess
    ```

    You may need to add additional libraries depending on the exact scripts you use, and if you are using a new endpoint/data destination.
* **MPP Solar Inverter:** Obviously, you need an MPP Solar inverter.
* **Connection to Inverter:** You must have your sbc/computer/pi connected to your MPP Solar inverter, usually via USB, serial or Bluetooth.
* **Target Data Destination:** You'll need an account and API credentials (if applicable) for your target data destination (e.g., EmonCMS, InfluxDB, PythonAnywhere, etc.).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/nkhearn/PowerData.git
    cd PowerData
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install requests mpp-solar
    ```

## Usage

1.  **Configure `mpp-solar`:** Ensure `mpp-solar` is correctly configured to communicate with your inverter. Refer to the `mpp-solar` documentation for configuration instructions.

2.  **Configure the export script:**
    * Edit the Python script (e.g., `export_to.py`) to set the necessary parameters, such as your API key, EmonCMS URL, node ID, and data field mappings.
    * If exporting to a different platform, you will need to create a new python file, and use the requests library, or other appropriate library, to send the data.

3.  **Run the Python script:**

    * Example (assuming a script called `export_to.py`):

        ```bash
        python export_to.py
        ```

4.  **Verify the data:** Check your target data destination to ensure the data is being received correctly.

## Example Scripts

* **`export_to.py`:** Exports MPP Solar inverter data to EmonCMS and other locations. This script serves as an example and can be adapted for other platforms.

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new data destination integration, please open an issue or submit a pull request.

## Author

nkhearn
