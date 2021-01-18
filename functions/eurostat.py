import re

def process_link(link):
    regex = re.compile("F.*\.tsv\.gz")
    r = re.search(regex, link)
    return link[(r.span()[0]+1):]

def process_datestring(string):
    regex_year = re.compile("\d{4}M")
    regex_month = re.compile("M\d+D")
    regex_day = re.compile("D\d+")
    reg = re.search(regex_year, string)
    year = reg.string[reg.start():reg.end()-1]
    reg = re.search(regex_month, string)
    month = reg.string[reg.start()+1:reg.end()-1]
    reg = re.search(regex_day, string)
    day = reg.string[reg.start()+1:reg.end()]
    return "{}-{}-{}".format(year, month, day)


    