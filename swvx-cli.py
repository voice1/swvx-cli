#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: swvx-cli is used to rapidly test switchvox api from command prompt shell.
Change the USERNAME, PASSWORD, and ADDRESS variables to fit your server setup.


Logging by default is set to INFO, change it as needed.

Usage:
    ./swvx.py <api method> ["parameters"]
    e.g.: 
    ./swvx.py switchvox.extensions.search
    ./swvx.py switchvox.extensions.getInfo "extensions=[899]"

Outputs to the cli are pretty printed. 
results are logged by default to the current directory


Analytics:
This script tracks API requests in order to get an ideal of its usage, and what API calls are commonly used.
Collected data is logged to the default log file.
Collected data:
    IP Address of where the script is run. (NOT your Swichvox)
    Switchvox Method (we do not capture parameters, just the method called.)

How we use this information:
This information is only collected to help us understand how often the script is being used, and what the most
common API calls are that are being made. We hope to use this information in the future to create useful tools.

"""
__version__ = '0.0.1'
__author__ = 'VOICE1 LLC <info@voice1-dot-me>'
__copyright__ = '(C) 2017 VOICE1 LLC'

# Change these to match your server!
USERNAME = "admin"
PASSWORD = "admin"
ADDRESS = "SWITCHVOX.IP.ADDRESS"
TIMEOUT = (15, 15)

# Please consider leaving this set to true.
ANALYTICS = True

import sys
import json
import logging

logger = logging.getLogger('swvx-cli')
logging.basicConfig(level=logging.INFO, 
                    filename="swvx-cli.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                    
try:
    from pyswitchvox.client import Client, ExtendAPIError, requests
except ImportError as e:
    error_message = "Can not import the pySwitchvox package.\n" \
    "Try: pip install pyswitchvox, or visit https://github.com/digium/pyswitchvox"
    
    logger.critical(error_message)
    sys.exit(error_message)


logger.debug("Creating switchvox object")
switchvox = Client(address=ADDRESS, username=USERNAME, password=PASSWORD, timeout=TIMEOUT)

def analytics(method, endpoint='collect'):
    """Measurement Protocol"""
    try:
        ipinfo = requests.get('http://ipinfo.io', timeout=TIMEOUT).json()
        logger.info("Captured public IP info: {}".format(ipinfo))
    except:
        ipinfo = {'ip': 'N/A'}
        
    payload = {
        'v': '1',                    # Version.
        'tid': 'UA-62762706-1',      # Tracking ID / Property ID.
        'cid': ipinfo.get('ip'),     # Anonymous Client ID. 
        't': 'event',                # Hit Type.
        'swvx_method': method,       # Switchvox method being documented.        
    }

    try:
        logger.info("Event Analytics: {}".format(payload))
        response = requests.post('http://www.google-analytics.com/' + endpoint, payload, timeout=TIMEOUT)
    except:
        return
    return response


if __name__ == '__main__':
    logger.debug("argv:", sys.argv)
    method = "switchvox.info.getList"
    param = ""
    result = None
    try:
        method = sys.argv[1]
    except:
        logger.warning("No method provided. Using default.")
        
    try:
        param = sys.argv[2]
    except:
        logger.warning("No parameters provided.")
    
    command = "result = %s(%s)" % (method, param)
    
    logger.info("%s(%s)" % (method, param))
    
    # We need to execute the 'string' provided on the CLI as an API call, as the provided string
    # maybe arbitary
    try:
        exec(command)
    except ExtendAPIError as e:
        print(str(e))
        
    data = json.dumps(result, indent=4)
    logger.info(data)

    print(data)
    
    if ANALYTICS:
        analytics(method)
    
    logger.info("Done.")