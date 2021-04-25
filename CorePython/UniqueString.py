# Check if string is uniq until given length

str = "hkbfaiorinfoee#inlksgdl74bldk38"
no_places = 8

# for c in str:
#     print(c)
my_set = set()        # Empty curly braces {} will make an empty dictionary

for i in range(no_places):
    my_set.add(str[i])

print(my_set)
print("STRING IS UNIQ UPTO GIVEN LENGTH" if len(my_set) == no_places  else "STRING NOT UNIQ UPTO GIVEN LENGTH")

class inherit(HttpUser):

    @task
    def companydetails(self):

            test_name = "CFO-BFFE Company Details"

            r = self.client.get(f"/api/companydetails?companyId={company}", name=test_name, headers=headers )