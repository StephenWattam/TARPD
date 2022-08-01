"""This script retrieves data from protocols.io, processes it to extract simple structured data
from the protocol run, and saves it to disk in JSON format for later use.

The rules written here are specific to the format used in the tarpd project, but are designed to be
relatively portable."""

import json
import re
import logging

from protocols_client import ProtocolsClient

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


CONFIG_FILENAME = "config.json"

logger.info(f"Looking for config at {CONFIG_FILENAME}...")
with open(CONFIG_FILENAME) as fin:
    config = json.load(fin)


client = ProtocolsClient()
about_me = client.get_profile()

logger.info(f"Logged in as {about_me['user']['username']}")
logger.info(f"Retrieving run {config['run_id']}")
run = client.get_run(config['run_id'])


# Extract the steps
steps = run["protocol"]["steps"]

db = {}
for step in steps:

    data = json.loads(step["data"])
    blocks = data["blocks"]
    title = blocks[0]["text"]
    key = re.search("\[(.+)\]", title)
    logger.debug("Found section with title '%s' and key '%s'", title, key)

    # Skip if we don't see a [group_key]
    if key is None:
        continue
    key = key.group(1)

    # Handle different forms of input data
    input_data = None
    if "entityMap" in data and len(data["entityMap"]) > 0:
        input_data = data["entityMap"][0]

    # If nothing is there, skip.
    if input_data is None:
        continue

    # Depending on the type
    typ = input_data["type"]
    value = None
    logger.debug("Type of entry is '%s', value=%s", typ, value)
    if typ == "notes":
        # Join the text together as paragraphs.  Not certain this will cover all cases
        # but it should get the main use-case of the notes field.
        db[key] = "\n\n".join([x["text"] for x in input_data["data"]["blocks"]])

    if typ == "smart_component":
        # Read each key as a unique top-level key
        for a in input_data["data"]["fields"]:

            key = re.search("\[(.+)\]", a['name'])
            if key is None:
                continue
            db[key.group(1)] = a['value']

    if typ == "link":
        # A link
        db[key] = input_data["data"]["url"]


# Write to disk
logger.info("Writing database to disk at %s", config['database_filename'])
with open(config["database_filename"], 'w') as fout:
    json.dump(db, fout, indent=4)
logger.info("Success.")
