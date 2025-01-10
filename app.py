from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import asyncio
import os
from _utils import list_config_files, get_config_filename_by_country_code, kill_vpn

app = Flask(__name__)
CORS(app)

vpn_process = None
VPN_STATUS = False
connected_country = None

countries = list_config_files("config")

@app.route('/')
def index():
    countries = list_config_files('config')
    return render_template('index.html', countries=countries, VPN_STATUS=VPN_STATUS, connected_country=connected_country)

@app.route('/connect', methods=['POST'])
async def connect():
    global vpn_process, VPN_STATUS, connected_country

    if VPN_STATUS:
        return jsonify(), 400
    data = request.get_json()
    country_code = data.get("country")
    auth_file = 'auth.txt'

    config_file, c_name = get_config_filename_by_country_code(country_code, countries)

    if not config_file:
        return jsonify({"status": "error", "message": "Configuration file not found"}), 400

    vpn_process = await asyncio.create_subprocess_exec(
        "sudo", "openvpn", "--config", f"config/{config_file}", "--auth-user-pass", auth_file,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    if vpn_process:
        VPN_STATUS = True
        connected_country = c_name
    print(VPN_STATUS)
    return jsonify({"status": "success"})

@app.route('/disconnect', methods=['POST'])
async def disconnect():
    global vpn_process, VPN_STATUS
    await kill_vpn(vpn_process)
    vpn_process = None
    VPN_STATUS = False
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
