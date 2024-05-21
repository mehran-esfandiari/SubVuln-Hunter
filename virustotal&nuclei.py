import requests
import json
import re
import os

print("""
   _____       __  _    __      __         __  __            __           
  / ___/__  __/ /_| |  / /_  __/ /___     / / / /_  ______  / /____  _____
  \__ \/ / / / __ \ | / / / / / / __ \   / /_/ / / / / __ \/ __/ _ \/ ___/
 ___/ / /_/ / /_/ / |/ / /_/ / / / / /  / __  / /_/ / / / / /_/  __/ /    
/____/\__,_/_.___/|___/\__,_/_/_/ /_/  /_/ /_/\__,_/_/ /_/\__/\___/_/     
                                                                      
                                                   Created by Mehran-Esfandiari

""")

threads = input("Enter the number of threads for nuclei: ")

# Define the URL for the VirusTotal IP address report API
url = "https://www.virustotal.com/vtapi/v2/ip-address/report"

# Define your VirusTotal API key
api_key = "Your API"

# Read IP addresses from the hosts.txt file
with open("hosts.txt", "r") as file:
    ip_addresses = [ip.strip() for ip in file.readlines()]

# Set headers for the HTTP request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*"
}

# Create the results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Iterate over each IP address to get the report from VirusTotal
for ip_address in ip_addresses:
    # Set parameters for the API request
    params = {
        'apikey': api_key,
        'ip': ip_address
    }

    # Make the GET request to the VirusTotal API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if the hostname field is present in the response
        if 'hostname' in str(data):
            # Extract subdomains using regex
            sub_domains = re.findall(r"'hostname': '([^']+)'", str(data))

            # Create a directory for the current IP address
            ip_dir = os.path.join("results", ip_address.replace('.', '-'))
            os.makedirs(ip_dir, exist_ok=True)

            # Save the subdomains to a file
            with open(os.path.join(ip_dir, "Subdomains.txt"), "a") as file:
                for sub_domain in sub_domains:
                    file.write(sub_domain + "\n")

            # Append the valid IP address to Valid-Hosts.txt
            with open("Valid-Hosts.txt", "a") as file:
                file.write(ip_address + "\n")
            print(f"Sub-domains for IP {ip_address} saved.")

            # Run nuclei to scan for vulnerabilities on the subdomains
            nuclei_command = f"nuclei -l {os.path.join(ip_dir, 'Subdomains.txt')} -as -c {threads}  -o {os.path.join(ip_dir, 'Vulnerable-Subdomain.txt')}"
            os.system(nuclei_command)
        else:
            # Log the IP address as invalid if no hostname is found
            print(f"No hostname found in the response for IP {ip_address}.")
            with open("Invalid-Hosts.txt", "a") as file:
                file.write(ip_address + "\n")
    else:
        # Print an error message if the request failed
        print(f"Failed to retrieve data for IP {ip_address}. Status code:", response.status_code)
