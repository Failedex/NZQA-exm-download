# NZQA pastexam download script

NZQA is slowly removing their past exams, so download them while you can

While you could download past exams via "Download files as zip", this method has proven to be extremely inconsistent as it wouldn't actually download all the past exam papers. 

Using the unmatched power of regex and 4 lines of cocain, I wrote this script (in 10 minutes or so) that would download **all** of the pastexams of a topic. 

I also made it so that it only download the relevant papers (exam and schedules), so it's also significantly faster than downloading their zip files

## "Installing"
People with git will know exactly how to `git clone` so I'll leave you be
For people without git, click this [link](https://raw.githubusercontent.com/Failedex/NZQA-exm-download/main/download.py) and right click to "Save page as".

## Usage 
For this example, I will be downloading level 3 organic past exams. 
Start by running the python script you just downloaded (download.py). If you don't have python, download it [here](https://www.python.org/) and run the file with python.

The program will ask for assestment code first, find this on the nzqa website. It should be a 5 digit number
```
assestment code: 91391
```

Next is the topic name, this doesn't really matter, it's just so the program can make an appropriately named folder.
```
topic: Organic_Chemistry
```

Afterwards, you should have a folder with the topic name with all the pastexam papers with their schedules (answers). Feel free to move and share this folder as you please.

If there are any issues, fix it yourself.
