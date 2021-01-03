#Read and parse log file
#Mefat Shabani


import re
import os.path

date_time_regex = r"(?P<date>(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d+ \d\d:\d\d:\d\d)"
type_regex = r"(?P<type>\S+)"
message_regex = r"(?P<msg>.+)"
log_regex = date_time_regex + "\s+" + type_regex + "\s+" + message_regex

file = input("Input file: ")

if os.path.isfile(file):
    file = open(file, "r")

    word = input("Input the word to search for: ")
    log = []

    for ln in file:
        capture = re.search(log_regex, ln)
        if capture is not None:
            log.append({
                "date": capture.group("date"),
                "type": capture.group("type"),
                "msg": capture.group("msg")
            });
    
    for log_entry in log:
        log_msg = log_entry["msg"]
        if(re.search(word, log_msg)):
            print(log_msg)
    
else:
    print("File does not exist")