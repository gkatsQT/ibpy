# Synopsis #

This tutorial describes how to build IbPy from scratch.  By using this
method, you can create an IbPy installation for the latest TWS API
version.


## Prerequisites ##

We're going to assume that you're using a modern POSIX system (such as
Linux, Mac OS, or one of the BSDs).  We're also going to assume that
you've got Python installed.

Everything we do will be in a directory called `src` in our home
directory.  If you don't have such a thing, run these commands:

```
    $ cd ~
    $ mkdir src
```


## Install java2python ##

To build IbPy sources, we need [java2python](http://code.google.com/p/java2python/) and its dependancies.  Be sure you've installed
[Antlr 2.7.7](http://www.antlr2.org/) and its Python library.

You'll need a very specific version of java2python, [revision 50](https://code.google.com/p/ibpy/source/detail?r=50).
Checkout, build and install:

```
    $ cd ~/src
    $ svn co -r 50 http://java2python.googlecode.com/svn/trunk java2python
    $ cd java2python/java2python
    $ make
    $ cd ..
    $ python setup.py install --user
```

This will install the java2python package into
`~/.local/lib/python2.6/site-packages`, and the `j2py` script in
`~/.local/bin`.  Make sure the bin directory is in your `PATH`.

## Checkout IbPy ##

The remaining build process is automated from within the IbPy package.
Check out the source:

```
    $ cd ~/src
    $ svn co http://ibpy.googlecode.com/svn/trunk ibpy
```


Next we need to build the translated source code. The Makefile in
`ib/ext` handles this for us:

```
    $ cd ~/src/ibpy/ib/ext
    $ make modules-clean
    $ make
```

## Build a Distribution ##

At this point, you can copy or symlink the directory `~/src/ibpy/ib`
into your Python path and it will work.  If you'd rather have a full
distribution, you can now build that and install from it instead.

```
    $ cd ~/src/ibpy
    $ make
```

This will create two files, one `.tar.gz` and one `.zip`, in the
`release-M-N` directory, where `M` is the IbPy version and `N` is the TWS
API version.