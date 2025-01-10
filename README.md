# VPN Connector Application

This is a Flask-based web application with a simple UI for selecting a country and connecting to a VPN using OpenVPN. It supports any VPN provider that is compatible with OpenVPN.

---

## Features
- User-friendly UI for selecting a country.
- Simple integration with OpenVPN.
- Easy setup for VPN provider credentials.

---

## Requirements
- **OpenVPN** must be installed on your system.
- **Python 3.8+**

---

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Danielyilma/vpn.git
   cd vpn
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your VPN provider credentials:
   - Create a file named `auth.txt` in the root directory.
   - Add your credentials in the following format:
     ```
     username
     password
     ```

5. Start the Flask application:
   ```bash
   flask run
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

---

## How It Works
1. The application presents a list of countries to the user.
2. Upon selection, the application configures OpenVPN to connect to a server in the chosen country.
3. The credentials provided in `auth.txt` are used for authentication.

---

## Notes
- Ensure OpenVPN is installed and accessible via the command line.
- The `auth.txt` file must remain in the root directory for the application to access your credentials.
- The application does not store credentials permanently outside of the `auth.txt` file.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributions
Feel free to fork the repository, submit issues, or make pull requests to improve the application!

---

## Contact
For any questions or feedback, please contact the repository maintainer.

