#!/usr/bin/env python
""" Defines the ContracDetails class.

"""
from ib.lib import setattrs


class ContractDetails(object):
    """ ContractDetails(...) -> contract details 

    """
    def __init__(self,
                 summary=None,
                 marketName='', 
                 tradingClass='', 
                 conId=0, 
                 minTick=0,
                 multiplier='',
                 priceMagnifier=0,
                 orderTypes='', 
                 validExchanges=''):
        if summary is None:
            summary = Contract()
        setattrs(self, locals())


    def __str__(self):
        return 'Details(%s)' % (self.summary, )