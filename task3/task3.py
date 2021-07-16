import requests
import json
from tkinter import *

Countries = ['USA', 'UKR', 'CAN', 'JPN', 'ITA']
custom = 'POL'
countryNames = []
dataLabels = []
countryLabels = []

def getData(iso):

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/sixmonth/"

    headers = {
        'x-rapidapi-key': "200109f47bmshe91f43046a9d637p115ecdjsne666b4a7da88",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url+iso, headers=headers)
    parsed = json.loads(response.text)
    return parsed

def showData():
    custom = entry.get().upper()
    
    customRes = getData(custom)
    print(customRes)
    if len(customRes) > 0:
        customLabel['text'] = customRes[0]['total_cases']
    for i in range(len(Countries)):
        res = getData(Countries[i])
        dataLabels[i]['text'] = res[0]['total_cases']
        countryLabels[i]['text'] = res[0]['symbol']


root = Tk()
root.title("COVID-19 INFO")
root.resizable(width = False, height = False)

for i in range(len(Countries)):
    dataLabels.append(Label(root, width = 10, anchor="w"))
    countryLabels.append(Label(root, width = 13, anchor="w"))

for i in range(len(Countries)):
    dataLabels[i].grid(row=i+1, column=1)
    countryLabels[i].grid(row=i+1, column=0)

customLabel = Label(root, width = 13, anchor="w", text='???')
customLabel.grid(row=len(dataLabels)+2, column=1, sticky=W)

entry = Entry(width=4)
entry.insert(0, 'POL')
entry.grid(row=len(dataLabels)+2, column=0, sticky=W)

showData()
Button(root, text="Refresh", command=showData, width=20).grid(row=len(dataLabels)+3, column=0, columnspan = 2)

root.mainloop()

