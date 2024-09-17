from bs4 import BeautifulSoup
import requests

def find(url, tag, class_name=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if class_name is None:
        return soup.find_all(tag)
    return soup.find_all(tag, class_=class_name)

def solution_number(url):
    h4_tags = find(url, 'h4')
    for h4_tag in h4_tags:
        if "Solutions".strip() in h4_tag.text:
            target_tag = h4_tag.find_next()
            return target_tag.text