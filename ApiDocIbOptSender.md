### Sender(object) (class) ###

Encapsulates an EClientSocket instance, and proxies attribute lookup to it.

class defined at [line 14](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/sender.py#14)

> method **`connect(host, port, clientId, handler, clientType=EClientSocket)`**

> _Creates a TWS client socket and connects it._

```
    host: name of host for connection; default is localhost
    port: port number for connection; default is 7496
    clientId: client identifier to send when connected
    handler: object to receive reader messages
    returns: True if connected, False otherwise
```

> defined at [line 21](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/sender.py#21)
> ###### . ######

> method **`disconnect()`**

> _Disconnects the client._

```
    returns: True if disconnected, False otherwise
```

> defined at [line 38](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/sender.py#38)
> ###### . ######

> method **`__getattr__(name)`**

```
    returns: named attribute from EClientSocket object
```

> defined at [line 49](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/sender.py#49)
> ###### . ######

