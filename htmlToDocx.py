import requests
from bs4 import BeautifulSoup
from docx import Document
from htmldocx import HtmlToDocx
class htmlToDocx:
    def __init__(self, html):
        self.new_parser = HtmlToDocx()
        docx = self.new_parser.parse_html_string(html.prettify())
        return docx
    def convert(self, html, docx):
        self.new_parser.add_html_to_document(html.prettify(),docx)
        return docx