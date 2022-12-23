import re
import matplotlib.pyplot as plt

def extract_language(text):
    """
    Extracts the language from the given Page string
    
    Parameters
    ----------
    text: string from which language need to be extracted

    Returns
    -------
    string 

    Example
    -------
    >>>extract_language('2NE1_zh.wikipedia.org_all-access_spider')
    'zh'
    """
    try:
        found = re.search('_(..?).wikipedia', text).group(1)
    except AttributeError:
        # AAA, ZZZ not found in the original string
        found = '' # apply your error handling
    return found

from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm

def pipe(series):

    X = series.values
    result = adfuller(X)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])

    model = sm.tsa.seasonal_decompose(series, model='additive')
    model.plot()
    model.resid.plot()


    