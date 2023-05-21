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

## Functions.

"""
	run([Matlan linter message index URL])

Runs the scraper, which then fetches the Matlab linter message index webpage,
and parses it for the messages and their severities, which is then prints to
standard output.

"""
def run(message_index_url: str):

	print(file=sys.stderr)

	print("Running Matlab linter message fetcher on", message_index_url, file=sys.stderr)

## Only run the scraper, if this file was the one invoked with Python.

if __name__ == "__main__":

	DEFAULT_INDEX_URL = "https://se.mathworks.com/help/matlab/matlab_env/index-of-code-analyzer-checks.html"

	if len ( sys.argv ) == 2:

		message_index_url = sys.argv[1]

	else:

		message_index_url = DEFAULT_INDEX_URL

	run(message_index_url)
