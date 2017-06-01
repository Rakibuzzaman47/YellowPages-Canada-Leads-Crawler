import requests
from bs4 import BeautifulSoup
import time

print "Please Enter Yellow Pages Search/URL & Press Enter:"

url = raw_input()

response = requests.get(url)

if response.status_code == 200:
	codes = response.content
	soup = BeautifulSoup(codes, "lxml")
	business_names = soup.find_all("a", "jsListingName")
	business_address = soup.find_all("span", "listing__address--full")
	business_phone = soup.select(".mlr__submenu__item h4")
	business_contact_person = soup.select(".capText")
	business_website = soup.select(".mlr__item.mlr__item--website a")
	number = 0
	for names in business_names:
		name = business_names[number]
		name = str(name)
		name = BeautifulSoup(name, "lxml")
		name = name.text
		name = str(name)
		try:
			b_address = business_address[number]
		except IndexError:
			b_address = "N/A"
		address = str(b_address)
		address = BeautifulSoup(address, "lxml")
		address = address.text
		address = str(address)
		try:
			b_contact_phone = business_phone[number]
		except IndexError:
			b_contact_phone = "N/A"
		phone = str(b_contact_phone)
		phone = BeautifulSoup(phone, "lxml")
		phone = phone.text
		phone = str(phone)
		try:
			b_contact_person = business_contact_person[number]
		except IndexError:
			b_contact_person = "N/A"
		contact_person = str(b_contact_person)
		contact_person = BeautifulSoup(contact_person, "lxml")
		contact_person = contact_person.text
		contact_person = str(contact_person)
		try:
			b_website = business_website[number]
		except IndexError:
			b_website = "N/A"

		if b_website == "N/A":
			website = b_website
		else:
			website = b_website.get('href')
			website = str(website)
		fo = open("leads.txt", "a+")
		fo.write("\""+name+"\"")
		fo.write(";")
		fo.write("\""+address+"\"")
		fo.write(";")
		fo.write("\""+phone+"\"")
		fo.write(";")
		fo.write("\""+contact_person+"\"")
		fo.write(";")
		if website != "N/A":
			fo.write("\"https://www.yellowpages.ca"+website+"\"")
		else:
			fo.write("\"N/A\"")
			website = ""
		fo.write("\n")
		fo.close()
		number = number + 1
	print("Done. Please Move The leads.csv file to a safer location or It'll be overwritten.")
else:
	print("Error. Please contact with the Developer at shabujmona@gmail.com.")
	time.sleep(10)
	exit()
