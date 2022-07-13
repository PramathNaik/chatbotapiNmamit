import pandas as pd
import requests
df = pd.read_excel('DATA.xlsx')
url = "http://localhost:8000/addxl?q="
for i in range(len(df)):
    question = str(df['QUESTIONS'][i])
    answer = str(df['RESPONSES'][i])
    mainurl = url + question + "&a=" +answer
    #requests.get(mainurl)
    print("done")