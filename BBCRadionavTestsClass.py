####################################################
# radionav features tests
# JM
# 16/5/18
# A CHANGE HAS BEEN MADE
# v1.0
####################################################
import sys
from time import sleep
import BBCWebPageData as page_data
from BBCResultsClass import ResultsObject

from BBCRadionavTestClass import BBCRadionavObject
radionav = BBCRadionavObject()

drawer_open_closed_filename = "Open and Close a Drawer Test"
open_drawers_filename = "Open Drawers Test"
categories_links_filename = "Categories Links Test"
navigate_to_all_categories_filename = "Select All Categories Test"

#######################################################
# Scenario : Opening and closing the drawers - NOT DONE
#######################################################
def test_opening_and_closing_the_drawers():

    test_results_file = ResultsObject(drawer_open_closed_filename)
    test_title = ("\n\nTEST - CLICKING A SECTION OPENS A DRAWER, CLICKING AGAIN CLOSES THE DRAWER...")
    console_and_results_output(test_results_file, test_title)

    pass

##################################################################
#Scenario: Opening a drawer should close the other drawers
##################################################################
def test_opening_a_drawer_closes_other_drawers():

    test_results_file = ResultsObject(open_drawers_filename)
    test_title = ("\n\nTEST - OPENING A DRAWER CLOSES OTHER DRAWERS...")
    console_and_results_output(test_results_file, test_title)
        
    for section in page_data.sections:
        if radionav.open_a_drawer(section):
            sleep(1)
            test_results_file.write_to_file("\n\nTESTING - " + section + "drawer opened...")
            for drawer in page_data.sections:  
                is_drawer_open = radionav.is_drawer_open(drawer) 
                if section == drawer:
                    if is_drawer_open:
                        msg = "\n" + drawer + " drawer is OPEN - PASS"
                    else:
                        msg = "\n" + drawer + " drawer is CLOSED - FAIL"
                    console_and_results_output(test_results_file, msg)
                else:   
                    if not is_drawer_open:
                        msg = "\n" + drawer + " drawer is CLOSED - PASS"
                    else:
                        msg = "\n" + drawer + " drawer is OPEN - FAIL"
                    console_and_results_output(test_results_file, msg)
        else:
            print('\n\nCANNOT IDENTIFY ' + drawer + ' ON WEBPAGE - EXITING ' + test_title)
            return
    return 

#########################################################
#Scenario: Selecting categories displays categories links
#########################################################
def test_selecting_categories_displays_categories_links():

    test_results_file = ResultsObject(categories_links_filename) 
    test_title = "\n\nTEST - SELECTING CATEGORIES DISPLAYS CATEGORIES LINKS..."
    console_and_results_output(test_results_file, test_title)
    
    if radionav.open_a_drawer("categories"):
        sleep(1)
        for index in range (len(page_data.categories)):
            if radionav.get_categories_link(index): #also need to check that the category names match
                msg = ("\nCategory - " + page_data.categories[index] + " is visible - PASS")
                console_and_results_output(test_results_file, msg)
            else:
                msg = ("\nCategory - " + page_data.categories[index] + " is not visible - FAIL")
                console_and_results_output(test_results_file, msg)
    else:
        print('\n\nCANNOT IDENTIFY CATEGORIES DRAWER ON WEBPAGE - EXITING ' + test_title)
        
    return

####################################################################
#Scenario: Selecting all categories navigates to all categories page
####################################################################
def test_selecting_all_categories_navigates_to_all_categories_page():

    test_results_file = ResultsObject(navigate_to_all_categories_filename)
    test_title = "\n\nTEST - SELECTING ALL CATEGORIES LINK NAVIGATES TO ALL CATEGORIES PAGE..."
    console_and_results_output(test_results_file, test_title)

    categories_page_title = page_data.categories_page_title
    
    if radionav.open_a_drawer("categories"):
        if radionav.click_on_a_link(page_data.all_categories_link):
            if radionav.is_page_visible(categories_page_title):
                msg = "\nAll Categories page is visible - PASS"
            else:
                msg = "\nAll Categories page is not visible - FAIL"
            console_and_results_output(test_results_file, msg)
        else:
            print('\n\nCANNOT IDENTIFY ALL CATEGORIES LINK IN CATEGORIES DRAWER - EXITING ' + test_title)
    else:
        print('\n\nCANNOT IDENTIFY CATEGORIES DRAWER ON WEBPAGE - EXITING ' + test_title)

    return

# Writes output to the console and the results file
def console_and_results_output(results_file, msg):
    print(msg)
    results_file.write_to_file(msg)

# Returns to homepage
def return_to_homepage():
    if radionav.return_to_homepage():
        print("\nReturning to homepage")
    else:
         print('\n\nCANNOT IDENTIFY IPLAYER RADIO LINK ON WEBPAGE')
        
#############################    
def run_test():

    print('\nCHECKING FOR RADIONAV BEFORE PROCEEDING WITH TEST...')
    if not radionav.is_radionav_visible():
        print('\nRADIONAV NOT FOUND - EXITING TESTS')
        sys.exit()
    else:
        print('\nRADIONAV FOUND, PROCEEDING WITH TESTS...')

    test_opening_and_closing_the_drawers() #todo
    test_opening_a_drawer_closes_other_drawers()
    sleep(1)
    return_to_homepage()
    test_selecting_all_categories_navigates_to_all_categories_page()
    sleep(1)
    return_to_homepage()    #this fails due to wrong xpath
    test_selecting_categories_displays_categories_links()
    sleep(1)
    return_to_homepage()    #this fails due to wrong xpath
  
#################################################################################################################
if __name__=='__main__':
    
    #open the browser, load the page and confirm it is loaded
    #before proceeding with test
    
    iradio_url = 'http://www.bbc.co.uk/radio'
    main_page_title = 'BBC - iPlayer Radio'
    
    radionav.load_page(iradio_url)
    if not radionav.is_page_visible(main_page_title):
        print("BBC IPLAYER RADIO WEB PAGE HAS FAILED TO OPEN - EXITING TEST")
        sys.exit()
        
    run_test()
    radionav.close_browser()
