
/*	Author: lab
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #  Exercise #
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif


int main(void){
    DDRA = 0x00; PORTA = 0x0F; // Configure port A's 8 pins as inputs
    DDRC = 0xFF; PORTC = 0x00; // Configure port C's 8 pins as outputs, initialize to 0s
    unsigned char cntavail = 0x00; // Hold how many parking spots are available
    unsigned char tmpA = 0x00; // Temporary variable to hold the value of A
    while(1) {
	// 1) Read input
	tmpA = PINA & 0x0F;
	1111 1111 //PINA
	0000 1111 //0x0F
      =
	0x0F =tmpA
	// 2) Perform computation
	// if no parking spots taken cnt = 4
        if (PINA == 0x00){
                cntavail = (cntavail & 0x00) | 0x04;
        	// cnt: 0000 0000
		// 0x0F:0000 0000
		//      (0000 0000) | 0000 0010
	}
	// if one spot is taken
	else if (tmpA == 0x01 || tmpA == 0x02 || tmpA == 0x04 || tmpA == 0x08){
		cntavail = (cntavail & 0x00) | 0x03;
	}
	// if two spots are taken
	else if (tmpA == 0x03 || tmpA == 0x06 || tmpA == 0x0C || tmpA == 0x05 || tmpA == 0x09 || tmpA == 0x0A){
        	cntavail = (cntavail & 0x00) | 0x02;
	} 
	// if three spots are taken 
	else if(tmpA ==  0x07 || tmpA == 0x0B || tmpA == 0x0D || tmpA == 0x0E){
		cntavail = (cntavail & 0x00) | 0x01;
	}
	// if four spots are taken
	else{
		cntavail = (cntavail & 0x00) | 0x00;
	}
	// 3) Write output
        PORTC = cntavail;
    }
    return 0;

}
