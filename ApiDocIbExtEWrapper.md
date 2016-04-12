### EWrapper(AnyWrapper) (class) ###

generated source for EWrapper

class defined at [line 18](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#18)

> method **`tickPrice(tickerId, field, price, canAutoExecute)`**

> defined at [line 23](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#23)
> ###### . ######

> method **`tickSize(tickerId, field, size)`**

> defined at [line 26](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#26)
> ###### . ######

> method **`tickOptionComputation(tickerId,  field,  impliedVol,  delta,  modelPrice,  pvDividend)`**

> defined at [line 29](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#29)
> ###### . ######

> method **`tickGeneric(tickerId, tickType, value)`**

> defined at [line 37](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#37)
> ###### . ######

> method **`tickString(tickerId, tickType, value)`**

> defined at [line 40](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#40)
> ###### . ######

> method **`tickEFP(tickerId,  tickType,  basisPoints,  formattedBasisPoints,  impliedFuture,  holdDays,  futureExpiry,  dividendImpact,  dividendsToExpiry)`**

> defined at [line 43](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#43)
> ###### . ######

> method **`orderStatus(orderId,  status,  filled,  remaining,  avgFillPrice,  permId,  parentId,  lastFillPrice,  clientId,  whyHeld)`**

> defined at [line 54](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#54)
> ###### . ######

> method **`openOrder(orderId, contract, order, orderState)`**

> defined at [line 66](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#66)
> ###### . ######

> method **`openOrderEnd()`**

> defined at [line 69](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#69)
> ###### . ######

> method **`updateAccountValue(key, value, currency, accountName)`**

> defined at [line 72](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#72)
> ###### . ######

> method **`updatePortfolio(contract,  position,  marketPrice,  marketValue,  averageCost,  unrealizedPNL,  realizedPNL,  accountName)`**

> defined at [line 75](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#75)
> ###### . ######

> method **`updateAccountTime(timeStamp)`**

> defined at [line 85](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#85)
> ###### . ######

> method **`accountDownloadEnd(accountName)`**

> defined at [line 88](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#88)
> ###### . ######

> method **`nextValidId(orderId)`**

> defined at [line 91](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#91)
> ###### . ######

> method **`contractDetails(reqId, contractDetails)`**

> defined at [line 94](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#94)
> ###### . ######

> method **`bondContractDetails(reqId, contractDetails)`**

> defined at [line 97](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#97)
> ###### . ######

> method **`contractDetailsEnd(reqId)`**

> defined at [line 100](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#100)
> ###### . ######

> method **`execDetails(reqId, contract, execution)`**

> defined at [line 103](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#103)
> ###### . ######

> method **`execDetailsEnd(reqId)`**

> defined at [line 106](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#106)
> ###### . ######

> method **`updateMktDepth(tickerId,  position,  operation,  side,  price,  size)`**

> defined at [line 109](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#109)
> ###### . ######

> method **`updateMktDepthL2(tickerId,  position,  marketMaker,  operation,  side,  price,  size)`**

> defined at [line 117](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#117)
> ###### . ######

> method **`updateNewsBulletin(msgId, msgType, message, origExchange)`**

> defined at [line 126](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#126)
> ###### . ######

> method **`managedAccounts(accountsList)`**

> defined at [line 129](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#129)
> ###### . ######

> method **`receiveFA(faDataType, xml)`**

> defined at [line 132](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#132)
> ###### . ######

> method **`historicalData(reqId,  date,  open,  high,  low,  close,  volume,  count,  WAP,  hasGaps)`**

> defined at [line 135](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#135)
> ###### . ######

> method **`scannerParameters(xml)`**

> defined at [line 147](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#147)
> ###### . ######

> method **`scannerData(reqId,  rank,  contractDetails,  distance,  benchmark,  projection,  legsStr)`**

> defined at [line 150](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#150)
> ###### . ######

> method **`scannerDataEnd(reqId)`**

> defined at [line 159](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#159)
> ###### . ######

> method **`realtimeBar(reqId,  time,  open,  high,  low,  close,  volume,  wap,  count)`**

> defined at [line 162](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#162)
> ###### . ######

> method **`currentTime(time)`**

> defined at [line 173](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#173)
> ###### . ######

> method **`fundamentalData(reqId, data)`**

> defined at [line 176](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#176)
> ###### . ######

> method **`deltaNeutralValidation(reqId, underComp)`**

> defined at [line 179](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#179)
> ###### . ######

> method **`tickSnapshotEnd(reqId)`**

> defined at [line 182](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapper.py#182)
> ###### . ######

