#!/usr/bin/python

import socket
import struct

#Note when programming the colour automatically you will have to see the connected light and see each light separetely

class PDS_70mr:
  def __init__(self , destination_ip, port):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM means UDP
    destination_address = ('10.33.157.51', 6038)
    self.socket.connect(destination_address)

  def getSocket(self):
    return self.socket

  def turn_on(self , whichFixture , r , g , b):
	
	  # Make packet data:
	  # - header
      header1 = "0401 dc4a 0100 0101 0000 0000 0000 0000 ffff ffff 00".replace(" ", "").decode('hex') 
      # Port 1. Also note you have to get this data by checking the packet of what is going on the network using Wireshark software.

  	# - RGB data padded to 512 bytes
      rgb = ['0']* 6
      if r <= 15:
        rgb[1] = hex(r)[2:3]
      else:
        rgb[0] = hex(r)[2:3]
        rgb[1] = hex(r)[3:4]

      if g <= 15:
        rgb[3] = hex(g)[2:3]
      else:
        rgb[2] = hex(g)[2:3]
        rgb[3] = hex(g)[3:4]

      if b <= 15:
        rgb[5] = hex(b)[2:3]
      else:
        rgb[4] = hex(b)[2:3]
        rgb[5] = hex(b)[3:4]

      # - RGB data padded to 512 bytes
      rgb_data1 = ['0'] * 512
      whichByte = 6 * (whichFixture - 1)

      for i in range(6):
      	rgb_data1[whichByte + i] = rgb[i]

      rgb_data1_str = ''.join(rgb_data1)
      pkt_data1 = header1 + rgb_data1_str.decode('hex')#struct.pack("6B", *rgb_data1)

	    # Send the packets
      self.socket.send(pkt_data1)

  def programFixturesSequentially(self):
    return   