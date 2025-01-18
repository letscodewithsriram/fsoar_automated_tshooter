
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import shutil
    import tarfile
    import logging
    import os
    logging.basicConfig(level=logging.DEBUG)
    # logging.debug('This will get logged')
    # logging.debug('This is a debug message')
    # logging.info('This is an info message')
    # logging.warning('This is a warning message')
    # logging.error('This is an error message')
    # logging.critical('This is a critical message')

    configs = {}
    dbs_dict = {}

    configs['logspath'] = ("C:\\Users\\sramanujam\\OneDrive - Fortinet Corp Main\\\FORTISOAR TAC\\AUTOMATION & ANALYTICS"
                           "\\LOG ANALYZER\\CODES\\fsoar_automated_tshooter\\logs\\")
    logging.info("Default Log Path: %s" % (configs['logspath']))

    configs['extracted_logspath'] = configs['logspath'] + "\\fortisoar-logs\\var\\log\\cyops\\"
    logging.info("Extracted Log Path: %s" % (configs['extracted_logspath']))

    configs['logger_info'] = logging

    with open('findings/output.txt', 'w') as findingsfh:
        findingsfh.write('')

    from modules import extracter, env_reset, parse_prod_logs, parse_cyops_api_ssl_errors_logs, generate_summary
    # extracter.unzip_the_tarfile(configs)
    parse_prod_logs.prod_parser(configs, dbs_dict)
    parse_cyops_api_ssl_errors_logs.cyops_api_ssl_error(configs, dbs_dict)
    generate_summary.create_workbook()
    # env_reset.clear_logs(configs)
