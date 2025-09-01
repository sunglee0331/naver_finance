**Naver Finance Market Data Scraper
**

This Python script scrapes stock market data from Naver Finance and saves it as a CSV file. It uses Selenium for web automation and pandas for data processing.

Features

Automates Chrome browser to navigate Naver Finance pages.

Selects specific financial fields:

Operating Profit (영업이익)

Total Assets (자산총계)

Total Buy Quantity (매수총잔량)

Iterates through pages (1–40) and collects market data.

Handles missing values and appends new data to a CSV file (sise.csv).

Requirements

Python 3.8+

Google Chrome browser

ChromeDriver compatible with your Chrome version

Python packages:

pip install pandas selenium

Usage

Set up ChromeDriver:
Download ChromeDriver from here
 and ensure it is in your system PATH.

Run the script:

python naver_finance_scraper.py


The script will:

Open the Naver Finance Market Summary page.

Reset all selected checkboxes.

Select desired financial items.

Navigate pages 1 to 40 and extract data.

Save results to sise.csv (appends if file already exists).

Notes

You can modify the items_to_select list to scrape different fields.

The script may break if the Naver Finance website updates its HTML structure.

Ensure ChromeDriver version matches your installed Chrome browser.

Example Output

CSV columns may include:

종목명, 현재가, 전일비, 등락률, 거래량, 매수총잔량, 영업이익, 자산총계, ...

License

This project is for educational purposes and personal use.
