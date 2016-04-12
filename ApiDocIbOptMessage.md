### isWrapperMethod(name, value) (function) ###

_Predicate for wrapper methods._

```
  name: name of class attribute as string
  value: value of class attribute; any object
  returns: True if wrapper method
```

defined at [line 107](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#107)
###### . ######

### selectWrapperMethods(cls) (function) ###

_Wrapper methods of a class._

```
  cls: class object to inspect
  returns: list of two-tuples, each (name, argnames)
```

defined at [line 119](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#119)
###### . ######

### buildMessageTypes(wrapper, mapping, **bases) (function) ###**

_Construct message types and add to given mapping._

```
  wrapper: class object to inspect for methods
  mapping: dictionary for adding new message types
  bases: sequence of base classes for message types
  returns: None
```

defined at [line 134](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#134)
###### . ######

### messageTypeNames() (function) ###

_Builds set of message type names._

```
  returns: set of all message type names as strings
```

defined at [line 158](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#158)
###### . ######

### MessageType(type) (class) ###

MessageType -> simple metaclass to track Message subclasses  As new Message subclasses are defined (see below), they are saved to the registry mapping.

class defined at [line 25](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#25)

> method **`__init__(name, bases, namespace)`**

> _Constructor._

```
    name: name of newly created type
    bases: tuple of base classes for new type
    namespace: dictionary with namespace of new type
```

> defined at [line 31](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#31)
> ###### . ######

### Message(object) (class) ###

Base class of all Message types.

class defined at [line 45](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#45)

> method **`__init__(**kwds)`**

> _Constructor._

```
    **kwds: keywords and values for instance
```

> defined at [line 52](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#52)
> ###### . ######

> method **`__len__()`**

> defined at [line 61](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#61)
> ###### . ######

> method **`__str__()`**

> defined at [line 67](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#67)
> ###### . ######

> method **`items()`**

> _List of message (slot, slot value) pairs, as 2-tuples._

```
    returns: list of 2-tuples, each slot (name, value)
```

> defined at [line 75](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#75)
> ###### . ######

> method **`values()`**

> _List of instance slot values._

```
    returns: list of each slot value
```

> defined at [line 82](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#82)
> ###### . ######

> method **`keys()`**

> _List of instance slots._

```
    returns: list of each slot.
```

> defined at [line 89](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#89)
> ###### . ######

### Error(Message) (class) ###

Specialized message type.  The error family of method calls can't be built programmatically, so we define one here.

class defined at [line 97](http://code.google.com/p/ibpy/source/browse/trunk/ib/opt/message.py#97)

