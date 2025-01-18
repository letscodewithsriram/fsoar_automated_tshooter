import re
import json
from datetime import datetime

def check_known_issues(logkey):
    with open('input/info.json', 'r')  as ucfh:
        data = json.load(ucfh)
        for uckey in data['usecases'].keys():
            # print ("Pattern -->" + data['usecases'][uckey].split(';')[1].strip())
            # print ("Log Line --> " + logkey)
            if re.search(data['usecases'][uckey].split('~')[1].strip(), logkey):
                #prob = data['usecases'][uckey].split(';')[1].strip()
                prob = logkey
                sol = data['usecases'][uckey].split('~')[2].strip()
                logtype = data['usecases'][uckey].split('~')[0].strip()
                # print ("Matched")
                with open('findings/output.txt', 'a') as findingsfh:
                    findingsfh.write(logtype + "~" + prob + "~" + sol + "\n")

def cyops_api_ssl_error(configs, dbs_dict):
    lclogger = configs['logger_info'].info(configs)
    cyops_path = configs['extracted_logspath']
    dbs_dict['ssl_cyops_api_errors'] = {}
    with open (cyops_path + '\\cyops-api\\ssl_cyops_api_error.log', 'r') as fh:
        for line in fh:
            line = line.strip()
            if line and line.startswith("202") and re.search('/',line) and re.search(" \[", line):
                # print(line)
                lg_date = line.strip().split(' ')[0]
                lg_time = line.strip().split(' ')[1]
                lg_type = line.strip().split(' ')[2]
                #lg_logline = " ".join(line.strip().split(':')[3])
                lg_logline = line
                # print("-->" + line)

                check_known_issues(lg_logline)
            else:
               lclogger.critical(line.strip())
               exit()