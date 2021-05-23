"""
Affected Data Fields
        Client Types (multi-select value list)
        Stages (single-select value list)
        Firm Org Offices (multi-select value list)
        Role (single-select value list)
        SF330 Profile Code (single-select value list)
Potentially Affected Data Fields
        Secondary Categories (multi-select value list)
        Companies (one:many)
        Delivery Methods (multi-select value list)
        Firm Org Divisions (multi-select value list)
        Firm Org Practice Areas (multi-select value list)
        Primary Categories (multi-select value list)Staff Team (one:many)
        Firm Org Studios (multi-select value list)
        Submittal Type (single-select value list)
        Firm Org Territories (multi-select value list)
"""

from faker import Faker
import requests

from old_compass import CompassCore
import json

import time

how_many_to_create = 50
compass = CompassCore()


fake = Faker()
opportunity_ids = []

opportunity_post_data = []

def generate_opportunity():
    return {
        "ClientId":  6865358,
        "OpportunityName": f"After 5::{fake.md5()}"
    }

for _ in range(how_many_to_create):
    opportunity_post_data.append(generate_opportunity())

work = []


division = compass.read('firmorgs/divisions').json()[0]['DivisionID']
territory = compass.read('firmorgs/territories').json()[0]['TerritoryID']
pracarea = compass.read('firmorgs/practiceareas').json()[0]['PracticeAreaId']
studio = compass.read('firmorgs/studios').json()[0]['StudioId']
stype = compass.read('opportunities/submittaltype').json()[0]["SubmittalTypeId"]
dmeth =  compass.read('opportunities/deliverymethod').json()[0]["DeliveryMethodID"]
primcats = compass.read('opportunities/primarycategories').json()[0]['PrimaryCategoryId']
seccats = compass.read('opportunities/secondarycategories').json()[0]['SecondaryCategoryID']
clienttype = compass.read('opportunities/clienttypes').json()[0]['Id']
roleid = compass.read('opportunities/role').json()[0]['RoleId']
profcode = compass.read('opportunities/sf330profilecode/').json()[0]['ProfileCodeId']
officeid = compass.read('firmorgs/offices').json()[0]['OfficeID']

print(division)
print(territory)
print(pracarea)
print(studio)
print(stype)
print(dmeth)
print(primcats)
print(seccats)
print(clienttype)
print(roleid)
print(profcode)
print(officeid)
print()

###
#50401
#53305
#115030
#24050
#6440
#9353
#101313
#65602
#11461
#3681
#2852550
#15627
#2755208
#2755209
###

# create the opportunities in cosential
for i in range(len(opportunity_post_data)):
    r = compass.create([opportunity_post_data[i]], 'opportunities')
    opportunity_ids.append(r.json()[0].get('OpportunityId'))
    print(r.json()[0].get('OpportunityId'))

for i in range(len(opportunity_ids)):
    if i % 25 == 0:
        print('sleeping...')
        time.sleep(2)
        
    compass.create([{"OfficeID": officeid}], f'opportunities/{opportunity_ids[i]}/offices')
    compass.create([{"ProfileCodeId": profcode}], f'opportunities/{opportunity_ids[i]}/sf330profilecode')
    compass.create([{"RoleId": roleid}], f'opportunities/{opportunity_ids[i]}/role')
    compass.create([{"Id": clienttype}], f'opportunities/{opportunity_ids[i]}/clienttypes')
    compass.create([{"SecondaryCategoryId": seccats}], f'opportunities/{opportunity_ids[i]}/secondarycategories')
    compass.create([{"primaryCategoryId": primcats}], f'opportunities/{opportunity_ids[i]}/primarycategories')
    compass.create([{"DivisionId": division}], f'opportunities/{opportunity_ids[i]}/divisions')
    compass.create([{"TerritoryId": territory}], f'opportunities/{opportunity_ids[i]}/territories')
    compass.create([{"PracticeAreaId": pracarea}], f'opportunities/{opportunity_ids[i]}/practiceareas')
    compass.create([{"StudioId": studio}], f'opportunities/{opportunity_ids[i]}/studios')
    compass.create([{"SubmittalTypeId": stype}], f'opportunities/{opportunity_ids[i]}/submittaltype')
    compass.create([{"DeliveryMethodID": dmeth}], f'opportunitites/{opportunity_ids[i]}/deliverymethod')


# compass.start_from = 0
# compass.records_returned = 200
# while True:
#     r = compass.read('opportunities')
#     if r.text == '[]':
#         break
#     for row in r.json():
#         q = compass.read(f"opportunities/{row['OpportunityId']}/offices")
#         print(f"{row['OpportunityName']} :: {q.json()}")


# compass.start_from = 0
# compass.records_returned = 200
# while True:
#     r = compass.read('opportunities')
#     if r.text == '[]':
#         break
#     for row in r.json():
#         if "SQL CONN TEST" in row['OpportunityName']:
#             compass.remove(f"opportunities/{row['OpportunityId']}")