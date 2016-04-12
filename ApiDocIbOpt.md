# Description #


Use:
```
   from ib.opt import ibConnection, message

   def my_callback(msg):
       ...

   con = ibConnection()
   con.register(my_callback, message.TickSize, message.TickPrice)
   con.connect()
   con.reqAccountUpdates(...)
   ...
   con.unregister(my_callback, message.TickSize)
```

Enable and disable logging:

```
   con.enableLogging()
   ...
   con.enableLogging(False)
```

### ibConnection (variable) ###

> _This is the preferred client interface to this module. Alternatively, the Connection type can be sub-classed an its 'create' classmethod reused._

defined at [line 37](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/__init__.py#37)
###### . ######

