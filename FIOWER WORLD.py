# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:02:09 2022

@author: ian
"""

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos() 
    mc.setBlocks(x+1,y,z+1,x-1,y,z-1,38)
    time.sleep(0.2)
