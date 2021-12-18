import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

BUY_PRICE = 200
YOUR_SMTP_ADDRESS = ""
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

url = "https://www.amazon.com/Adapter-MacBook-Multiport-Thunderbolt-Accessories/dp/B09BTTXRN2/ref=sr_1_2_sspa?qid=1639828637&s=computers-intl-ship&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWFVMVlZHRFpKMlZUJmVuY3J5cHRlZElkPUEwMDc1MjU5MkNNMTlQTlIyTjQ3NCZlbmNyeXB0ZWRBZElkPUEwMDQ4ODgyREJGRDZEOUc5MFA2JndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
title = soup.find(id="productTitle").get_text().strip()
print(title)
price = soup.find(name = "span", class_ ="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )