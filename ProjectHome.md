IbPy is a third-party implementation of the API used for accessing the Interactive Brokers on-line trading system.  IbPy implements functionality that the Python programmer can use to connect to IB, request stock ticker data, submit orders for stocks and futures, and more.


See the [documentation index](DocumentationIndex.md) for installation instructions and usage.

### IbPy 0.7.6-9.51 Released 19 Dec 2008 ###

This release provides support for Python 2.6 and TWS API 9.51.

### IbPy 0.7.5-9.40 Released 07 Jul 2008 ###

Well, lookie there!  We still know how to release code!

This release has been brewing for quite a while.  In addition to supporting TWS 9.40, there's lots of minor fixes and enhancements.

### IbPy 0.7.4-9.20 Released 28 Aug 2007 ###

Now with flavor crystals!  Actually, TWS 9.20 is supported.

This release marks the first TWS API change since IbPy was restructured to utilize the java2python package.  The update took only a few hours, and most of that time was spent experimenting with a solution for overloaded classmethods.

### IbPy 0.7.3-9.00 Released 11 Aug 2007 ###

This release fixes options-related code in EReader.py.  Also included is a new demo script for placing option orders and retrieving option market data.

### IbPy 0.7.2-9.00 Released 02 Mar 2007 ###

This release fixes a missing import in EReader.py.  Also new in this release (and 0.7.1) is a conditional import and activation of the [Psyco](http://psyco.sourceforge.net/) specializing compiler.  To enable, set the `IBPY_PSYCO` environment variable.

### IbPy 0.7.1-9.00 Released 22 Feb 2007 ###

Several users reported problems extracting the archive on Windows.  The problem was the use of 'aux' as a directory name.  We've renamed the directory, regenerated the code, and created a new release.

### IbPy 0.7.0-9.00 Released 21 Feb 2007 ###

Read the release announcement [here](http://groups.google.com/group/comp.lang.python.announce/browse_frm/thread/82080918113959bd).  Download and documentation links are over there, on the right.  Enjoy!

### Version Numbers ###

The new IbPy has new version numbers.  The new format is `major.minor.micro-tws_api_version.`