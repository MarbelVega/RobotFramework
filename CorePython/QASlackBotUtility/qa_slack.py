from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Check token.txt for more info on tokens.
token = open('token.txt', 'r').read()

# Set this to True if you want it to appear as the integration bot your token is linked to.  Set it to False if you want slackbot to say it.
as_user = True

# Define channels you want your message to be sent to.
# File needs to be comma separated.
channels = open('channels.txt', 'r').read().replace(" ", "").split(',')

# Your Message Here.  This is the message that every victim in the channels will receive.
message = open("message.txt", 'r').read()

#############################################################################################################
# Below this line, you really do not need to do anything, unless you are fixing bugs, or doing custom stuff.
#############################################################################################################

# Create the client.
client = WebClient(token=token)

# Loop through the channels, post the message, and handle the responses if there is an error.
for channel in channels:
    try:
        response = client.chat_postMessage(channel=channel, text=message, as_user=as_user)
    except SlackApiError as e:
        print(f"Attempted to slack {channel}, received an error of {e.response['error']}.")
