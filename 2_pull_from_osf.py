"""This script retrieves files from the OSF record specified and places them in a directory
for later use with the templating engine."""

import sys
import json
from osf_client import OSFClient

print(f"This script is currently disabled: please place your OSF files in a directory as specified by the config.json")
sys.exit(1)


with open("auth.json") as fin:
    auth = json.load(fin)

client = OSFClient(auth["osf_personal_token"])

print(f"Retrieving user information (and testing login info!)")
user = client.get_user()
print(f"-> user: {user}")

# Full run project: m35px
#                   https://osf.io/m35px/
collection = client.get_collection("54sqr")

# TODO: retrieve files.
