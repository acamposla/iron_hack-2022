import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import dateutil.parser
from datetime import datetime
import requests
from pandas import json_normalize
import os
from dotenv import load_dotenv
load_dotenv()
import meteomatics.api as api
import datetime as dt
from bs4 import BeautifulSoup
import re
#import src.manage_data as dat
import json


def urlf(letter):
    url =f"https://www.airlineratings.com/airline-ratings/?l={letter}" 
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")
    return soup
