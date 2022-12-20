import requests
import csv
from datetime import date
import os

today = date.today()
day = today.strftime("%d_%m_%Y")

"""
Method to combine domain strings from the csv file
"""
def concat_domain(list_of_rows):
    start_of_list = list_of_rows[0]
    "remove the headers row of the csv file from the list"
    headerless_list = list_of_rows[1:]

    "Iterate through the row list without the headers"
    for row in headerless_list:
        "Get the domains of each list"
        domains = row[:5]
        "concat broken domain text"
        row.insert(0, ''.join(domains))
        "remove the broken up domain elements from list"
        for item in domains:
            row.remove(item)
    "Add headers back to list and return list"
    return start_of_list + headerless_list



"""
Add periods to concatenate domains
"""
def add_period(rowlist):
    """remove the header from the lists and update to match the later format """
    start_of_list = rowlist[0]
    new_header_list = update_headers(start_of_list)

    "Separate the rest of the headers"
    rest_of_rows = rowlist[1:]

    """
    insert periods after index [1] and index [3]" 
    first iterate through the list of rows (which are also in a list)

    """
    for row in rest_of_rows:
        "insert periods at the different index [0] and [3] of each row list"
        row.insert(1, '.')
        row.insert(3, '.')
    "Add the headers back to the list and return the updated list with periods"
    return new_header_list + rest_of_rows



def update_headers(headerlist):

    "remove unneccessary headers from csv file"
    headerlist.remove('Second Level Domain')
    headerlist.remove('Top Level Domain')
    headerlist.remove('Copyright')
    headerlist.remove('Distance')
    headerlist.remove('Tags')
    return headerlist



lines_in_csv = []
"""
Pull down the csv file from Acunetix using credentials 
and API endpoint Parameters specify what type of file 
to save data as

"""
def pull_discovery():
    params = {
        'csvSeparator': 'Comma',
    }
    response = requests.get('ACUNETIX_API_URL', params=params,
                            auth=(USERID,TOKEN))

    "If the authentication works, then save data to a csv file."
    if response.status_code == 200:
        file_name = "discovery_list_" + day + ".csv"
        file_path = "USER_LOCAL_DRIVE_PATH"
        file = os.path.join(file_path, file_name)

        "create a csv file to write to and reference the variable as csv_file"
        with open(file, 'w' ) as csv_file:

            "Iterate through the lines of the response"
            for line in response.iter_lines():
                "Convert bytes into string, split the data on the comma and add to a a list called rows"
                rows = line.decode('utf-8').split(',')
                "list comprehension to remove additional quotes in the string"
                rows = [item.strip('"') for item in rows]
                "Add list of rows to a new list for csv file"
                lines_in_csv.append(rows)

            "insert periods into row list before combining domain strings"
            add_period(lines_in_csv)

            "Method to combine domain strings"
            concat_domain(lines_in_csv)

            "Write lines to csv file"
            content_lines = csv.writer(csv_file)
            for lines in lines_in_csv:
                content_lines.writerow(lines)
        
        print("Check your folder for new report...")

    else:
        print(response.status_code)
