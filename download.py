import re
import requests 
from os.path import join, isdir
from os import mkdir

regex = "href=\"(.*?)\""

def get_links(url, dir): 
    prefix = "https://www.nzqa.govt.nz"
    postfix = ".pdf"
    html = requests.get(url).text 
    r = re.compile(regex, re.IGNORECASE|re.MULTILINE)

    a = r.findall(html)

    for i in a:
        name = i.split("/")[-1]
        if name[-4:] != postfix:
            continue

        tmp = name.split("-")

        if len(tmp) == 1: 
            continue

        if tmp[1] == "ass" or tmp[1] == "exm":
            print(name)
            res = requests.get(prefix+i)
            with open(join(dir, name), "wb") as f: 
                f.write(res.content)

def get_links_v2(code, dir): 
    for year in range(2013, 2023, 1): 
        print(year)

        # exm
        name = f"{code}-exm-{str(year)}.pdf"
        res = requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/{str(year)}/{name}")
        with open(join(dir, name), "wb") as f: 
            f.write(res.content)

        # schedule
        name = f"{code}-ass-{str(year)}.pdf"
        res = requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/schedules/{str(year)}/{name}")
        with open(join(dir, name), "wb") as f: 
            f.write(res.content)

if __name__ == "__main__": 
    code = input("assestment code: ")
    dir = input("topic: ")
    if not isdir(dir):
        mkdir(dir)
    # get_links("https://www.nzqa.govt.nz/ncea/assessment/view-detailed.do?standardNumber="+code, dir)

    get_links_v2(code, dir)
