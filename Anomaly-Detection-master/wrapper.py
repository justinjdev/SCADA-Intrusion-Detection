# Justin Jones
# DFSC 3316 FALL 2017 
#
# This is a wrapper for `Anomaly Detection using tensorflow and tshark`
#   @   https://github.com/H21lab/Anomaly-Detection
#
# Every 20 minutes the program will start a new network capture, convert it into proper format, and run it with the script.
# Python 3.6

import subprocess
import asyncio
import time

def start_network_capture(in_path=''):
    output_status = subprocess.getoutputstatus('tshark -a duration:1200 -w {}'.format(in_path))
    if output_status == 0:
        output_status = subprocess.getoutputstatus('tshark -T ek -x -r {} > input.json'.format(in_path))
    
    return output_status
    
def process_pcap(path=''):
    output_status = cat
   
def train_model(path='input.json')   
    

def main():
    status = start_network_capture()
    time.sleep(1205)
    if status == 0:
        process_pcap()
    else:
        print("Error in capture process.")
    
    
    