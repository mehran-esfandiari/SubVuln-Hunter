# SubVuln Hunter






![Image](https://github.com/users/mehran-esfandiari/projects/1/assets/165242715/f7def240-ab2d-40b2-bbfc-c3b0c3628edd)






## VirusTotal Subdomain Finder and Nuclei Scanner
This project is an automated tool designed to find subdomains associated with IP addresses using the VirusTotal API and scan them for vulnerabilities with Nuclei.

## Features

- Subdomain Discovery: Retrieves subdomains associated with IP addresses from VirusTotal.
- Vulnerability Scanning: Uses Nuclei to scan discovered subdomains for known vulnerabilities.
- Batch Processing: Handles multiple IP addresses read from a file.
- Customizable Threads: Allows users to specify the number of threads for Nuclei scans.

## Prerequisites

- Python 3.x
- requests module
- [Nuclei](https://github.com/projectdiscovery/nuclei)

## Installation
1. Clone the Repository:

   ```sh
    git clone https://github.com/mehran-esfandiari/SubVuln-Hunter.git
    cd SubVuln-Hunter

2. Set Up Virtual Environment and Install Dependencies:

   ```sh

    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
3. Configure Your VirusTotal API Key:

- Replace the placeholder YOUR_API_KEY_HERE in the script with your actual VirusTotal API key.

## Usage
1. Prepare the IP List:

- Create a hosts.txt file containing a list of IP addresses to scan, one per line.

2. Run the Script:

   ```sh
    python SubVuln-Hunter.py
3. Input the Number of Threads:
- When prompted, enter the number of threads to use for the Nuclei scan.

## Disclaimer ❗
This project is intended for educational and research purposes only. The author does not condone or support any illegal activities and will not be held responsible for any misuse of this code. Users are solely responsible for ensuring that their use of this project complies with all applicable laws and regulations.

## License
This project is licensed under the MIT License - see the [LICENSE ](url)file for details.