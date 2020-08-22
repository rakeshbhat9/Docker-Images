# Std Lib
import os
import logging
from datetime import date,timedelta

# Third Party Lib
import pandas as pd


def get_data():
    l = pd.read_html('https://en.wikipedia.org/wiki/List_of_2020_Indian_Premier_League_personnel_changes')
    d = l[7]
    print(os.getcwd())
    d.to_csv('ipl.csv')
    return 