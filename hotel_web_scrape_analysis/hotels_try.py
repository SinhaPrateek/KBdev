import bs4
import requests
import pandas as pd
"""
res = requests.get('https://in.hotels.com/search.do?resolved-location=CITY%3A1401516%3AUNKNOWN%3AUNKNOWN&destination-id=1401516&q-destination=Boston,%20Massachusetts,%20United%20States%20of%20America&q-check-in=2017-11-29&q-check-out=2017-11-30&q-rooms=1&q-room-0-adults=2&q-room-0-children=0')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
"""
with open(r'30nov_hotels.html', "r") as f:
    page = f.read()


bs4obj = bs4.BeautifulSoup(page,"lxml")
#columns = ["Date","Hotel_name","Price","Max_Price","Address","Guest_review","Star_rating"]
df = pd.DataFrame()
letters = bs4obj.find_all("div", class_="hotel-wrap")
i = 0
for element in letters:
    try:
        name = element.find("div", class_="description h-card resp-module").a.get_text()
        street_add = element.find("div", class_="description h-card resp-module").find("span", class_="p-street-address").get_text()
        guest_review = element.find("div", class_="description h-card resp-module").find("span", class_="guest-rating-value").find("strong").get_text()
        star_rating = element.find("div", class_="description h-card resp-module").find("div",class_="star-rating-container resp-module").get_text()
        old_price = element.find("div", class_="pricing resp-module").find("div", class_="price").find("del").get_text()
        new_price = element.find("div", class_="pricing resp-module").find("div", class_="price").find("ins").get_text()
        dict = {}
        dict['Date'] = "30Nov"
        dict['Hotel_name'] = name
        dict['Price'] = new_price
        dict['Max_price'] = old_price
        dict['Address'] = street_add+",Boston"+",MA"
        dict['Guest_review'] = guest_review
        dict['Star_rating'] = star_rating
        df = df.append(dict, ignore_index=True)
        #print(name,old_price,new_price,street_add,guest_review,star_rating)
        i = i+1
        print(i)
    except:
        name = element.find("div", class_="description h-card resp-module").a.get_text()
        street_add = element.find("div", class_="description h-card resp-module").find("span", class_="p-street-address").get_text()
        guest_review = element.find("div", class_="description h-card resp-module").find("span", class_="guest-rating-value").find("strong").get_text()
        star_rating = element.find("div", class_="description h-card resp-module").find("div", class_="star-rating-container resp-module").get_text()
        price = element.find("div", class_="pricing resp-module").find("div", class_="price").find("b").get_text()
        dict = {}
        dict['Date'] = "30Nov"
        dict['Hotel_name'] = name
        dict['Price'] = price
        dict['Max_price'] = price
        dict['Address'] = street_add + ",Boston" + ",MA"
        dict['Guest_review'] = guest_review
        dict['Star_rating'] = star_rating
        df = df.append(dict, ignore_index=True)
        #print(name,price,street_add,guest_review,star_rating)
        i = i+1
        print(i)

print(i)
df.to_csv("30_Nov.csv", index=False)


