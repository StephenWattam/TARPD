# TARPD Structured Data Templating
This repository contains code that retrieves structured research data from two sources: protocols.io, and the OSF.  These data are retrieved using the services' respective APIs, parsed into a structured format, and output using a Microsoft Word templating system to a single docx document.

## Prerequisites

 - python 3.8+
 - `pip install requirements.txt`

## Usage
The code is structured as a set of scripts to run in-order.  These tools are configured in `config.json`.

 1. `1_pull_from_protocols.py` --- Connect to protocols.io and retrieve data
 2. `2_pull_from_osf.py` --- Connect to OSF and retrieve files to a directory.  This doesn't currently work due to auth issues, so this script is inoperative.
 3. `3_merge_into_template.py` --- Render the files and database into a docx file.


## TODO / Further Work

 - OSF authentication is unreliable so currently files are retrieved from disk
 - Templating for MS Word is very limited due to poor library support for the format


## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
