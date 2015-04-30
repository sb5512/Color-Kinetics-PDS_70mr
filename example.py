from PDS_70mr.PDS_70mr import PDS_70mr
import time

k = 0
x = PDS_70mr('10.33.157.51', 6038)
while k < 5:
  x.turn_on(4 , 00 , 7 , 80)
  time.sleep(0.5)
  x.turn_on(4 , 255 , 0 , 0)
  time.sleep(0.5)
  k = k + 1
x.turn_on(4 , 00 , 00 , 00)