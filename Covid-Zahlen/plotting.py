# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 23:54:17 2021

@author: hdamm
"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scraping import scrapePDF
from pdfRead import readPDF
from time import sleep

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

Einwohner_VG = 235623


def dt_iso_to_dt_RKI(dt_iso):
    dt_RKI = dt_iso.isoformat().replace('-', '/')
    return dt_RKI


def dt_RKI_to_dt_iso(dt_RKI):
    dt_iso = datetime.date.fromisoformat(dt_RKI.replace('/', '-'))
    return dt_iso


def inz1d(dt_iso):  # dt_RKI_to_dt_iso('2021/03/08')
    dt_RKI = dt_iso_to_dt_RKI(dt_iso) + ' 00:00:00+00'
    inz = RKIData_VG[RKIData_VG.Meldedatum == dt_RKI].AnzahlFall.sum()
    return inz


def inz7d(dt_iso):
    inz = 0
    for i in range(7):
        dt_RKI = dt_iso_to_dt_RKI(dt_iso - datetime.timedelta(days=i)) + ' 00:00:00+00'
        inzi = RKIData_VG[RKIData_VG.Meldedatum == dt_RKI].AnzahlFall.sum()
        inz = inz + inzi
    return inz


while True:
    abfrage = input("Sollen neue tagesaktuelle Werte vom LAGuS MV abgerufen werden? J/N ")
    if abfrage.upper() != "J" and abfrage.upper() != "N":
        print("Ungültige Eingabe.")
    else:
        break
if abfrage.upper() == "J":
    print("In Abfrage")
    # Getting every PDF within 2021
    scrapePDF()
    # Reading every PDF and returning the incidence
    readPDF()
    # Necessary to ensure that the Inzidenz.txt-File is written
    sleep(1)

LAGuSData = pd.read_csv("Inzidenz.txt")
LAGuSData.rename(columns={" Inzidenz": "Inzidenz laut LAGuS"}, inplace=True)
LAGuSData["Datum"] = pd.to_datetime(LAGuSData["Datum"], dayfirst=True)
LAGuSData = LAGuSData.sort_values("Datum", inplace=False).reset_index(drop=True, inplace=False)
inz7d_100ks_LaGuS = LAGuSData["Inzidenz laut LAGuS"].to_numpy()
dates_LaGuS = LAGuSData["Datum"].to_numpy()

RKIData = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv')
RKIData_VG = RKIData[RKIData.Landkreis == 'LK Vorpommern-Greifswald']
# Freeing some memory
RKIData = None

time_period = np.array([dt_RKI_to_dt_iso('2021/01/01'), datetime.date.today()])
days = (time_period[1] - time_period[0]).days
dates = np.array([time_period[0] + datetime.timedelta(days=i) for i in range(days)])
inz7d_100ks = np.array([inz7d(date) / Einwohner_VG * 100000 for date in dates])

# %%
plt.figure()
plt.title('7 Tage Inzidenz LK Vorpommern-Greifswald')
plt.ylabel('7 Tage Inzidenz / 100.000 Einwohner')
plt.xlabel('Datum')
plt.grid()
plt.plot(dates, inz7d_100ks, '-o', label='RKI')
plt.plot(dates_LaGuS, inz7d_100ks_LaGuS, '-o', label='LaGuS')
plt.xticks(rotation=90)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.legend()
plt.show()
