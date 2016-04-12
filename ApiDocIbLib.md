### synchronized(lock) (function) ###

_Synchronization decorator.  from http://wiki.python.org/moin/PythonDecoratorLibrary_

```
  lock: Lock or RLock instance
  returns: decorator that provides automatic locking
```

defined at [line 31](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#31)
###### . ######

### classmethod_(classmethod) (class) ###_

Classmethod that provides attribute delegation.

class defined at [line 19](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#19)

> method **`__init__(func)`**

> defined at [line 23](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#23)
> ###### . ######

> method **`__getattr__(name)`**

> defined at [line 27](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#27)
> ###### . ######

### Boolean(object) (class) ###

Partial implementation of Java Boolean type.

class defined at [line 50](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#50)

> method **`__init__(value)`**

> _Constructor._

```
    value: bool instance, True or False
```

> defined at [line 54](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#54)
> ###### . ######

> method **`booleanValue()`**

> _The value of this instance (a bool)._

```
    returns: True or False
```

> defined at [line 61](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#61)
> ###### . ######

> method **`valueOf(text)`**

> _Creates an instance of this class with a bool value._

```
    cls: this class
    text: string
    returns: instance of cls
```

> defined at [line 69](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#69)
> ###### . ######

### Cloneable(object) (class) ###

Stub for the Cloneable Java interface.  Some of the translated code implements the Java Cloneable interface, but its methods are never used.  We provide this class for sub typing, and will implement methods as needed later.

class defined at [line 80](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#80)

> method **`clone()`**

> defined at [line 87](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#87)
> ###### . ######

### DataInputStream(object) (class) ###

Partial implementation of the Java DataInputStream type.

class defined at [line 91](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#91)

> method **`__init__(stream)`**

> _Constructor._

```
    stream: any object with recv method
```

> defined at [line 95](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#95)
> ###### . ######

> method **`readByte(unpack=struct.unpack)`**

> _Reads a byte from the contained stream._

```
    returns: string read from stream
```

> defined at [line 103](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#103)
> ###### . ######

### DataOutputStream(object) (class) ###

Partial implementation of the Java DataOutputStream type

class defined at [line 111](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#111)

> method **`__init__(stream)`**

> _Constructor._

```
    stream: any object with send method
```

> defined at [line 115](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#115)
> ###### . ######

> method **`write(data, pack=struct.pack, eol=struct.pack('!b', 0))`**

> _Writes data to the contained stream._

```
    data: string to send, or 0
    returns: None
```

> defined at [line 122](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#122)
> ###### . ######

### Double(float) (class) ###

Partial implementation of Java Double type.

class defined at [line 136](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#136)

> method **`parseDouble()`**

> _Float double (float) from string._

```
    text: value to parse
    returns: float instance
```

> defined at [line 145](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#145)
> ###### . ######

### Integer(int) (class) ###

Partial implementation of Java Integer type.

class defined at [line 154](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#154)

> method **`parseInt()`**

> _Int from string._

```
    text: value to parse
    returns: int instance
```

> defined at [line 163](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#163)
> ###### . ######

> method **`parseLong()`**

> _Long from string._

```
    text: value to parse
    returns: long instance
```

> defined at [line 172](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#172)
> ###### . ######

### Socket(socket.socket) (class) ###

Partial implementation of the Java Socket type.

class defined at [line 187](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#187)

> method **`__init__(host, port)`**

> _Constructor; attempts connection immediately._

```
    host: hostname as string
    port: port number as integer
```

> defined at [line 191](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#191)
> ###### . ######

> method **`getInputStream()`**

> _Returns this instance, which has a send method._

> defined at [line 200](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#200)
> ###### . ######

> method **`getOutputStream()`**

> _Returns this instance, which has a recv method._

> defined at [line 206](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#206)
> ###### . ######

> method **`isConnected()`**

> defined at [line 212](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#212)
> ###### . ######

### StringBuffer(list) (class) ###

Partial implementation of the Java StringBuffer type  Translated code uses instances of this type to build up strings. The list base type provides the append method.

class defined at [line 220](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#220)

> method **`__str__(join=str.join, chr=chr)`**

> _the string value of this instance_

```
    returns: string from characters contained in this instance
```

> defined at [line 226](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#226)
> ###### . ######

### ThreadType(QThread) (class) ###

Partial implementation of Java Thread type, based on Qt3 QThread.

class defined at [line 237](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#237)

> method **`__init__(name)`**

> _Constructor._

```
    name: ignored
```

> defined at [line 241](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#241)
> ###### . ######

> method **`interrupt()`**

> _Stop this thread (by call to terminate)._

> defined at [line 248](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#248)
> ###### . ######

> method **`isInterrupted()`**

> _Check state of thread._

```
    returns: True if thread is finished
```

> defined at [line 254](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#254)
> ###### . ######

> method **`setDaemon(value)`**

> _No-op._

```
    value: ignored
    returns: None
```

> defined at [line 261](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#261)
> ###### . ######

> method **`setName(value)`**

> _No-op._

```
    value: ignored
    returns: None
```

> defined at [line 268](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#268)
> ###### . ######

### ThreadType(QThread) (class) ###

Partial implementation of Java Thread type, based on Qt4 QThread.

class defined at [line 280](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#280)

> method **`__init__(name)`**

> _Constructor._

```
    name: ignored
```

> defined at [line 284](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#284)
> ###### . ######

> method **`interrupt()`**

> _stop this thread (by call to exit)_

> defined at [line 291](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#291)
> ###### . ######

> method **`isInterrupted()`**

> _check state of thread_

```
    returns: True if thread is finished
```

> defined at [line 297](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#297)
> ###### . ######

> method **`setDaemon(value)`**

> _No-op._

```
    value: ignored
    returns: None
```

> defined at [line 304](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#304)
> ###### . ######

> method **`setName(value)`**

> _sets the name of this QObject_

```
    value: name of object as string
    returns: None
```

> defined at [line 311](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#311)
> ###### . ######

### ThreadType(threading.Thread) (class) ###

Partial implementation of Java Thread type, based on Python Thread.

class defined at [line 323](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#323)

> method **`__init__(name)`**

> _Constructor._

```
    name: name of this thread
```

> defined at [line 327](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#327)
> ###### . ######

> method **`interrupt()`**

> _No-op; Python threads are not directly interruptible._

> defined at [line 335](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#335)
> ###### . ######

> method **`isInterrupted()`**

> _Check state of thread (always False)._

```
    returns: False
```

> defined at [line 341](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#341)
> ###### . ######

### Thread(ThreadType) (class) ###

Thread parent type, based on available framework

class defined at [line 349](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#349)

> method **`__init__(name, parent, dis)`**

> _Constructor._

```
    name: name of this thread
    parent: ignored
    dis: ignored
```

> defined at [line 353](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#353)
> ###### . ######

> method **`term()`**

> defined at [line 363](http://code.google.com/p/ibpy/source/browse/trunk/ib/lib/__init__.py#363)
> ###### . ######

