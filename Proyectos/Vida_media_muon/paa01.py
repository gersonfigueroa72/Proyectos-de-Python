#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:46:09 2019

@author: hepf
"""
import sys
import os
import struct

class paaFile:
    def __init__(self,FileName):
        
        self.file = open(FileName, "rb" )
        
        # Getting file identifier
    
        identifier = self.file.readline().decode("utf-8")
        if( identifier != "PAA 01\n" ):
            print("Error: Not a PAA file or incompatible file structure")
            sys.exit()
        
        # Reading text headers (5 lines, offset 8 bytes)
    
        self.file.seek(8, 0)
        
        self.t_header = []
        
        self.t_header.append( self.file.readline().decode("utf-8") )
        self.t_header.append( self.file.readline().decode("utf-8") )
        self.t_header.append( self.file.readline().decode("utf-8") )
        self.t_header.append( self.file.readline().decode("utf-8") )
        self.t_header.append( self.file.readline().decode("utf-8") )
        
        # Reading data information (offset 520 bytes)
    
        self.file.seek(520, 0)
        
        # Endianness check
        ecn = struct.unpack('<I', self.file.read(4))[0]
        
        # Points per pulse
        self.ps = struct.unpack('<I', self.file.read(4))[0]
        
        # Pulses in this file
        self.pc = struct.unpack('<I', self.file.read(4))[0]
        
        # Threshold level used
        self.tl = struct.unpack('<i', self.file.read(4))[0]
        
        # Verify that binary data block size is coherent
        
        file_length_in_bytes = os.path.getsize(FileName)
        if( (file_length_in_bytes-640)/(2*self.ps) != float(self.pc) ):
            print("Error: Binary data size is not coherent")
            sys.exit()
            
    def __del__(self): 
        self.file.close() 
        
    def paaGetTextHeader(self,header):
        return self.t_header[header]
    
    def paaGetPulseSize(self):
        return self.ps
    
    def paaGetPulseCount(self):
        return self.pc
    
    def paaGetThresholdLevel(self):
        return self.tl
    
    def paaGetPulseRP(self,pulse_number):
        if( ( pulse_number < 0 ) or (pulse_number > (self.pc-1) )):
            print("Error: Bad pulse number")
            sys.exit()
        offset = 640 + 2*self.ps*(pulse_number)
        self.file.seek(offset, 0)
        pulse_data = []
        for i in range(self.ps):
            ipoint = struct.unpack('<H', self.file.read(2))[0]
            # Data from RedPitaya that uses SteamLab 0.97 API,
            # ie Pulse Aquire pacq, comes in 14 bit signed
            # integers. The following convertion is needed.
            if( ipoint > 8191 ):
                ipoint = ipoint - 16384
            pulse_data.append(ipoint)
        return pulse_data
    
    # Use this method to read data that does not comes
    # from Pulse Aquire pacq utility.
    
    def paaGetPulseRaw(self,pulse_number):
        if( ( pulse_number < 0 ) or (pulse_number > (self.pc-1) )):
            print("Error: Bad pulse number")
            sys.exit()
        offset = 640 + 2*self.ps*(pulse_number)
        self.file.seek(offset, 0)
        pulse_data = []
        for i in range(self.ps):
            ipoint = struct.unpack('<H', self.file.read(2))[0]
            pulse_data.append(ipoint)
        return pulse_data
