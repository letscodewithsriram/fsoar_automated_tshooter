import re
from datetime import datetime

def prod_parser(configs, dbs_dict):
    lclogger = configs['logger_info'].info(configs)
    cyops_path = configs['extracted_logspath']
    dbs_dict['prod'] = {}
    with open (cyops_path + '\\cyops-api\\prod.log', 'r') as fh:
        for line in fh:
            if line.startswith("[202") and re.search("00:00]",line):
                datetime_str = line.strip().split(' ')[0]
                datetime_format = "[%Y-%m-%dT%H:%M:%S.%f+00:00]"
                dt_object = datetime.strptime(datetime_str, datetime_format)
                epoch_time = dt_object.timestamp()
                dbs_dict['prod'][epoch_time] = line.strip()
            else:
               lclogger.critical(line.strip())
               exit()