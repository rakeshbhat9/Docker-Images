# Std Lib
import os
import logging
from datetime import date,timedelta

# Third Party Lib
import pandas as pd
from pandas.util.testing import makeDataFrame

log = logging.getLogger(__name__)
output_path = '/usr/local/airflow/dags/project_1/data'

if os.path.isdir(output_path):
    os.chdir(output_path)
else:
    os.mkdir(output_path)
    os.chdir(output_path)

def get_data():
    log.info('Reading data')
    d = makeDataFrame()
    d.to_csv(output_path+'/ipl.csv')
    log.info('Data placed in folder')
    return