"""
This file contains the functions and variables for
importing statistical data from a csv into a 
dictionary for reporting
"""

from datetime import datetime
import csv

# Contstants
# Initialise statics dictionary with keys
STATS = [{'stats_code':'disp',
        'stats_name':'Disposable Income',
        'value_type':'val',
        'country_stats':[{
            'country_code':None ,
	        'country_name': None ,
	        'region_code': None, 
	        'region_name': None,
	        'statistic':[{
		        'year': None,
		        'value': None
		    }]
        }]
    },
    {'stats_code':'popu',
        'stats_name':'Population',
        'value_type':'num',
        'country_stats':[{
            'country_code':None ,
	        'country_name': None ,
	        'region_code': None, 
	        'region_name': None,
	        'statistics':[{
		        'year': None,
		        'value': None
		    }]
        }]
    }
]

def load_country_stats(stats_code, data_row, header_row):
    """
    loads the country_stats keys with values from header row in file
    """
    for stat in STATS:
        if stat['stats_code'] == stats_code:
            for country in stat['country_stats']:
                country['country_code'] = data_row[0]
                country['country_name'] = data_row[1]
                country['region_code'] = data_row[2]
                country['region_name'] = data_row[3]
                country['statistics'] = load_statistics(data_row, header_row)

def load_statistics(data_row, header_row):
    """
    loads annual statistical data for each country from stats_code.csv into 
    a list of annual statistics and returns that to the load_country_stats
    function to load with the other country statistics
    uses header row for year value and data rows for values
    """
    annual_stats = []
    value_row = data_row
    year_row = header_row
    for i in range(4,len(year_row)):
        annual_stats.append({'year':year_row[i],'value':value_row[i]})
    return(annual_stats)

def import_csv2dict(stats_name):
    """
    Imports data from csv file to python dictionary
    Assumes the csv file has headings in the first row for statistics keys
    Calls function to load remaining rows into STATS
    """
    stats_code = stats_name[:4]
    file_name = stats_name + '.csv'
    header_row = []
    try:
        with open(file_name, 'r', encoding='utf-8-sig', newline='') as csv_file:
            csv_data = csv.reader(csv_file, dialect='excel')
            first_row = True
            for row in csv_data:
                if first_row:
                    header_row = row
                    first_row = False
                    continue
                else:
                    load_country_stats(stats_code, row, header_row)          
                    continue

    except OSError as e:
        print(f'Unable to open CSV file. Please contact system manager with error:\n   >>  {e.args[1]}  <<')
        return False  

    return(STATS)                    
