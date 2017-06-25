#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0
count_salary = 0
count_email = 0
count_payments = 0
count_poi_payments = 0
number_of_entries = len(enron_data)

for key, value in enron_data.items():
    #print(key, len([item for item in value if item]))
    if(enron_data[key]['poi']):
    	count = count + 1
    if(enron_data[key]['poi'] & (enron_data[key]['salary'] != 'NaN')):
    	count_poi_payments = count_poi_payments + 1
    if(enron_data[key]['salary']!= 'NaN'):
    	count_salary = count_salary + 1
    if(enron_data[key]['email_address']!= 'NaN'):
    	count_email = count_email + 1
    if(enron_data[key]['total_payments']!= 'NaN'):
    	count_payments = count_payments + 1


print("Number of POIs = "+ str(count))
#print(enron_data["PRENTICE JAMES"].keys())
print("Number of salaries = "+ str(count_salary))
print("Number of email addresses = "+ str(count_email))
print(count_payments)
print(number_of_entries)
print(count_poi_payments)


