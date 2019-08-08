
import numpy as np

def BinPacking(data, container):

   data = sorted(data, reverse=True)
   bins = []

   maxValue = container[]

   for item in data:
       # Try to fit item into a bin
       for bin in bins:
           if bin.sum + item <= maxValue:
               # print 'Adding', item, 'to', bin
               bin.append(item)
               break
       else:
           # item didn't fit into any bin, start a new bin
           # print 'Making new bin for', item
           bin = BinC.Bin()
           bin.append(item)
           bins.append(bin)

   return bins