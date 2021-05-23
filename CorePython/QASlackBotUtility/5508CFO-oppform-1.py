from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# This is the section that shows you how to find stuff
labels = (By.CLASS_NAME, "datalabel")
# this will need to be overridden in the loop, but works for some
rq_checkbox_v1 = (BY.XPATH, "../../td[2]")  #!! does not work for all, because we are not consistent on how we html.

# the indexes of the checkbox orders
field_name = {"idx": 1, "name": "field_name"}
require_fields = {"idx": 2, "name": "require_field"}
grid_enable = {"idx": 3, "name": "grid_enable"}
grid_edit = {"idx": 4, "name": "grid_edit"}
enable_field = {"idx": 5, "name": "enable_field"}
conditional_require_by_stage = {"idx": 6, "name": "req_by_stage"}
associated_Forms={"idx": 7, "name": "assoc_forms"}




def highlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element.
    Very useful when repling
    """
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    #time.sleep(effect_time)
    #apply_style(original_style)



driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

# do login stuff here.  For now, we are using the python repl so stuff will have to happen.


l = driver.find_elements(By.CLASS_NAME, "datalabel")

# highlight our items to make sure we got the right ones
for item in l:
    highlight(item, 0, 'red', 3)

the_fields = []

# get the list of fields
for item in l:
    the_fields.append(item.text.strip('*').strip(':'))


# see what we find for required fields!
for item in l:
    rq_checkbox = item.find_element(By.XPATH, "../../td[1]")
    highlight(rq_checkbox, 0, 'Blue', 3)

# see what we find on the table
required_table_item = driver.find_element(By.XPATH, "//td[@class='SubHeaderCell', contains(text(), 'Required Field')]")


# triaging for which row is the required field in the table
required_table_item = driver.find_element(By.XPATH, "//td[@class='SubHeaderCell'][contains(text(), 'Require Field')]")
highlight(required_table_item, 0, 'purple', 5)


# highlight everything just to see

x = driver.find_elements(By.XPATH, f"//div[contains(@class, 'DataLabel')]")
for item in x:
    for label in (field_name,
                  require_fields,
                  grid_enable,
                  grid_edit,
                  enable_field,
                  conditional_require_by_stage,
                  associated_Forms):
        if label['idx'] == 1:
            color = 'DarkSeaGreen'
        elif label['idx'] == 2:
            color = 'DarkViolet'
        elif label['idx'] == 3:
            color = 'DarkSlateGray'
        elif label['idx'] == 4:
            color = 'Fuchsia'
        elif label['idx'] == 5:
            color = 'Crimson'
        elif label['idx'] == 6:
            color = 'ForestGreen'
        elif label['idx'] == 7:
            color = 'DarkTurquoise'
        try:
            rq_x = item.find_element(By.XPATH, f"../../td[{label['idx']}]")
        except:
            rq_x = item.find_element(By.XPATH, f"../../../../../../td[{label['idx']}]")
        highlight(rq_x, 0, color, 5)

field_list = {}

x = driver.find_elements(By.XPATH, f"//div[contains(@class, 'DataLabel')]")
for item in x:
    temp_dictionary = {}
    for label in (field_name,
                  require_fields,
                  grid_enable,
                  grid_edit,
                  enable_field,
                  conditional_require_by_stage,
                  associated_Forms
    ):
        try:
            rq_x = item.find_element(By.XPATH, f"../../td[{label['idx']}]/input").is_selected()
            temp_dictionary[label['name']] = rq_x
        except:
            try:
                rq_x = item.find_element(By.XPATH, f"../../../../../../td[{label['idx']}]/input").is_selected()
                temp_dictionary[label['name']] = rq_x
            except:
                continue
    field_list[item.text.strip(":").strip("*")] = temp_dictionary

print(field_list)


for item in z["fields"]:
   if item['label'] in field_list.keys():
     print(f"{item['label']} has been found")
   else:
     print(f"{item['label']} has not been found")


for item in z["fields"]:
   try:
    print(f"{item['label']}:  {field_list.get(item['label'])}")
    print(f"enabled:  {field_list.get(item['label']).get('enable_field')} == {item.get('enabled')}")
   except:
    continue

for item in z["fields"]:
   try:
    print(f"{item['label']}:  {field_list.get(item['label'])}")
    print(f"enabled:  {field_list.get(item['label']).get('require_field')} == {item.get('requiredByStage')}")
   except:
    continue

y = driver2.find_element_by_tag_name('pre').text


z = json.loads(y)

for item in z['fields']:
    print(f"{item['label']}::   enabled->  {item.get('enabled')}    rqd ->    {item.get('requiredByStage')}")
# go through, check everything
# compare the two pages
# go through, make required by stages
# compare the two pages
