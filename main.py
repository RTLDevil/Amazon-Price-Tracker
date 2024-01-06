import requests
import smtplib
from bs4 import BeautifulSoup
my_email = "Your email"
App_password = "You password App"
Amazon_Product_URL = "https://www.amazon.com.au/Apple-iPhone-Pro-Max-256/dp/B0CHX8VZNL/?_encoding=UTF8&pd_rd_w=4bWEU&content-id=amzn1.sym.f8cb1bd1-aeac-493c-be53-97c7cb120e56%3Aamzn1.symc.573c83ff-b207-408b-b0c7-3d92bb6b7d04&pf_rd_p=f8cb1bd1-aeac-493c-be53-97c7cb120e56&pf_rd_r=SGHTDRNWSCJXCVDVE8E0&pd_rd_wg=hx5F5&pd_rd_r=36429f1d-adff-41d5-a7ef-b89b75acd779&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/000000000 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "DNT": "1",
    "Accept-Encoding": "gzip, deflate, br"
}
responce = requests.get(url=Amazon_Product_URL, headers=Headers)
responce.raise_for_status()
soup = BeautifulSoup(responce.text, "html.parser")
price = soup.find(name="span", class_="a-offscreen").getText()
amount = price.split("$")[1]
# convert into float
price_float = amount.split(",")
Amount =float(''.join(price_float))
Product_name = soup.find(name="span", id="productTitle").getText()
if Amount < 2300.00:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=App_password)
    connection.sendmail(from_addr=my_email, to_addrs="the email you want to send", msg=f"SUBJECT: Amazon Price Tacker \n\n This Price of the {Product_name} is now {Amount}. Buy Now.")
    connection.close()