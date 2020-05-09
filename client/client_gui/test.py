#!/home/jalexander/anaconda3/bin/python3

import os
import sys

path_to_client_functions = os.path.join(os.path.abspath(".."),"client_backend")
sys.path.insert(1,path_to_client_functions)

import client_functions
