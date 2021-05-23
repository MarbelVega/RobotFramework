from selenium import webdriver

def get_report_name_from_report_manager_checkbox(element):
    return element.find_element_by_xpath("./../../../td[contains(@class, 'x-grid3-td-title')]/div").text

def does_the_web_page_have_the_generic_error(element):
    try:
        element.find_element_by_xpath(".//td[contains(., 'The error has been logged and tech support has been automatically informed.')]/a[contains(., 'Go back')]/..")
        print("element found")
    except:
        return False
    return True

def get_the_generic_error_code(element):
    text = element.find_element_by_xpath(".//td[contains(., 'The error has been logged and tech support has been automatically informed.')]/a[contains(., 'Go back')]/..").text
    return text[text.find('E0E'):]

# We can set chrome capabilities easier through this method, rather than within robot
# Here is where we would make it headless and the like...
def set_chrome_capabilities(download_directory, is_headless=False):
    options = webdriver.ChromeOptions()
    if download_directory != 'default':
        prefs = {'download.default_directory': download_directory}
        options.add_experimental_option('prefs', prefs)
        if is_headless:
            options.add_argument('headless')
    capabilities = options.to_capabilities()
    return capabilities
