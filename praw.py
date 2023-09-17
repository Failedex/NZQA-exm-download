import requests 
import re
import string

regex = "href=\"(.*?)level=0[1-3]\">(?:.*?)</a>"
codes = set()

def get_subjects(letter):
    html = requests.get(f"https://www.nzqa.govt.nz/ncea/assessment/browse.do?type=&letter={letter}").text 
    r = re.compile(regex, re.MULTILINE)

    a = r.findall(html.replace("&amp;", "&"))
    
    for i in a: 
        print(i)
        get_codes(i)

regex2 = "<strong>(\d{5})</strong>"

def get_codes(subject): 
    prefix = "https://www.nzqa.govt.nz"

    for level in ["02", "03"]: 
        html = requests.get(prefix+subject+"level="+level).text
        r = re.compile(regex2, re.MULTILINE)

        a = r.findall(html)

        for i in a: 
            codes.add(i)

def main():
    for letter in string.ascii_uppercase:
        get_subjects(letter)

    for i in codes:
        print(i)

if __name__ == "__main__":
    main()
