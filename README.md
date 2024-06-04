# Twitch API Data Pipeline to PostgreSQL Database

This project is a Python script that fetches data from the Twitch API using RapidAPI and inserts it into a PostgreSQL database. It demonstrates how to interact with an external API, parse JSON data, establish a connection to a PostgreSQL database, and perform data insertion.

## Setup

1. **Install Dependencies**:
   - Ensure you have Python installed on your system.
   - Install the required Python packages using `pip`:
     ```
     pip install requirements.txt
     ```

2. **Configure PostgreSQL Database**:
   - Install PostgreSQL on your system if you haven't already.
   - Create a new PostgreSQL database and note down the database name, username, password, host, and port.
   - Update the database connection parameters in the Python script (`main.py`) with your PostgreSQL credentials.

3. **Obtain RapidAPI Key**:
   - Sign up for an account on RapidAPI (https://rapidapi.com/).
   - Subscribe to the Twitch API on RapidAPI and obtain the API key.
   - Update the API key in the Python script (`main.py`).

## Installation
To create a virtual environment in the project directory, use the following command:  
`python -m venv venv`

Activate the virtual environment using the appropriate command for your operating system:  
Windows OS:  
`venv\Scripts\activate`  
mac OS:  
`source venv/bin/activate`

Install python packages:  
`pip install -r requirements.txt`

## Usage 
To run the script, use the following command:  
`python main.py`

## Usage
1. **Run the Script**:
   - Execute the Python script `main.py`.
   - This script will make a request to the Twitch API, fetch data for the specified channel, write it to a JSON file, and insert it into the PostgreSQL database.

2. **Verify Data**:
   - Use your preferred method to verify that the data has been successfully inserted into the PostgreSQL database:
     - Command-Line Interface (CLI)
     - Graphical User Interface (GUI)
     - Python Script

## Troubleshooting

- If you encounter any issues with the script, ensure that:
  - Your PostgreSQL credentials are correct.
  - The PostgreSQL server is running.
  - RapidAPI key is valid and authorized to access the Twitch API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
