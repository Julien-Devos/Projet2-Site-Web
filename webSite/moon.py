#!/usr/bin/env python
"""
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

import math, decimal, datetime
dec = decimal.Decimal

def position(now=None):
   if now is None:
      now = datetime.datetime.now()

   diff = now - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = dec("0.20439731") + (days * dec("0.03386319269"))

   return lunations % dec(1)

def phase_p(pos):
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "New Moon",
      1: "Waxing Crescent",
      2: "First Quarter",
      3: "Waxing Gibbous",
      4: "Full Moon",
      5: "Waning Gibbous",
      6: "Last Quarter",
      7: "Waning Crescent"
   }[int(index) & 7]

def phase(date):
   pos = position(date)
   phasename = phase_p(pos)

   # roundedpos = round(float(pos), 3)
   return phasename

if __name__=="__main__":
   for i in range(1,30):
      print(phase(datetime.datetime(2021,4,i)))