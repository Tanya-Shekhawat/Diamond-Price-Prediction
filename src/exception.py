import sys 
from src.logger import logging  


def error_message_detail(error,error_details:sys): 
    _,_,exc_tb = error_details.exc_info() #exc_info is getting from the error_details from the system , it return 3 variables but we only need last one thats wy _,_ 
    file_name = exc_tb.tb_frame.f_code.co_filename # the exc_tb will have all the info it get from exc_info 

    error_message = "Error occured in python script name [{0}] line number [{1}] error message".format(
        file_name, exc_tb.tb_lineno,str(error) # [{0}] >> file name, lineno will get line number and then teh error along with line 
    )

class CustomException(Exception): 
    def __init__(self, error_message, error_details: sys): # error details will come form the system that why we imported the sys(generic ones)
        super().__init__(error_message) 
        self.error_message = error_message_detail(error_message, error_details=error_details) 

    
    def __str__(self):
        return self.error_message 