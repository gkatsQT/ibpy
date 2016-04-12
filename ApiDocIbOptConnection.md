### Connection(object) (class) ###

Encapsulates a connection to TWS.

class defined at [line 25](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#25)

> method **`__init__(host, port, clientId, receiver, sender)`**

> _Constructor._

```
    host: name of host for connection; default is localhost
    port: port number for connection; default is 7496
    clientId: client identifier to send when connected
```

> defined at [line 29](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#29)
> ###### . ######

> method **`__getattr__(name)`**

```
    returns: named attribute from instance receiver or sender
```

> defined at [line 42](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#42)
> ###### . ######

> method **`connect()`**

> _Establish a connection to TWS with instance attributes._

```
    returns: True if connected, otherwise raises an exception
```

> defined at [line 56](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#56)
> ###### . ######

> method **`disconnect()`**

> _Disconnect from TWS_

```
    returns: True if disconnected, False otherwise
```

> defined at [line 64](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#64)
> ###### . ######

> method **`enableLogging(enable=True)`**

> _Enable or disable logging of all messages._

```
    enable: if True (default), enables logging; otherwise disables
    returns: True if enabled, False otherwise
```

> defined at [line 71](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#71)
> ###### . ######

> method **`logMessage(message)`**

> _Format and send a message values to the logger._

```
    message: instance of Message
    returns: None
```

> defined at [line 84](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#84)
> ###### . ######

> method **`create(host='localhost', port=7496, clientId=0, receiver=None,  sender=None)`**

> _Creates and returns Connection class (or subclass) instance._

```
    host: name of host for connection; default is localhost
    port: port number for connection; default is 7496
    clientId: client identifier to send when connected
    returns: Connection (or subclass) instance
```

> defined at [line 94](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/connection.py#94)
> ###### . ######

