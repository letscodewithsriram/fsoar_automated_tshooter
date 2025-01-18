import os
import tarfile
import shutil

def unzip_the_tarfile(configs):
    configs['logger_info'].info(configs)
    file_name =  os.listdir(configs['logspath'])[0]
    configs['logger_info'].info(str(file_name))
    _file = tarfile.open(configs['logspath'] + file_name)
    _file.extractall("logs\\")
    _file.close()