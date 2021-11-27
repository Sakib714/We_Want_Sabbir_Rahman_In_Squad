import requests
from bs4 import BeautifulSoup

url = "https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?class=3;id=25;type=team"
# print(tbody.find_all('tr')[0].find_all('td')[0].find('a').string)

# Getting html page code
result = requests.get(url).content
doc = BeautifulSoup(result, "html.parser")

tbody = doc.find_all("tbody")[0]

# Main part
tr = tbody.find_all('tr')[5]  # Number inside third bracket is player serial number starts from 0

"""
In tr line number 15

Enter - 
0 for mahmudullah
1 for shakib al hasan
2 for tamim iqbal
3 for mashfiqur rahim
4 for soumya sarkar
5 for sabbir rahman
6 for liton das
7 for mohammad naim
8 for afif hossain
9 for mohammad ashraful
10 for mashrafe mortaza
11 for nassir hossaain
12 for anamul haque
13 for nurul hasan
14 for aftab ahmed
15 for mahedi hasan
16 for mosaddek hossain
17 for mohammad saifuddin
18 for nazimuddin
19 for junaid siddique
20 for naeem islaam
21 for mohammad mithun
22 for shamim hossain
23 for imrul kayes
24 for ziaur rahman
25 for mehidy hasan miraz
26 for  shamsur rahman
27 for najmul hossain shanto
28 for farhad reza
29 for taskin  ahmed
30 for mominul haque
31 for ariful haque
32 for abu hider
33 for alok kapali
34 for sohag gazi
35 for mustafizur rahman
36 for raqibul hasan

more in < https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?class=3;id=25;type=team >


"""


def get_name():
    return tr.find('a').string


def match_span():
    return tr.find_all('td')[1].string


def match_played():
    return tr.find_all('td')[2].string


def innings():
    return tr.find_all('td')[3].string


def runs():
    return tr.find_all('td')[5].string


def highest_score():
    return tr.find_all('td')[6].string


def average_score():
    return tr.find_all('td')[7].string


def ball_faced():
    return tr.find_all('td')[8].string


def strike_rate():
    return tr.find_all('td')[9].string


def century():
    return tr.find_all('td')[10].string


def fifty():
    return tr.find_all('td')[11].string


def ducks():
    return tr.find_all('td')[12].string


def fours():
    return tr.find_all('td')[13].string


def sixes():
    return tr.find_all('td')[14].string


# print(tr)

# print(match_span())

# ~~~~~~#

def get_player_data():
    print('Name: ', get_name())
    print('Match Span: ', match_span())
    print('Match Played: ', match_played())
    print('Innings: ', innings())
    print('Total Runs: ', runs())
    print('Highest Score: ', highest_score())
    print('Average Score: ', average_score())
    print('Ball Faced: ', ball_faced())
    print('Strike Rate ', strike_rate())
    print('century Scored: ', century())
    print('Half-Century Scored: ', fifty())
    print('Ducks: ', ducks())
    print('Total Fours: ', fours())
    print('Sixes: ', sixes())


get_player_data()

# print(tbody)
