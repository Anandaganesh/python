url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'
import matplotlib.pyplot as plt
import urllib.request as req

def fetch_url(url, fname):
    """
    Save a url to a local file.
    """
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode = 'wb') as fout:
        fout.write(data)

def read_csv(fname):
#   import pdb; pdb.set_trace()
    with open(fname, encoding = 'utf8') as fin:
        rows = []
        for i, line in enumerate(fin):
            values = line.strip().split(',')
            if i == 0:
                headers=values
            else:
                for j, val in enumerate(values):
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                    else:
                        values[j] = val
                rows.append(dict(zip(headers,values)))
    return rows
                
def filter(rows, state):
    res = []
    for row in rows:
        if row['state'] == state:
            res.append(row)
    return res

def get_date(row):
    return row['date']


def sortby(rows, col_name):
    def get_col_name(row):
        return row[col_name]
    return sorted(rows, key=get_col_name)

def get_value(rows, col_name):
    res=[]
    for row in rows:
        res.append(row[col_name])
    return res
    
res = read_csv('covid.csv')
ut_res = filter(res, 'UT')
ut_res = sortby(ut_res, 'date')
ut_val = set(get_value(ut_res, 'date'))

    
