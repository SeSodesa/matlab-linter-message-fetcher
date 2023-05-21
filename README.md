# Matlab Linter Message Fetcher

This is a small Python 3 script that fetches the linter messages of Matlab
from the MathWorks website. The need for this comes from the fact, that before
the function `[codeIssues]` was introduced in R2022b, Matlab had no
(documented) programmatic way of listing the severities of its linter messages
when using the linters `[mlint]` or `[checkcode]`.

[codeIssues]: https://se.mathworks.com/help/matlab/ref/codeissues.html
[checkcode]: https://se.mathworks.com/help/matlab/ref/checkcode.html
[mlint]: https://se.mathworks.com/help/matlab/ref/mlint.html

## Installation

The project has been tested with Python 3.10, so that is the version of
CPython you should install. Once Python is in place, you should set up a
virtual environment for this project in a folder of your choosing
([docs][venv]). The repository contains a
`[requirements.txt](./requirements.txt)` file, which lists the dependencies
needed. Install them as instructed in the documentation ([docs][reqs]).

[venv]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
[reqs]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-requirements-files

## Usage

The package is used by invoking the `[run.py](./run.py)` with Python:

	python3.10 run.py [Matlab linter message index]

where the argument to the linter message index is optional, if using the default address
<https://se.mathworks.com/help/matlab/matlab_env/index-of-code-analyzer-checks.html>
works.

## License

See the `[LICENSE](./LICENSE)` file.
