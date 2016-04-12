### overloaded (class) ###

An implementation of overloaded functions.

class defined at [line 46](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#46)

> method **`__init__(default_func)`**

> defined at [line 49](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#49)
> ###### . ######

> method **`__get__(obj, type=None)`**

> defined at [line 55](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#55)
> ###### . ######

> method **`register(*types)`**

> _Decorator to register an implementation for a specific set of types.  .register(t1, t2)(f) is equivalent to .register\_func((t1, t2), f)._

> defined at [line 60](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#60)
> ###### . ######

> method **`register_func(types, func)`**

> _Helper to register an implementation._

> defined at [line 71](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#71)
> ###### . ######

> method **`__call__(*args)`**

> _Call the overloaded function._

> defined at [line 76](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#76)
> ###### . ######

> method **`find_func(types)`**

> _Find the appropriate overloaded function; don't call it.  This won't work for old-style classes or classes without__mro__._

> defined at [line 84](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/overloading.py#84)
> ###### . ######

