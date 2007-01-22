#!/usr/bin/env python
""" ib.client.message -> Interactive Brokers client socket reader.

This module plus the reader.py module roughly correspond to the IB TWS
Java Client EReader.java source.

These types provide the logic of reading encoded TWS data and turning
that data into Message objects.  The types inherit the dispatch
method, which they use to send the Message objects to registered
listeners.

The message decoder dispatches its own messages after the message is
decoded from the socket.  This behavior will be expanded to include
message dispatch prior to the socket read.  See ticket #4.
"""
from ib import lib
from ib.types import Contract, ContractDetails, Execution, Order, TickType


logger = lib.logger()


class MessageDecoder(lib.ListenerContainer):
    """ MessageDecoder() -> base class for socket decoders

    Subtypes encapsulate the logic of reading values from a socket
    object encoded by the TWS application.  After instances read data,
    they generate Message objects and send them to registered
    listeners via the dispatch method.
    """
    def __str__(self):
        return self.__class__.__name__


    def preDispatch(self):
        msg = 'PreRead-%s' % (self, )
        for listener in self.preListeners:
            try:
                log('%s%s' % ('    ', msg, ))
                listener(msg)
            except (Exception, ), ex:
                logger.error(str(ex))


    def postDispatch(self, **kwds):
        """ postDispatch(**kwds) -> send a new Message instance to listeners

        """
        for listener in self.postListeners:
            try:
                msg = self.message(**kwds)
                if isinstance(msg, Error.message):
                    log = logger.warning
                else:
                    log = logger.info
                log('%s%s' % ('    ', msg, ))
                listener(msg)
            except (Exception, ), ex:
                logger.error(str(ex))


class Message(object):
    """ Message(**kwds) -> parent type for message classes.

    Subtypes must specify __slots__ for instances to have attributes.
    The keywords specified in the constructor must be present in the
    __slots__ tuple.
    """
    __slots__ = ()

    def __init__(self, **kwds):
        for name, value in kwds.items():
            setattr(self, name, value)


    def __str__(self):
        args = ['%s=%s' % (atr, getattr(self, atr)) for atr in self.__slots__]
        return str.join(' ', args)


class AccountBase(MessageDecoder):
    """ AccountBase() -> parent type for account-related readers

    Using a parent class enables the client to specify a single
    listener for multiple but related readers.
    """
    class message(Message):
        __slots__ = ('key', 'value', 'currency', 'accountName', )


class AccountValue(AccountBase):
    """ AccountValue() -> reads account value messages

    Generated message instance:

    msg.key - name of the account update field
    msg.value - value of the update
    msg.currency - currency type
    msg.accountName - guess!
    """

    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read an account value message

        """
        self.preDispatch()
        version = readInt()
        key = readStr()
        value = readStr()
        currency = readStr()

        accountName = ''
        if version >= 2:
            accountName = readStr()

        self.postDispatch(key=key,
                      value=value,
                      currency=currency,
                      accountName=accountName)


class AccountTime(AccountBase):
    """ AccountTime() -> reads account time stamp messages

    Generated message instance:

    msg.key - 'TimeStamp'
    msg.value - time the broker updated the account
    msg.currency - ""
    """
    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read an account update time message

        """
        self.preDispatch()        
        version = readInt()
        timeStamp = readStr()
        self.postDispatch(key='TimeStamp',
                      value=timeStamp,
                      currency='',
                      accountName='')


class ContractDetails(MessageDecoder):
    """ ContractDetails() -> reads contract detail messages

    Generated message instance:

    msg.details - full description of a contract
    """
    class detail(Message):
        __slots__ = ('details', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a contract details message

        """
        self.preDispatch()        
        details = ContractDetails()

        version = readInt()
        details.summary.symbol = readStr()
        details.summary.secType = readStr()
        details.summary.expiry = readStr()
        details.summary.strike = readFloat()
        details.summary.right = readStr()
        details.summary.exchange = readStr()
        details.summary.currency = readStr()
        details.summary.localSymbol = readStr()
        details.marketName = readStr()
        details.tradingClass = readStr()
        details.conId = readInt()
        details.minTick = readFloat()
        details.multiplier = readStr()
        details.orderTypes = readStr()
        details.validExchanges = readStr()
        if version >= 2:
            details.priceMagnifier = readInt()            
        self.postDispatch(details=details)


class Error(MessageDecoder):
    """ Error() -> reads error messages

    Generated message instance:

    msg.error_id - order id or ticker id that generated the error
    msg.error_code - error codes are documented by IB
    msg.error_msg - textual description of the error, documented by IB
    """
    class message(Message):
        __slots__ = ('error_id', 'error_code', 'error_msg', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read an error message

        """
        self.preDispatch()        
        version = readInt()

        if version < 2:
            error_id = error_code = None
            error_msg = readStr()
        else:
            error_id = readInt()
            error_code = readInt()
            error_msg = readStr()

        self.postDispatch(error_id=error_id, 
                      error_code=error_code, 
                      error_msg=error_msg)


class Execution(MessageDecoder):
    """ Execution() -> reads execution detail messages

    Generated message instance:

    msg.orderId - order id specified in the call to place order
    msg.contract - description of the executed contract 
    msg.details - addition order execution details
    """
    class message(Message):
        __slots__ = ('orderId', 'contract', 'details', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read an execution details message

        """
        self.preDispatch()        
        version = readInt()
        orderId = readInt()        

        contract = Contract()
        contract.symbol = readStr()
        contract.secType = readStr()
        contract.expiry = readStr()
        contract.strike = readFloat()
        contract.right = readStr()
        contract.exchange = readStr()
        contract.currency = readStr()
        contract.localSymbol = readStr()

        details = Execution()
        details.orderId = orderId
        details.execId = readStr()
        details.time = readStr()
        details.acctNumber = readStr()
        details.exchange = readStr()
        details.side = readStr()
        details.shares = readInt()
        details.price = readFloat()
        if version >= 2:
            details.permId = readInt()
        if version >= 3:
            details.clientId = readInt()
        if version >= 4:
            details.liquidation = readInt()

        self.postDispatch(orderId=orderId,
                      contract=contract,
                      details=details)


class ManagedAccounts(MessageDecoder):
    """ ManagedAccounts() -> reads a list of managed account ids

    """
    class message(Message):
        __slots__ = ('accounts', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a managed accounts message

        """
        self.preDispatch()        
        version = readInt()
        accounts = readStr()
        self.postDispatch(accounts=accounts)


class MarketDepth(MessageDecoder):
    """ MarketDepth() -> reads market depth messages

    Generated message instance:

    msg.tickerId - ticker id specified the call to reqMktDepth
    msg.position - specifies the row id of the order
    msg.operation - identifies how this message should be applied to the
                      market depth.  Valid values:
                      0 = insert
                      1 = update
                      2 = delete
    msg.side - side of the book to which this order belongs. Valid values:
                 0 = ask
                 1 = bid
    msg.price - order price
    msg.size - order size
    """
    class message(Message):
        __slots__ = ('tickerId', 'position', 'operation', 
                     'side', 'price', 'size', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a market depth message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        position = readInt()
        operation = readInt()
        side = readInt()
        price = readFloat()
        size = readInt()

        self.postDispatch(tickerId=tickerId,
                      position=position,
                      operation=operation,
                      side=side,
                      price=price,
                      size=size)


class MarketDepthLevel2(MessageDecoder):
    """ MarketDepthLevel2Reader() -> reads level 2 market depth messages

    Generated message instance:

    msg.tickerId - ticker id specified the call to reqMktDepth
    msg.position - specifies the row id of the order
    msg.market_maker - specifies the exchange hosting this order
    msg.operation - identifies how this message should be applied to the
                      market depth.  Valid values:
                      0 = insert
                      1 = update
                      2 = delete
    msg.side - side of the book to which this order belongs. Valid values:
                 0 = ask
                 1 = bid
    msg.price - order price
    msg.size - order size
    """
    class message(Message):
        __slots__ = ('tickerId', 'position', 'market_maker', 'operation', 
                     'side', 'price', 'size', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a market depth level 2 message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        position = readInt()
        market_maker = readStr()
        operation = readInt()
        side = readInt()
        price = readFloat()
        size = readInt()

        self.postDispatch(tickerId=tickerId,
                      position=position,
                      market_maker=market_maker,
                      operation=operation, 
                      side=side,
                      price=price,
                      size=size)


class NextId(MessageDecoder):
    """ NextId() -> reads next valid id messages

    Generated message instance:

    msg.nextValidId - first order id acceptable to the broker
    """
    class message(Message):
        __slots__ = ('nextValidId', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a next order id message

        """
        self.preDispatch()        
        version = readInt()
        nextValidId = readInt()
        self.postDispatch(nextValidId=nextValidId)


class OpenOrder(MessageDecoder):
    """ OpenOrder() -> reads open order messages

    Generated message instance:

    msg.orderId - the order id assigned by the broker
    msg.contract - describes the contract
    msg.order - details of the open order
    """
    class message(Message):
        __slots__ = ('orderId', 'contract', 'order', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read an open order message

        """
        self.preDispatch()        
        version = readInt()        

        order = Order()        
        order.orderId = readInt()

        contract = Contract()
        contract.symbol = readStr()
        contract.secType = readStr()
        contract.expiry = readStr()
        contract.strike = readFloat()
        contract.right = readStr()
        contract.exchange = readStr()
        contract.currency = readStr()
        if version >= 2:
            contract.localSymbol = readStr()
            
        order.action = readStr()
        order.totalQuantity = readInt()
        order.orderType = readStr()
        order.lmtPrice = readFloat()
        order.auxPrice = readFloat()
        order.tif = readStr()
        order.ocaGroup = readStr()
        order.account = readStr()
        order.openClose = readStr()
        order.origin = readInt()
        order.orderRef = readStr()

        if version >= 3:
            order.clientId = readInt()

        if version >= 4:
            order.permId = readInt()
            order.ignoreRth = readInt() == 1
            order.hidden = readInt() == 1
            order.discretionaryAmt = readFloat()

        if version >= 5:
            order.goodAfterTime = readStr()

        if version >= 6:
            order.sharesAllocation = readStr()

        if version >= 7:
            order.faGroup = readStr()
            order.faMethod = readStr()
            order.faPercentage = readStr()
            order.faProfile = readStr()

        if version >= 8:
            order.goodTillDate = readStr()

        if version >= 9:
            order.rule80A = readStr()
            order.percentOffset = readFloat()
            order.settlingFirm = readStr()
            order.shortSaleSlot = readInt()
            order.designatedLocation = readStr()
            order.auctionStrategy = readInt()
            order.startingPrice = readFloat()
            order.stockRefPrice = readFloat()
            order.delta = readFloat()
            order.stockRangeLower = readFloat()
            order.stockRangeUpper = readFloat()
            order.displaySize = readInt()
            order.rthOnly = bool(readInt())
            order.blockOrder = bool(readInt())
            order.sweepToFill = bool(readInt())
            order.allOrNone = bool(readInt())
            order.minQty= readInt()
            order.ocaType = readInt()
            order.eTradeOnly = bool(readInt())
            order.firmQuoteOnly = bool(readInt())
            order.nbboPriceCap = readFloat()

        if version >= 10:
            order.parentId = readInt()
            order.triggerMethod = readInt()

        if version >= 11:
            order.volatility = readFloat()
            order.volatilityType = readInt()
            if version == 11:
                receivedInt = readInt()
                order.deltaNeutralOrderType = receivedInt == 0 and "NONE" or "MKT"
            else:
                order.deltaNeutralOrderType = readStr()
                order.deltaNeutralAuxPrice = readFloat()
            order.continuousUpdate = readInt()

            ## we don't have a way to get the server version yet:
            ## if server version == 26
            #order.stockRangeLower = readFloat()
            #order.stockRangeUpper = readFloat()
            
            order.referencePriceType = readInt()
            
        self.postDispatch(orderId=order.orderId, 
                      contract=contract, 
                      order=order)


class OrderStatus(MessageDecoder):
    """ OrderStatus() -> reads order status messages

    Generated message instance:

    msg.orderId - order id specified previously 
    msg.message - order status
    msg.filled - number of shares executed
    msg.remaining - number of shares still outstanding
    msg.avgFillPrice - average price of executed shares 
    msg.permId - permanent id maintained by the broker
    msg.parentId - parent id for bracket or auto trailing stop orders
    msg.lastFillPrice - price of the last shares executed
    """
    class message(Message):
        __slots__ = ('orderId', 'message', 'filled', 'remaining',
                     'permId', 'parentId', 'lastFillPrice',
                     'avgFillPrice', 'clientId')


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read an order status message

        """
        self.preDispatch()        
        version = readInt()
        orderId = readInt()
        message = readStr()
        filled = readInt()
        remaining = readInt()
        avgFillPrice = readFloat()

        permId = 0
        if version >= 2:
            permId = readInt()

        parentId = 0
        if version >= 3:
            parentId = readInt()

        lastFillPrice = 0
        if version >= 4:
            lastFillPrice = readFloat()

        clientId = 0
        if version >= 5:
            clientId = readInt()

        self.postDispatch(orderId=orderId,
                      message=message,
                      filled=filled,
                      remaining=remaining,
                      avgFillPrice=avgFillPrice,
                      permId=permId,
                      parentId=parentId,
                      lastFillPrice=lastFillPrice,
                      clientId=clientId)


class Portfolio(MessageDecoder):
    """ Portfolio() -> reads portfolio update messages 

    Generated message instance:

    msg.contract - description of the contract
    msg.position - indicates the position on the contract
    msg.market_price - unit price of the instrument
    msg.market_value - total market value of the instrument
    """
    class message(Message):
        __slots__ = ('contract', 'position', 'market_price', 'market_value', 
                     'average_cost', 'unrealized_pnl', 'realized_pnl',
                     'accountName', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a portfolio update message

        """
        self.preDispatch()        
        contract = Contract()

        version = readInt()
        contract.symbol = readStr()
        contract.secType = readStr()
        contract.expiry = readStr()
        contract.strike = readFloat()
        contract.right = readStr()
        contract.currency = readStr()

        if version >= 2:
            contract.localSymbol = readStr()
            
        position = readInt()
        market_price = readFloat()
        market_value = readFloat()

        average_cost = unrealized_pnl = realized_pnl = 0.0
        if version >= 3:
            average_cost = readFloat()
            unrealized_pnl = readFloat()
            realized_pnl = readFloat()

        accountName = ''
        if version >= 4:
            accountName = readStr()

        self.postDispatch(contract=contract,
                      position=position,
                      market_price=market_price,
                      market_value=market_value,
                      average_cost=average_cost,
                      unrealized_pnl=unrealized_pnl,
                      realized_pnl=realized_pnl,
                      accountName=accountName)


class ReaderStart(MessageDecoder):
    """ ReaderStart() -> pseudo message for reader start notification

    Instances do not have a 'read' method, but messages are sent with with
    the 'send' method just the same.  The message layout is:

    msg - unadorned
    """
    class message(Message):
        __slots__ = ()


class ReaderStop(MessageDecoder):
    """ ReaderStart() -> pseudo message for reader stop notification

    Instances do not have a 'read' method, but messages are sent with with
    the 'send' method just the same.  The message layout is:

    msg.exception - string of the exception that stopped the reader
    """
    class message(Message):
        __slots__ = ('exception', )


class TickBase(MessageDecoder):
    """ TickBase() -> parent type for ticker-related readers

    Using a parent class enables the client to specify a single listener 
    for multiple but related readers.
    """
    class message(Message):
        """ Message type tweaked for ticker updates

        TickBase updates are the most frequent message sent by TWS.  This type
        is slightly faster than the Message base class.
        """
        __slots__ = ('tickerId', 'field', 'value', 'canAutoExecute', )

        def __init__(self, tickerId, field, value, canAutoExecute=0):
            self.tickerId = tickerId
            self.field = field
            self.value = value
            self.canAutoExecute = canAutoExecute


class TickPrice(TickBase):
    """ TickPrice() -> reads ticker price messages

    Generated message instance:

    msg.tickerId - ticker id previously specified
    msg.field - type of price (ask, bid, last, etc)
    msg.value - price of indicated field
    msg.canAutoExecute - some type of flag
    """
    sizer = None
    
    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a ticker price message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        tickType = readInt()
        price = readFloat()
        size = 0
        if version >= 2:
            size = readInt()
        canAutoExecute = 0
        if version >= 3:
            canAutoExecute = readInt()
        self.postDispatch(tickerId=tickerId,
                      field=tickType,
                      value=price,
                      canAutoExecute=canAutoExecute)
        if version >= 2:
            sizeTickType = None
            if tickType == TickType.BID:
                sizeTickType = TickType.BID_SIZE
            elif tickType == TickType.ASK:
                sizeTickType = TickType.ASK_SIZE
            elif tickType == TickType.LAST:
                sizeTickType = TickType.LAST_SIZE

            if sizeTickType is not None:
                self.sizer.preDispatch()
                self.sizer.postDispatch(tickerId=tickerId,
                                    field=sizeTickType,
                                    value=size)


class TickSize(TickBase):
    """ TickSize() -> reads ticker size messages

    Generated message instance:

    msg.tickerId - ticker id previously specified
    msg.field - type of size (ask, bid, last, etc)
    msg.value - size of indicated field
    """
    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a ticker size message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        tickType = readInt()
        size = readInt()
        self.postDispatch(tickerId=tickerId,
                      field=tickType,
                      value=size)


class TickOptionComputation(MessageDecoder):
    """ TickOptionComputation() -> reads ticker option computation messages

    """
    class message(Message):
        __slots__ = ('tickerId', 'field', 'impliedVol', 'delta', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a ticker size message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        tickType = readInt()
        impliedVol = readFloat()
        if impliedVol < 0:
            impliedVol = ''
        delta = readFloat()
        if abs(delta) > 1:
            delta = ''
        self.postDispatch(tickerId=tickerId,
                      field=tickType,
                      impliedVol=impliedVol,
                      delta=delta)


class NewsBulletin(MessageDecoder):
    """ NewsBulletin() -> reads news bulletin messages

    """
    class message(Message):
        __slots__ = ('news_id', 'news_type', 'news_message', 'news_exchange')


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a news bulletin message

        """
        self.preDispatch()        
        version = readInt()
        news_id = readInt()
        news_type = readInt()
        news_message = readStr()
        news_exchange = readStr()

        self.postDispatch(news_id=news_id,
                      news_type=news_type,
                      news_message=news_message,
                      news_exchange=news_exchange)


class ReceiveFa(MessageDecoder):
    """ ReceiveFa() -> reads some type of message

    """
    class message(Message):
        __slots__ = ('data_type', 'xml', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a type of message

        """
        self.preDispatch()        
        version = readInt()
        data_type = readInt()
        xml = readStr()
        
        self.postDispatch(data_type=data_type,
                      xml=xml)


class HistoricalData(MessageDecoder):
    """ HistoricalData() -> reads some type of message

    """
    class message(Message):
        __slots__ = ('version', 'tickerId', 'rows' )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a type of message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        nitems = readInt()
        rows = []
        for i in range(nitems):
            #read date,open,high,low,close,volume,wap,hasgaps
            row=[readStr(), readFloat(), readFloat(), readFloat(), readFloat(),
                 readInt(), readFloat(), readStr().lower()=='true']
            rows.append(row)
        self.postDispatch(version=version, tickerId=tickerId, rows=rows)


class BondContractData(MessageDecoder):
    """ BondContractData() -> reads some type of message

    """
    class message(Message):
        __slots__ = ('details', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a type of message

        """
        self.preDispatch()        
        details = ContractDetails()

        version = readInt()
        details.summary.symbol = readStr()
        details.summary.secType = readStr()
        details.summary.cusip = readStr()
        details.summary.coupon = readFloat()
        details.summary.maturity = readStr()
        details.summary.issueDate  = readStr()
        details.summary.ratings = readStr()
        details.summary.bondType = readStr()
        details.summary.couponType = readStr()
        details.summary.convertible = bool(readInt())
        details.summary.callable = bool(readInt())
        details.summary.putable = bool(readInt())
        details.summary.descAppend = readStr()
        details.summary.exchange = readStr()
        details.summary.currency = readStr()
        details.marketName = readStr()
        details.tradingClass = readStr()
        details.conId = readInt()
        details.minTick = readFloat()
        details.orderTypes = readStr()
        details.validExchanges = readStr()
        self.postDispatch(details=details)


class ScannerParameters(MessageDecoder):
    """ ScannerParameters() -> reads some type of message

    """
    class message(Message):
        __slots__ = ('xml', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a type of message

        """
        self.preDispatch()        
        version = readInt()
        xml = readStr()
        self.postDispatch(xml=xml)


class ScannerData(MessageDecoder):
    """ ScannerData() -> reads some type of message

    """
    class message(Message):
        __slots__ = ('tickerId', 'rows', )


    def read(self, readInt, readFloat, readStr):
        """ read(...) -> read a type of message

        """
        self.preDispatch()        
        version = readInt()
        tickerId = readInt()
        elementCount = readInt()
        rows = []

        for i in range(elementCount):
            rank = readInt()            

            contract = ContractDetails()
            contract.summary.symbol = readStr()
            contract.summary.secType = readStr()
            contract.summary.expiry = readStr()
            contract.summary.strike = readFloat()
            contract.summary.right = readStr()
            contract.summary.exchange = readStr()
            contract.summary.currency = readStr()
            contract.summary.localSymbol = readStr()
            contract.marketName = readStr()
            contract.tradingClass = readStr()
            distance = readStr()
            benchmark = readStr()
            projection = readStr()
            rows.append(dict(rank=rank, contract=contract, distance=distance,
                             benchmark=benchmark, projection=projection))

        self.postDispatch(tickerId=tickerId, rows=rows)