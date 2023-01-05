import requests
import csv
import numpy as np
import datetime
from datetime import date
import os
import pandas as pd
import matplotlib.pyplot as plt


today = date.today()
prevMon = today - datetime.timedelta(days=90)
day = today.strftime("%d_%m_%Y")

"Creates a graphical "

def mgmt_rp(bu_option):
    headers = {
        'Accept': 'application/json',
    }

    params = {
        'csvSeparator': 'Comma',
        'severity': ' ',
        'websiteGroupName': bu_option,
        'webSiteName': ' ',
        'startDate': prevMon,
        'endDate': today,
    }

    response = requests.get( response = requests.get('ACUNETIX_API_URL', params=params,
                            headers=headers)

   
    if response.status_code == 200:
        file_name = '{bu}_mgmt_{day}.csv'.format(bu=bu_option, day=day)          
        file_path = "FILE_PATH"
        file = os.path.join(file_path, file_name)
      
        with open(file, 'w', newline='') as csv_file:
            content = csv_file.write(response.text)
            csv_file.close()
        mk_grph(file)

    


"Creates a CSV file for issues found in Acunetix and saves it to your local drive"

def dev_rp(bu_option):
    headers = {
        'Accept': 'application/json',
    }

    params = {
        'csvSeparator': 'Comma',
        'severity': ' ',
        'websiteGroupName': bu_option,
        'webSiteName': ' ',
        'startDate': prevMon,
        'endDate': today,
    }
       response = requests.get( response = requests.get('ACUNETIX_API_URL', params=params,
                            headers=headers)

    if response.status_code == 200:
        file_name = '{bu}_devrpt_{day}.csv'.format(bu=bu_option, day=day)        
        file_path = "FILE_PATH"
        file = os.path.join(file_path, file_name)
      
        with open(file, 'w', newline='') as csv_file:
            content = csv_file.write(response.text)
            csv_file.close()
        print("Check your folder")
            
    else:
        print(response.status_code)


def mk_grph(ex_file):
    
    #Initialize the lists for X and Y axis
    data = pd.read_csv(ex_file)

    df = pd.DataFrame(data)

    site_col = list(df.iloc[:, 3])
    sev_col = list(df.iloc[:, 1])

    # returns dictionaries of columns 1 and 3; key:value pair for sev data is severity and severity count
    # site list is site and site count
    sev_data = countOccurance(sev_col)
    site_list = countOccurance(site_col)

    # returns the severity types
    sev_axis = list(sev_data.keys())
    
    # returns the count for severity types
    sev_yaxis = list(sev_data.values())
    
    #returns count for severity    
    sites = list(site_list.keys())

    x_axis = np.arange(len(sites))
    
    #Plot the data using bar() method
 #   plt.xticks(x_axis,sites)
    plt.bar(sev_axis, sev_yaxis, color='maroon')
    plt.title("Management Report")
    plt.xlabel("Sites")
    plt.ylabel("No. of Vulnerabilities")
  
    #Show the plot
    plt.show()
   



def countOccurance(axPoints):
    count_dict = {}
    for value in axPoints:
        if value in count_dict:
            count_dict[value] +=1
        else:
            count_dict[value] =1
    return count_dict

