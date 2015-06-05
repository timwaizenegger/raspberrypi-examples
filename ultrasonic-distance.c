/*
 * blink.c:
 *	Standard "blink" program in wiringPi. Blinks an LED connected
 *	to the first GPIO pin.
 *
 * Copyright (c) 2012-2013 Gordon Henderson. <projects@drogon.net>
 ***********************************************************************
 * This file is part of wiringPi:
 *	https://projects.drogon.net/raspberry-pi/wiringpi/
 *
 *    wiringPi is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU Lesser General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    wiringPi is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU Lesser General Public License for more details.
 *
 *    You should have received a copy of the GNU Lesser General Public License
 *    along with wiringPi.  If not, see <http://www.gnu.org/licenses/>.
 ***********************************************************************
 */

#include <stdio.h>
#include <wiringPi.h>

// LED Pin - wiringPi pin 0 is BCM_GPIO 17.

#define	PTRIG 17
#define PECHO 18

int timerStart = 0;

void interruptHandler(void)
{
	int now = micros();
	int delay = now - timerStart;
	printf("%d", delay);	
	
	//cm = pulseIn(PECHO, HIGH) / 58.0; //Echo time convert to cm
	//cm = (int(cm * 100.0)) / 100.0; //Keep two decimal places
}


int main(void)
{
	printf("Raspberry Pi distance measure\n");

	wiringPiSetupGpio();
	pinMode(PTRIG, OUTPUT);
	pinMode(PECHO, INPUT);
	pullUpDnControl(PECHO,PUD_DOWN);
	wiringPiISR(PECHO, INT_EDGE_RISING, &interruptHandler);
  	


	digitalWrite(PTRIG, LOW); //Send a voltage pulse to TrigPin
	delayMicroseconds(2);
	digitalWrite(PTRIG, HIGH);
	delayMicroseconds(10);
	timerStart = micros();
	digitalWrite(PTRIG, LOW);
	
	
	for(;;)
	{
		
	}


  return 0 ;
}
