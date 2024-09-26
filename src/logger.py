import logging 
import os
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #create a log file with name defined in f string 
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE) # path is make logs folder and inside that log file will be there 
os.makedirs(logs_path, exist_ok=True) # make that dir is not exist 

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # file path insdei the folder 

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # msg format inside the logging file 
    level=logging.INFO # where ever I'll write logging.INFO the msg in the above format will be writeen along with line number 
) # basic config, 