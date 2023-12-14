import requests
from bs4 import BeautifulSoup
from docx import Document
from htmldocx import HtmlToDocx

class icis:
    def __init__(self):
        url="https://www.icis.com/explore/resources/news/"
        
    

response = requests.get(
    "https://www.icis.com/explore/resources/news/2023/12/13/10953329/ukraine-moldova-to-join-vertical-gas-corridor-in-january-2024/")
soup = BeautifulSoup(response.text, "html.parser")
header=soup.find("div", {"class": "wp-block-cover__inner-container"})
content=soup.find("div", {"class": "wpb_wrapper"})
ns=header.find("h1").text.split()
filename = ""
for i in ns:
    filename += i + " "

new_parser = HtmlToDocx()
docx = new_parser.parse_html_string(header.prettify())
new_parser.add_html_to_document(content.prettify(),docx)
docx.save(filename.strip()+".docx")
