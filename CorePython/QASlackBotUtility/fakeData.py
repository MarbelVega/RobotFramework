from faker import Faker

class fakeData(object):
    fake = Faker()

    def random_first_name(self):
        """This item returns a random first name using faker."""
        return self.fake.first_name()
    
    def random_last_name(self):
        """This item returns a random last name using faker."""
        return self.fake.last_name()
    
    def random_email(self, format="dot", first_name=None, last_name=None, domain="example.org"):
        """Either returns a random example.org email, or uses the variables to determine an email.
        ---More details will be added to this as this is used more.  This was preemptively given
        variables to work with the email parser stuff.---
        """
        if first_name is None:
            first_name = self.fake.give_me_a_first_name()
        if last_name is None:
            last_name = self.fake.give_me_a_last_name()
        
        # format stuff here
        return f"{first_name}.{last_name}@{domain}"
    
    def random_opportunity_name(self):
        """Returns a random string to be used as the opp name"""
        return f"{self.fake.md5()}"
    
    def random_project_name(self):
        """Returns a random string to be used as the project name"""
        return f"{self.fake.md5()}"
    
    def random_lead_name(self):
        """Returns a random string to be used as the lead name"""
        return f"{self.fake.md5()}"

    def random_company_name(self):
        """Returns a random string to be used as the company name"""
        return f"{self.fake.md5()}"

    def random_call_subject(self):
        """Returns a random string to be used as the call subject line"""
        return f"{self.fake.md5()}"
