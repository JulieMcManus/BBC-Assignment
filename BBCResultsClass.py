####################################################
# results class
# writes results to a file
# arguments: name of the results file
# JM
# 16/5/18
# v1.0
####################################################
import datetime
import os

class ResultsObject():

    def __init__(self, results_file_name, results_folder = 'BBCTestResults'):

        self.results_folder = results_folder
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)
        
        self.results_file_name = results_file_name
        self.folder_and_file_path = (self.results_folder + "\\" + self.results_file_name)
        self.log_file = self.get_log_file_name()
        
    def write_to_file(self, msg):
        with open(self.log_file, "a") as results:
            results.write(msg)
        return

    def get_folder_and_file_path(self):
        return self.folder_and_file_path

    def set_results_file_name(self, results_file_name):
        self.results_file_name = results_file_name
        return

    #################################################################################
    # Creates a file name for a log file by appending date/time to the filename
    # Arguments: The file name
    # Returns: The log file name with date and time appended
    ###############################################################################
    def get_log_file_name(self):

        now = datetime.datetime.now()
        right_now = (str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "-" + str(now.hour) + "-" + str(now.minute))
        return self.folder_and_file_path + " " + right_now + ".txt"

    def get_results_folder(self):
        return self.results_folder
        

#################################################################################################################
if __name__=='__main__':

    results = ResultsObject('Julie')
    
    folder_and_file_path = results.get_folder_and_file_path()
    print(folder_and_file_path)

    log_file_name = results.get_log_file_name()
    print(log_file_name)

    results_folder = results.get_results_folder()
    print(results_folder)
    
    results.set_results_file_name('Julie Results')
    results.write_to_file('Hello World')
    

