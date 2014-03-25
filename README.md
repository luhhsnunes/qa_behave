Environment Setup
=========

Make sure you have python on your machine.
Then install behave by 'pip install behave' or 'easy_install behave'
And install hamcrest 'pip install PyHamcrest' or 'easy_install PyHamcrest'

Browser Setup
=========
The application has only support for Firefox at the moment. It doesn't run with any other browser, unless you download and install the packages.
The file browser.py contains the browser setup to run the step files.
And environment.py contains the setup and tear down for the tests.

Running Behave Tests
=========
To run a specific test: 'behave path_to_file.feature'
To run the entire suite 'behave'

