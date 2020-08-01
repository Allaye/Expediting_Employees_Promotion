#!/usr/bin/env python
# coding: utf-8

import datetime
import time 
import pandas as pd
import numpy as np


def time_tracker(starttime, endtime, filename, extension, wageperhour = 5):
    '''
    @time_tracker is a function that can be used to calculate the money earned when working.
    this function accepts tuple objects nothing else in the form '9/15/18/10/30' month/day/year/hour/minute in this 
    order nothing else
    '''
    eyear, emon, eday, ehour, emin = endtime     #tuple unpacking the arguments 
    syear, smon, sday, shour, smin = starttime
    
    st = datetime.datetime(syear, smon, sday, shour, smin)     #convert the stings into datetime object
    et = datetime.datetime(eyear, emon, eday, ehour, emin) 
    # calculating the differences between the start time and the end time 2
    wt =  et - st 
    wts = wt.total_seconds()     # converting the total time worked into seconds for eazy calculation
    ttw = int(float(str(wts)))     # convert the total time worked in seconds into integer
    duration = datetime.timedelta(seconds = ttw)     #converting the total seconds works into a date-time format
    divider = 3600
    total_earned = float((wts/divider)* wageperhour)     #calculating the money earned and converting the value into a float
    print('you worked for {} and earned {}{:.2f}{}'.format(duration,'$',total_earned,'dollars'))     #using the .string format method

    save_time_tracker_details(eyear, emon, eday, ehour, emin, syear, smon, sday, shour,
                              smin , wageperhour, total_earned, duration, filename, extension)
    



def save_time_tracker_details( eyear, emon, eday, ehour, emin, syear, smon, sday, shour,
                              smin , wageperhour, totalwage, totaltime, filename, extension):
    
    """
    @save_time_tracker_details is a simple function that just saves the data generated form the time_tracker fuction 
    into a csv or excel file,  
    """
    dataname = "".join([filename, extension])     #joining the filename and the extension
    col = np.array(['eyear', 'emon', 'eday', 'ehour', 'emin', 'syear', 'smon', 'sday', 'shour',
                              'smin' , 'wageperhour', 'totalwage', 'time_worked'])    #creating an array
    tracker_data = pd.DataFrame(data=[[eyear, emon, eday, ehour, emin,syear, smon, sday, shour,
                              smin , wageperhour, totalwage, totaltime]], columns=col)     #creating the dataframe 
    
    if extension == '.csv' or '.CSV':      #saving the dataframe as a csv or excel

        tracker_data.to_csv(dataname)    
    else:
        tracker_data.to_excel(dataname)



def save_time_tracker_details( eyear, emon, eday, ehour, emin, syear, smon, sday, shour,
                              smin , wageperhour, totalwage, totaltime, filename, extension):
    
    """
    @save_time_tracker_details is a simple function that just saves the data generated form the time_tracker fuction 
    into a csv or excel file,  
    """
    dataname = "".join([filename, extension])     #joining the filename and the extension
    col = np.array(['eyear', 'emon', 'eday', 'ehour', 'emin', 'syear', 'smon', 'sday', 'shour',
                              'smin' , 'wageperhour', 'totalwage', 'time_worked'])    #creating an array
    tracker_data = pd.DataFrame(data=[[eyear, emon, eday, ehour, emin,syear, smon, sday, shour,
                              smin , wageperhour, totalwage, totaltime]], columns=col)     #creating the dataframe 
    
    if extension == '.csv' or '.CSV':      #saving the dataframe as a csv or excel

        tracker_data.to_csv(dataname)    
    else:
        tracker_data.to_excel(dataname)



def main():
    '''
    @Evans if you still want to use the user input in the code add it here, if you are done delete this commet
    '''
    start = 2020,7,30,8,20
    end =  2020,7,31,12,30
    time_tracker(start, end, "testing", '.csv', 5)



if __name__ == "__main__":
    
    main()