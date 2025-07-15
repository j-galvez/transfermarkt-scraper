# 🌍 Transfermarkt Scraper

This project is a Python script that scrapes data from **any football league page on [Transfermarkt](https://www.transfermarkt.com/)**, 
using the **BeautifulSoup** and **Requests** libraries. It extracts basic information about players and exports it to a CSV file.

## 📌 What does this scraper do?

- Accesses a league page on Transfermarkt (URL can be modified in the script).
- Extracts club names and their links.
- Visits each club's page.
- Extracts the following player information:
  - 👟 Club/Team
  - 🧍 Player name
  - #️⃣ Shirt number
  - 🧭 Position
- Saves all collected data to a file named `players.csv`.

- > ⚠️ By default, the script scrapes only a few teams and players for demonstration. You can remove or change the `limit=` parameters in the code to fetch full data for any league.

---

## 🛠️ Technologies Used

- Python 3
- BeautifulSoup 4
- Requests
- CSV
- datetime
- time


## ⚠️ In order to run this script, you must install BeautifulSoup 4 and Requests libraries
  'pip install beautifulsoup4 requests'


  

## ▶️ How to Use

### 1.Modify the league URL

In the script (`scraper.py`), locate the `requests.get(...)` line and replace the URL with the desired league page on Transfermarkt. For example:

```python
response = requests.get(
    'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1', headers=headers
)
```

You can use any league by changing the URL accordingly.



### 2.Run the script

After execution, a `players.csv` file will be created on the same folder where the script is saved with the scraped data.

---

## 📁 Example Output (`players.csv`)

| team               | name           | shirt | position          |
|--------------------|----------------|-------|-------------------|
| Manchester City    | Ederson        |   31  | Goalkeeper        |
| Chelsea FC         | Robert Sánchez |   1   | Goalkeeper        |

---
## 🔜 Future updates
-Extract age
-Extract player / team pictures


## 📎 Additional Notes

- The script includes a **10-second delay** between requests to respect Transfermarkt’s servers and avoid being blocked.
- If Transfermarkt changes its HTML structure, you may need to update the HTML selectors in the script.
- This project was created for educational purposes and as part of a personal portfolio.

---

## 📄 License

This project is for educational use only. All data belongs to [Transfermarkt](https://www.transfermarkt.com/).

----
Developed by **Jorge Gálvez** – [@j-galvez](https://github.com/j-galvez)


