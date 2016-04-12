### EWrapperMsgGenerator(AnyWrapperMsgGenerator) (class) ###

generated source for EWrapperMsgGenerator

class defined at [line 19](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#19)

> method **`tickPrice(tickerId, field, price, canAutoExecute)`**

> defined at [line 27](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#27)
> ###### . ######

> method **`tickSize(tickerId, field, size)`**

> defined at [line 31](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#31)
> ###### . ######

> method **`tickOptionComputation(tickerId,  field,  impliedVol,  delta,  modelPrice,  pvDividend)`**

> defined at [line 35](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#35)
> ###### . ######

> method **`tickGeneric(tickerId, tickType, value)`**

> defined at [line 48](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#48)
> ###### . ######

> method **`tickString(tickerId, tickType, value)`**

> defined at [line 52](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#52)
> ###### . ######

> method **`tickEFP(tickerId,  tickType,  basisPoints,  formattedBasisPoints,  impliedFuture,  holdDays,  futureExpiry,  dividendImpact,  dividendsToExpiry)`**

> defined at [line 56](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#56)
> ###### . ######

> method **`orderStatus(orderId,  status,  filled,  remaining,  avgFillPrice,  permId,  parentId,  lastFillPrice,  clientId,  whyHeld)`**

> defined at [line 68](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#68)
> ###### . ######

> method **`openOrder(orderId, contract, order, orderState)`**

> defined at [line 81](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#81)
> ###### . ######

> method **`openOrderEnd()`**

> defined at [line 110](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#110)
> ###### . ######

> method **`updateAccountValue(key, value, currency, accountName)`**

> defined at [line 114](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#114)
> ###### . ######

> method **`updatePortfolio(contract,  position,  marketPrice,  marketValue,  averageCost,  unrealizedPNL,  realizedPNL,  accountName)`**

> defined at [line 118](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#118)
> ###### . ######

> method **`updateAccountTime(timeStamp)`**

> defined at [line 130](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#130)
> ###### . ######

> method **`accountDownloadEnd(accountName)`**

> defined at [line 134](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#134)
> ###### . ######

> method **`nextValidId(orderId)`**

> defined at [line 138](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#138)
> ###### . ######

> method **`contractDetails(reqId, contractDetails)`**

> defined at [line 142](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#142)
> ###### . ######

> method **`contractDetailsMsg(contractDetails)`**

> defined at [line 148](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#148)
> ###### . ######

> method **`contractMsg(contract)`**

> defined at [line 153](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#153)
> ###### . ######

> method **`bondContractDetails(reqId, contractDetails)`**

> defined at [line 158](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#158)
> ###### . ######

> method **`contractDetailsEnd(reqId)`**

> defined at [line 164](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#164)
> ###### . ######

> method **`execDetails(reqId, contract, execution)`**

> defined at [line 168](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#168)
> ###### . ######

> method **`execDetailsEnd(reqId)`**

> defined at [line 173](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#173)
> ###### . ######

> method **`updateMktDepth(tickerId,  position,  operation,  side,  price,  size)`**

> defined at [line 177](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#177)
> ###### . ######

> method **`updateMktDepthL2(tickerId,  position,  marketMaker,  operation,  side,  price,  size)`**

> defined at [line 186](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#186)
> ###### . ######

> method **`updateNewsBulletin(msgId, msgType, message, origExchange)`**

> defined at [line 196](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#196)
> ###### . ######

> method **`managedAccounts(accountsList)`**

> defined at [line 200](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#200)
> ###### . ######

> method **`receiveFA(faDataType, xml)`**

> defined at [line 204](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#204)
> ###### . ######

> method **`historicalData(reqId,  date,  open,  high,  low,  close,  volume,  count,  WAP,  hasGaps)`**

> defined at [line 208](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#208)
> ###### . ######

> method **`realtimeBar(reqId,  time,  open,  high,  low,  close,  volume,  wap,  count)`**

> defined at [line 221](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#221)
> ###### . ######

> method **`scannerParameters(xml)`**

> defined at [line 233](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#233)
> ###### . ######

> method **`scannerData(reqId,  rank,  contractDetails,  distance,  benchmark,  projection,  legsStr)`**

> defined at [line 237](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#237)
> ###### . ######

> method **`scannerDataEnd(reqId)`**

> defined at [line 248](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#248)
> ###### . ######

> method **`currentTime(time)`**

> defined at [line 252](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#252)
> ###### . ######

> method **`fundamentalData(reqId, data)`**

> defined at [line 256](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#256)
> ###### . ######

> method **`deltaNeutralValidation(reqId, underComp)`**

> defined at [line 260](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#260)
> ###### . ######

> method **`tickSnapshotEnd(tickerId)`**

> defined at [line 264](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EWrapperMsgGenerator.py#264)
> ###### . ######

