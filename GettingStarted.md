# Installation #

Be sure to have the following dependencies installed:

  * [Python 2.5](http://www.python.org/download/releases/2.5/) - IbPy requires Python 2.5 or newer.
  * [Interactive Brokers TWS](http://www.interactivebrokers.com/en/control/twscontrol.php) - IbPy works with both browser-based and stand-alone versions of TWS.

Then download, unpack, and install the IbPy release.

  * Download the latest release from http://code.google.com/p/ibpy/downloads/list
  * Unpack the release using `tar` on Linux, BSD, or MacOS.  Unpack the zip file on Windows.
  * Run `python setup.py install` in the release directory extracted from the archive.

Digest instructions:
```
  $ wget http://ibpy.googlecode.com/files/IbPy-0.7.0-9.00.tar.gz
  $ tar xfz IbPy-0.7.0-9.00.tar.gz
  $ cd IbPy-0.7.0-9.00
  $ python setup.py install
```


# Running the Demos #

There are several example scripts in the `demo` directory of the
release.  These are:

  * `reference_python` - prints TWS messages to the console using the generated code within IbPy
  * `reference_jython` - prints TWS messages, using the Java and Jython (not IbPy).
  * `example_opt` - prints TWS messages and uses the optional IbPy interface
  * `api_coverage` - executes all of the TWS API methods and displays coverage statistics

To run these scripts, first install IbPy, then start TWS and login.
Next navigate to the `demo` directory created when the release was
unpacked, then run the scripts like so:

```
  $ ./reference_python
```

Or even:

```
  $ python example_opt
```


Good luck, and happy trading.