import requests
from bs4 import BeautifulSoup
import json
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)


def json_from_html_using_bs4(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")


# find("div", {"id": "articlebody"})
    # the whole damn row
    rows = soup.find("script", {"id": "__NEXT_DATA__"}).text
    temp = rows.split('"rows":')
    temp = temp[1].split(',"sponsorLogo":')
    jsonData = json.loads(temp[0])
    # print(jsonData)
    # print(rows)
    star = ['One', 'Two', 'Three', 'Four', 'Five']
    res, player_no = [], 1
    f = open("pga.csv", "w")
    # their names
    cursorObject = dataBase.cursor()
    for player in jsonData:
        name = player['playerName']
        stats = player['stats']
        avg_score = stats[0]['statValue']
        total = stats[1]['statValue']
        rounds = stats[2]['statValue']

        row = '"{0}",{1},{2},{3}\n'.format(name, avg_score, total, rounds)
        f.write(row)

        sql = "INSERT INTO pga (playerName, average, total,measured_rounds) VALUES (%s, %s,%s,%s)"
        val = (name, avg_score, total, rounds)
        cursorObject.execute(sql, val)

    dataBase.commit()
    f.close()


base_url = "https://www.pgatour.com/stats/detail/02569"


res = json_from_html_using_bs4(base_url)
