# Acunetix-API-Automation
Just a bunch of scripts for Acunetix automation ranging from downloading discovery data to running scans.

### main.py  ### 
Runs the main script and imports issues and discovery modules

### discovery.py  ### 
A module that makes an API call to Acunetix pulling down all the domains from the discovery, exports it into a .csv file. The script goes a little further and combines the domains into urls.

### issues.py  ### 
A module that pulls down all the issues for specific websites/groups.
