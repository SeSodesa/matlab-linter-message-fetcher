### run.py
#
# The root file of this project. Start the scraper with
#
#    python3.10 /path/to/this/run.py
#
# after having installed the requirements listed in requirements.txt.
#

## Imports

import sys
import requests

from bs4 import BeautifulSoup

## Functions.

"""
	run([Matlab linter message index URL])

Runs the scraper, which then fetches the Matlab linter message index webpage,
and parses it for the messages and their severities, which is then prints to
standard output.

"""
def run ( message_index_url : str ):

	print ( "\nRunning Matlab linter message fetcher on", message_index_url, file=sys.stderr )

	page = requests.get ( message_index_url )

	soup = BeautifulSoup ( page.content, "html.parser" )

	table_rows = soup.find_all ( "tr" )

	# Print header row.

	print ( " Check ID ␟ Severity ␟ Message ␟ Can be disabled" )

	# Then print each linter message.

	for row in table_rows:

		row_data = row.find_all ( "td" )

		# Skip rows that do not look like linter message rows.

		if not len ( row_data ) == 4:

			continue

		linter_code = row_data[0].code.contents[0]

		code_severity = row_data[1].contents[0]

		linter_message = row_data[2].contents[0]

		fourth_column = row_data[3].contents[0].lower()

		if fourth_column == "true":

			can_be_replaced = True

		elif fourth_column == "false":

			can_be_replaced = False

		else:

			continue # … as this is not a linter message table row.

		print ( " ", linter_code, " ␟ ", code_severity, " ␟ \"", linter_message, "\" ␟ ", can_be_replaced , sep="")

	# end for

## Only run the scraper, if this file was the one invoked with Python.

if __name__ == "__main__":

	DEFAULT_INDEX_URL = "https://se.mathworks.com/help/matlab/matlab_env/index-of-code-analyzer-checks.html"

	if len ( sys.argv ) == 2:

		message_index_url = sys.argv[1]

	else:

		message_index_url = DEFAULT_INDEX_URL

	run ( message_index_url )
