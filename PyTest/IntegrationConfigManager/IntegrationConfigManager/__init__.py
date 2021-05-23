import csv
import yaml
import random
import os

class IntegrationConfigManager(object):
    '''
        This class makes managing things like environments and random users easier for pytest
        integration projects.

        It also allows a job to override the current environment by having an environment variable
        called "CURRENT_ENVIRONMENT".

        You can set this temporarily in a command prompt with 
            set CURRENT_ENVIRONMENT = "QA".
        You can set this temporarily in powershell or jenkins with
            $env:CURRENT_ENVIRONMENT = "QA".
        Jenkins jobs can be parametrized, and have the name of the parameter be "CURRENT_ENVIRONMENT"
        without the need to temporarily set it.
    '''
    CURRENT_ENVIRONMENT = ''

    def load_config(self, filename="environment_config.yml"):
        '''
            Loads an environment config, and returns a config relevant to your project based on
                the environment you are running against.
            
            Expects the configs to be written in yaml, since those allow comments and are fairly simple.

            Expects, unless otherwise specified, the file "old.config" to exist within the base
                directory of your project.
        '''
        with open(filename) as file:
            cfg = yaml.load(file, Loader=yaml.FullLoader)
        return cfg

    def load_user(self, firm_id, user_type, exclude_users=[], filename="creds.csv"):
        '''
            This will load a random user from the credentials file, based on the environment
                you are running against.
            
            Expects the file "creds.csv" to exist in your project directory, unless specified.
            The file contains a format like so:
                environment,firmid,type,username,password
            
            Exclude users by putting their usernames in the exclude_users array:
                exclude_users=['akulk', 'jenjo']
            
            **User Types (user_types) map up to the "type" field in the csv.
            **environment will match your current running environment in your project.
        '''
        users = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Filter by environment and user type
                if self.CURRENT_ENVIRONMENT.lower() in row['environment'].lower() and row['type'] in user_type and row['firmid'] == firm_id:
                    # Filter out username
                    if row['username'] not in exclude_users:
                        users.append(row)
        
        # Will break if there are no users, but that's ok.  We'll give some help text to tell you why.
        try:
            return random.choice(users)
        except:
            print(f"You need to add users to {filename} for your environment.")
