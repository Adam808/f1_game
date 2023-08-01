import re
from urllib.request import urlopen

#driver predictions
player1 = ['VER', 'PER', 'LEC', 'HAM', 'SAI', 'RUS', 'ALO', 'GAS','NOR', 'STR',
        'OCO', 'PIA', 'BOT', 'MAG', 'RIC', 'HUL', 'ZHO', 'DEV', 'TSU', 'ALB', 'SAR']
player2 = ['VER', 'LEC', 'SAI', 'PER', 'RUS', 'HAM', 'NOR', 'BOT', 'ALO', 'GAS',
       'OCO', 'STR', 'ALB', 'MAG', 'HUL', 'RIC', 'ZHO', 'SAR', 'TSU', 'PIA', 'DEV']
player3 = ['VER', 'PER', 'LEC', 'SAI', 'RUS', 'HAM', 'ALO', 'NOR', 'BOT', 'OCO',
       'MAG', 'STR', 'GAS', 'PIA', 'RIC', 'HUL', 'TSU', 'ZHO', 'ALB', 'DEV', 'SAR']

#create dict of entries
entries = {'player1': player1, 'player2': player2, 'player3':player3}

#create list of drivers
url = "https://www.formula1.com/en/results.html/2023/drivers.html"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = '<span class="uppercase hide-for-desktop">.*?</span>'
raw_names = re.findall(pattern, html)
driver_list = []
for i in raw_names:
    driver_list.append(re.sub("<.*?>", "", i))

#check that all lists contain same drivers
for i in entries:
    print(sorted(entries[i]) == sorted(driver_list))

#calculate scores
def score(x):
    global driver_list
    score = 0
    for i in x:
        score += abs(x.index(i) - driver_list.index(i))
    return score

#output scores
for i in entries:
    print(i, score(entries[i]))
