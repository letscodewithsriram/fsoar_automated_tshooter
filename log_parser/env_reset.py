import shutil

def clear_logs(configs):
    shutil.rmtree(configs['logspath'] + "fortisoar-logs")