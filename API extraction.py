# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:39:15 2023

@author: josec
"""

# imports das coisas
import json
import pandas as pd
import requests
import numpy as np

# API
url = 'https://kisense.cleanwatts.energy/api/1.4/sessions'

body = {
    "Login": "cwll_isep",
    "Password": "LivingLabs2023" #replace with the used user and pasword
}

headers = {
    "Accept-Encoding": "gzip,deflate",
    "Accept": "application/json",
    "Content-Type": "Application/json",
    "User-Agent": "Jakarta Commons-HttpClient/3.1",
    "Host": "kisense.cleanwatts.energy",  #header to authenticate
}
r = requests.post(url, headers=headers, data=json.dumps(body)) #request to authenticate

token = r.json()["Token"]
auth = "CW " + token #concating the CW to the recieved token 

headers_2 = {
    'Accept-Encoding': 'gzip,deflate',
    "Authorization" : auth,
    "Accept" : "application/json",
    'User-Agent': 'Jakarta Commons-HttpClient/3.1',
    "Content-Type" : "Application/json",
    "Host" : "kisense.cleanwatts.energy"
}


#GET PROD/CONS)


#instant, daily, hourly, monthly or yearly
granularity="hourly"
epochfrom=1609459200000 #time start use website https://www.epochconverter.com/
epochto=1685577600000 #time to end use website https://www.epochconverter.com/


# #################################################### Produzido #################################################
# 
tag1 = 2936 #id of the variable you want to retrieve
url_extract = url.rstrip("sessions")+"consumptions/"+str(granularity)+"?to="+str(epochto)+"&from="+str(epochfrom)+"&tags=%5B"+str(tag1)+"%5D"
r1 = requests.get(url=url_extract, headers=headers_2) #request for the data

aux_json = r1.json() #reads the json file that we got
extract = pd.DataFrame(aux_json, columns=['Read']) #add the data that we want to the dataframe
extract.insert(1, "epoch", pd.DataFrame([d['DateUTC']/1000 for d in aux_json]), True) #add the epoch time to the dataframe

extract.to_excel(r"PATH TO THE FILE") #path to where the excel will get saved