# Acunetix-API-Automation
Just a bunch of scripts for Acunetix automation ranging from downloading discovery data to running scans.

### acunetix_csv_discovery_dump.py  ### 
A script that makes an API call to Acunetix pulling down all the domains from the discovery, exports it into a .csv file. The script goes a little further and combines the domains into urls.

 ***NEXT STEPS:*** 
  - [ ] Automatically run scripts on monthly basis (figure out a day)
  - [ ] Remvoe old domains and archive them in txt file to validate w/ teams
  - [ ] Ensure all domains have an IP address associated if not look it up and populate column with IP addresses
    - [ ] check to see what IP addresses are active
