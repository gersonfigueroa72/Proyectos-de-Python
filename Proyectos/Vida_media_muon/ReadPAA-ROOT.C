/*
 * ROOT script for read PAA files
 * 
 * @author: Héctor Pérez
 * date: 04/08/2020
 * 
 * Usage:
 * 1. Load this file into root with .L
 * 2. Call the function GetPAAPulse( "FileName.paa", <pulse number> );
 *
 */ 

#include "TGraph.h"
#include "TCanvas.h"

#include <cstdlib>
#include <iostream>
#include <fstream>

void GetPAAPulse(const char* PAAFileName, Int_t PulseNumber)
{
    std::ifstream PAAFile(PAAFileName, std::ios::in | std::ios::binary );
    
    if(!PAAFile)
    {
        std::cout << "Error openning file: " << PAAFileName << std::endl;
        return;
    }

    char ReadBuffer[512];

    PAAFile.getline(ReadBuffer,8);

    if( strcmp(ReadBuffer,"PAA 01") != 0 )
    {
        std::cout << "Invalid file type" << std::endl;
        return;
    }

    PAAFile.seekg(8);
    PAAFile.getline(ReadBuffer,512);
    std::cout << ReadBuffer << std::endl;
    PAAFile.getline(ReadBuffer,512);
    std::cout << ReadBuffer << std::endl;
    PAAFile.getline(ReadBuffer,512);
    std::cout << ReadBuffer << std::endl;
    PAAFile.getline(ReadBuffer,512);
    std::cout << ReadBuffer << std::endl;
    PAAFile.getline(ReadBuffer,512);
    std::cout << ReadBuffer << std::endl;

    std::cout << std::endl;

    PAAFile.seekg(524);
    uint32_t ps;
    PAAFile.read( (char*)&ps, 4);
    std::cout << "Points per pulse: " << ps << std::endl;
    uint32_t pc;
    PAAFile.read( (char*)&pc, 4);
    std::cout << "Pulses in this file: " << pc << std::endl;
    int32_t tl;
    PAAFile.read( (char*)&tl, 4);
    std::cout << "Threshold level: " << tl << std::endl;

    if( ( PulseNumber < 0 ) || ( PulseNumber > (pc-1) ))
    {
        std::cout << "Error: Bad pulse number" << std::endl;
        return;
    }
    
    uint32_t offset = 640 + 2*ps*PulseNumber;
    PAAFile.seekg( offset );
    Int_t pulse_data_v[ps];
    Int_t pulse_data_t[ps];
    uint16_t ipoint;
    for( int i = 0 ; i < ps ; i++ )
    {
        PAAFile.read( (char*)&ipoint, 2);
        if( ipoint > 8191 )
            pulse_data_v[i] = ipoint - 16384;
        else
            pulse_data_v[i] = ipoint;
        pulse_data_t[i] = i;
    }


    TGraph *Pulse = new TGraph( ps, pulse_data_t, pulse_data_v);
	
	TCanvas *ShowGraph = new TCanvas("Pulse", "RP aqcuire tools: ROOT script", 600, 400);
    Pulse->Draw("AC*");
	ShowGraph->Update();

    PAAFile.close();

}
