# Synopsis #

```
from ib.ext.EWrapper import EWrapper
from ib.ext.EClientSocket import EClientSocket

class SomeWrapper(EWrapper):
    def tickPrice(self, tickerId, field, price, canAutoExecute):
        ... code to handle tickPrice data ...

    ... code to implement all other EWrapper methods ...

wrapper = SomeWrapper()
connection = EClientSocket(wrapper)
connection.eConnect('localhost', 7496, 0)
connection.reqIds()
... additional requests ...
connection.eDisconnect()
```

# Details #

IbPy is built by automatic translation of the reference Java
implementation supplied by Interactive Brokers.  The generated modules
live in the `ib.ext` package, and provide the same interface as
their Java counterparts.

You can use IbPy just like you would use the IB Java package.  To do
so, you must define a subclass of EWrapper, implement all of its
methods, then provide an instance of your subclass to an EClientSocket
instance.  After you have connected the socket instance, you can call
the TWS API to request account information, market information, place
orders, etc.

Refer to the [IbPy API documentation](http://code.google.com/p/ibpy/w/list?q=label:ApiDoc) and to the
[Interactive Brokers documentation](http://www.interactivebrokers.com/php/webhelp/whnjs.htm) for more information.