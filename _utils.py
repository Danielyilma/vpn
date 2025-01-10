import os 

def list_config_files(directory):
    """List available OpenVPN configuration files in a directory."""
    countries = []
    for filename in os.listdir(directory):
        if filename.endswith(".ovpn"):
            country_code = filename.split('-')[0]
            country_name = {
                "us": "United States",
                "ca": "Canada",
                "uk": "United Kingdom",
                "de": "Germany",
                "jp": "Japan",
                "nl": "Netherlands"
            }.get(country_code, "Unknown")
            countries.append((country_code, country_name, filename))
    return countries

def get_config_filename_by_country_code(country_code, countries):
    for code, name, filename in countries:
        if code == country_code:
            return filename, name
    return None, None

async def kill_vpn(proc):
    if proc:
        try:
            proc.kill()
            await proc.wait()
            print("VPN forced to disconnect.")
        except Exception as e:
            print(f"Error while disconnecting: {e}")