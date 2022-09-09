import requests
from datetime import timedelta
from datetime import datetime
import pandas as pd
import urllib.request
import json

def chronicling(arg1, arg2, arg3, arg4):
    '''
    arg1="sn84024738"
    arg2=YYYY-MM-DD
    arg3=YYYY-MM-DD
    arg4="dispatch"
    '''
    daterange=pd.date_range(arg2, arg3)
    for single_date in daterange:
        try:
            r=requests.get('https://chroniclingamercia.loc.gov/lccn/'+arg1+'/'+single_date.strftime('%Y-%m-%d')+'/'+'ed-1.json')
            for i in r.json()['pages']:
                with open('/chronicling_america/data/'+arg4+'/'+single_date.strftime('%Y-%m-%d')+'-'+i['url'][-10:].rstrip('json')+'.txt', 'w+') as text:
                    with urllib.request.urlopen(i['url'].rstrip('.json')+'/ocr.txt') as f:
                        text.write(f.read().decode('utf-8'))
            print(single_date.strftime('%Y-%m-%d'))
        except:
            continue
            