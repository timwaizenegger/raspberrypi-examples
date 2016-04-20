/*
 * 
 * This is not finished, use the python version instead.
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
	//printf("interrupt!S"); fflush (stdout);
	int now = micros();
	int delay = now - timerStart;
	printf("%f\n", delay / 58.0);	fflush (stdout); 
	
	//cm = pulseIn(PECHO, HIGH) / 58.0; //Echo time convert to cm
	//cm = (int(cm * 100.0)) / 100.0; //Keep two decimal places
}


int main(void)
{
	printf("Raspberry Pi distance measure\n");

	wiringPiSetupGpio();
	pinMode(PTRIG, OUTPUT);
	//pinMode(PECHO, INPUT);
	//pullUpDnControl(PECHO,PUD_DOWN);
	wiringPiISR(PECHO, INT_EDGE_RISING, &interruptHandler);
  	printf("callback registered\n");



	
	
	for(;;)
	{
	digitalWrite(PTRIG, LOW); //Send a voltage pulse to TrigPin
	delayMicroseconds(2);
	digitalWrite(PTRIG, HIGH);
	delayMicroseconds(10);
	digitalWrite(PTRIG, LOW);
	timerStart = micros();
	
	delay(200);
		
	}


  return 0 ;
}
