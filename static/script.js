document.addEventListener('DOMContentLoaded', function() {
    const vpnToggle = document.getElementById('vpn-toggle');
    const statusText = document.getElementById('status-text');
    const statusIndicator = document.getElementById('status-indicator');
    const countrySelect = document.getElementById('country-select');

    vpnToggle.addEventListener('change', function() {
        const selectedCountry = countrySelect.value;
        if (!selectedCountry) {
            alert('Please select a country before connecting.');
            vpnToggle.checked = false;
            return;
        }

        if (this.checked) {
            request("http://localhost:5000/connect", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ country: selectedCountry })
            }, "Connected");
        } else {
            request("http://localhost:5000/disconnect", {method: 'POST'}, "Disconnected");
        }
    });

    countrySelect.addEventListener('change', function() {
        if (this.value) {
            console.log(`Selected country: ${this.options[this.selectedIndex].text}`);
        }
    });

    async function request(url, data, status) {
        const response = await fetch(url, data);

        // const resdata = await response.json();
        if (response.status == 200) {
            vpnToggle.checked = status === 'Connected' ? true : false;
            console.log(vpnToggle.checked)
            statusText.textContent = status;
            statusIndicator.style.backgroundColor = status === 'Connected' ? "green" : "red";
        } else {
            vpnToggle.checked = status === 'Connected' ? false : true;
            alert('request failed');
        }
    }

});


