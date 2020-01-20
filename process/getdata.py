import pandas as pd
import matplotlib.pyplot as plt


def get_data():
    testdata = pd.read_csv('data/testdata.csv')
    testdata.dropna()
    
    # renaming the columns
    testdata.rename(columns={'LOCATION Latitude : ':'Latitude',
                        'LOCATION Longitude : ':'Longitude',
                        'LOCATION Altitude ( m)':'Altitude (m)'}, inplace=True)
    
    return testdata
    