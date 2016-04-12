### EClientSocket(object) (class) ###

generated source for EClientSocket

class defined at [line 32](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#32)

> method **`faMsgTypeName(faDataType)`**

> defined at [line 45](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#45)
> ###### . ######

> method **`serverVersion()`**

> defined at [line 105](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#105)
> ###### . ######

> method **`TwsConnectionTime()`**

> defined at [line 108](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#108)
> ###### . ######

> method **`wrapper()`**

> defined at [line 111](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#111)
> ###### . ######

> method **`reader()`**

> defined at [line 114](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#114)
> ###### . ######

> method **`__init__(anyWrapper)`**

> defined at [line 117](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#117)
> ###### . ######

> method **`isConnected()`**

> defined at [line 120](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#120)
> ###### . ######

> method **`eConnect(host, port, clientId)`**

> defined at [line 125](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#125)
> ###### . ######

> method **`connectionError()`**

> defined at [line 136](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#136)
> ###### . ######

> method **`checkConnected(host)`**

> defined at [line 140](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#140)
> ###### . ######

> method **`createReader(socket, dis)`**

> defined at [line 148](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#148)
> ###### . ######

> method **`eConnect_0(socket, clientId)`**

> defined at [line 153](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#153)
> ###### . ######

> method **`eDisconnect()`**

> defined at [line 172](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#172)
> ###### . ######

> method **`cancelScannerSubscription(tickerId)`**

> defined at [line 194](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#194)
> ###### . ######

> method **`reqScannerParameters()`**

> defined at [line 211](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#211)
> ###### . ######

> method **`reqScannerSubscription(tickerId, subscription)`**

> defined at [line 227](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#227)
> ###### . ######

> method **`reqMktData(tickerId, contract, genericTickList, snapshot)`**

> defined at [line 267](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#267)
> ###### . ######

> method **`cancelHistoricalData(tickerId)`**

> defined at [line 329](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#329)
> ###### . ######

> method **`cancelRealTimeBars(tickerId)`**

> defined at [line 345](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#345)
> ###### . ######

> method **`reqHistoricalData(tickerId,  contract,  endDateTime,  durationStr,  barSizeSetting,  whatToShow,  useRTH,  formatDate)`**

> defined at [line 362](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#362)
> ###### . ######

> method **`reqRealTimeBars(tickerId,  contract,  barSize,  whatToShow,  useRTH)`**

> defined at [line 421](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#421)
> ###### . ######

> method **`reqContractDetails(reqId, contract)`**

> defined at [line 455](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#455)
> ###### . ######

> method **`reqMktDepth(tickerId, contract, numRows)`**

> defined at [line 487](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#487)
> ###### . ######

> method **`cancelMktData(tickerId)`**

> defined at [line 516](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#516)
> ###### . ######

> method **`cancelMktDepth(tickerId)`**

> defined at [line 530](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#530)
> ###### . ######

> method **`exerciseOptions(tickerId,  contract,  exerciseAction,  exerciseQuantity,  account,  override)`**

> defined at [line 547](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#547)
> ###### . ######

> method **`placeOrder(id, contract, order)`**

> defined at [line 582](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#582)
> ###### . ######

> method **`reqAccountUpdates(subscribe, acctCode)`**

> defined at [line 781](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#781)
> ###### . ######

> method **`reqExecutions(reqId, filter)`**

> defined at [line 797](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#797)
> ###### . ######

> method **`cancelOrder(id)`**

> defined at [line 820](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#820)
> ###### . ######

> method **`reqOpenOrders()`**

> defined at [line 834](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#834)
> ###### . ######

> method **`reqIds(numIds)`**

> defined at [line 847](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#847)
> ###### . ######

> method **`reqNewsBulletins(allMsgs)`**

> defined at [line 861](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#861)
> ###### . ######

> method **`cancelNewsBulletins()`**

> defined at [line 875](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#875)
> ###### . ######

> method **`setServerLogLevel(logLevel)`**

> defined at [line 888](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#888)
> ###### . ######

> method **`reqAutoOpenOrders(bAutoBind)`**

> defined at [line 902](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#902)
> ###### . ######

> method **`reqAllOpenOrders()`**

> defined at [line 916](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#916)
> ###### . ######

> method **`reqManagedAccts()`**

> defined at [line 929](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#929)
> ###### . ######

> method **`requestFA(faDataType)`**

> defined at [line 942](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#942)
> ###### . ######

> method **`replaceFA(faDataType, xml)`**

> defined at [line 959](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#959)
> ###### . ######

> method **`reqCurrentTime()`**

> defined at [line 977](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#977)
> ###### . ######

> method **`reqFundamentalData(reqId, contract, reportType)`**

> defined at [line 993](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#993)
> ###### . ######

> method **`cancelFundamentalData(reqId)`**

> defined at [line 1017](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1017)
> ###### . ######

> method **`error(err)`**

> defined at [line 1035](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1035)
> ###### . ######

> method **`error_0(id, errorCode, errorMsg)`**

> defined at [line 1040](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1040)
> ###### . ######

> method **`close()`**

> defined at [line 1043](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1043)
> ###### . ######

> method **`is_(strval)`**

> defined at [line 1048](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1048)
> ###### . ######

> method **`isNull(strval)`**

> defined at [line 1052](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1052)
> ###### . ######

> method **`error_1(id, pair, tail)`**

> defined at [line 1056](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1056)
> ###### . ######

> method **`send(strval)`**

> defined at [line 1060](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1060)
> ###### . ######

> method **`sendEOL()`**

> defined at [line 1065](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1065)
> ###### . ######

> method **`send_0(val)`**

> defined at [line 1069](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1069)
> ###### . ######

> method **`send_1(val)`**

> defined at [line 1073](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1073)
> ###### . ######

> method **`send_2(val)`**

> defined at [line 1078](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1078)
> ###### . ######

> method **`send_3(val)`**

> defined at [line 1082](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1082)
> ###### . ######

> method **`sendMax(val)`**

> defined at [line 1086](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1086)
> ###### . ######

> method **`sendMax_0(val)`**

> defined at [line 1093](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1093)
> ###### . ######

> method **`send_4(val)`**

> defined at [line 1100](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1100)
> ###### . ######

> method **`IsEmpty(strval)`**

> defined at [line 1104](http://code.google.com/p/ibpy/source/browse/trunk/ib/ext/EClientSocket.py#1104)
> ###### . ######

