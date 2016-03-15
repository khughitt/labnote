Installation
============

Requirements
------------

To use labnote, you must have a recent version of 
`Python (>=3.3) <https://www.python.org/>`__) available on your machine.

Additionally, labnote requires the following Python libraries:

-  `Beautiful Soup 4 <http://www.crummy.com/software/BeautifulSoup/>`__
-  `Jinja2 <http://jinja.pocoo.org/docs/dev/>`__
-  `PyYAML <http://pyyaml.org/>`__

If you are using pip to install labnote, all of the required
dependencies should be automatically installed for you.

Labnote is currently aimed at supporting Windows, Linux, and OS X setups.

Installing labnote
------------------

To install the latest stable version of Labnote using
`pip <https://docs.python.org/3.5/installing/index.html>`__, run:

::

    pip install labnote

To install the most recent version of Labnote from Github, run:

::

    pip install git+https://github.com/khughitt/labnote

To see a full list of options available for labnote, run ``labnote -h``:

::

    usage: labnote [-h] [-c CONFIG] [-i INPUT_DIRS [INPUT_DIRS ...]]
                [-o OUTPUT_FILE] [-u URL_PREFIX] [--print-config]
                [--user-css USER_CSS] [--user-js USER_JS]

    Generate HTML lab notebook.

    optional arguments:
    -h, --help            show this help message and exit
    -c CONFIG, --config CONFIG
                            Configuration filepath. (Will use configuration in
                            $HOME/.config/labnote/config.yml, if it exists.)
    -i INPUT_DIRS [INPUT_DIRS ...], --input-dirs INPUT_DIRS [INPUT_DIRS ...]
                            Input directory(s) containing notebook entries.
    -o OUTPUT_FILE, --output-file OUTPUT_FILE
                            Location to output notebook HTML to.
    -u URL_PREFIX, --url-prefix URL_PREFIX
                            Prefix to add to each entry URL. (Default: "")
    --print-config        Prints the default configuration for Labnote to screen
    --user-css USER_CSS   Custom stylesheet to use.
    --user-js USER_JS     Custom javascript file to use.

Testing installation
--------------------

To generate the example notebook, ``cd`` to the labnote source directory and
run:

::

    labnote -c example/example.config.yml \
        -i example/research/*/*           \
        -o example/research/index.html

If the installation is working, you should see output to the screen which looks
like:

::

	- Using configuration: example/example.config.yml
	- Starting Labnote
	LOADING
	- Scanning for notebook entries in example/research/animal_behavior/molothrus
	- Scanning for notebook entries in example/research/barnacles/cirripede-morphology
	- Scanning for notebook entries in example/research/barnacles/cirripede-taxonomy
	- Scanning for notebook entries in example/research/finches/finch-beak-size-comparison
	- Scanning for notebook entries in example/research/finches/finch-foraging-strategies
	- Scanning for notebook entries in example/research/finches/natural-selection
	- Scanning for notebook entries in example/research/images/1854_Balanidae_F339.2_figlbp12.jpg
	- Scanning for notebook entries in example/research/images/a1417007h.jpg
	- Scanning for notebook entries in example/research/private/notes.html
	- Scanning for notebook entries in example/research/resources/css
	- Scanning for notebook entries in example/research/resources/img
	* Adding example/research/animal_behavior/molothrus/README.html
	* Adding example/research/barnacles/cirripede-morphology/README.html
	* Adding example/research/barnacles/cirripede-taxonomy/README.html
	* Adding example/research/finches/finch-beak-size-comparison/beak_size.py
	* Adding example/research/finches/finch-foraging-strategies/foraging-strategies.py
	* Adding example/research/finches/natural-selection/thoughts.txt
	- Finished
	- Generating notebook HTML
	- Saving notebook to example/research/index.html

A file named ``index.html`` will be outputted ``example/``
directory and should look something like what is shown in the screenshot
from the overview section of the documentation.

Now you are ready to configure Labnote for your own files.

Automating notebook generation
------------------------------

The easiest way to keep your lab notebook up-to-date is to set Labnote so that
it is run every day.

Labnote can be easily automated using 
`Cron <https://en.wikipedia.org/wiki/Cron>`__. For example, to have labnote
regenerate your lab notebook once a day, run ``crontab -e`` to edit your
user-level cron jobs, and add:

::

    @daily labnote

If you have created a user configuration for labnote in
``$HOME/.config/labnote/config.yml``, then you are all set. Otherwise simply
add whatever options you would use when calling Labnote from the command-line
to the cronjob, e.g.:

::

    @daily labnote -c /path/to/config.yml

For more information on how to create and customize cron jobs on your system,
see the `Ubuntu Cron Tutorial <https://help.ubuntu.com/community/CronHowto>`__.

