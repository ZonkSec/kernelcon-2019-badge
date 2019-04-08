#include <APA102.h>

// Define which pins to use.
const uint8_t dataPin = 4;
const uint8_t clockPin = 1;
int mode = 0;
int secret_mode = 0;
int r = 0;
int g = 0;
int b = 0;
// "nedry.tech"  -> "https://62616467650d0a.kernelcon.org/" in binary
byte message[] = {0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0};
//dinoID d09468528e
byte message1[] = {0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1};
int interupted = 0;

// Create an object for writing to the LED strip.
APA102<dataPin, clockPin> ledStrip;

// Set the number of LEDs to control.
const uint16_t ledCount = 5;

// Create a buffer for holding the colors (3 bytes per color).
rgb_color colors[ledCount];

// Set the brightness to use (the maximum is 31).
uint8_t brightness = 5;

void setup()
{
    SREG  = 0b1000000;     // enables Global Interrupt Enable bit
    GIMSK = 0b01000000;    // turns on external interrupts
    MCUCR = 0b00000010;    // sets inntrupt to be falling edge
    PCMSK = 0b00001000;    // turn on interrupts on pins PB0
    sei();                 // enables interrupts
}

//**********************************************************************************************
// MAIN LOOP - operates the menu based on a counter intremented by interupt button press
// counter then calls into a function to handle that specific mode. checks for secret state first
//***********************************************************************************************
void loop()
{
    interupted = 0;
    if (secret_mode > 100) // if button pushed enough times, enters secret mode where it blinks out DINO-ID
    {
      binaryBlink(message1,136);
    }
    else{
      switch (mode){
        case 0: //MODE: each color fades rainbow independtly
          rainbow(70);
          break;
        case 1: //MODE: each color fades rainbow together
          ledStrip.write(colors, ledCount, brightness);
          break;
        case 2: //MODE: each color fades rainbow together
          rainbow(0);
          break;
        case 3: //MODE: each color fades rainbow together
          ledStrip.write(colors, ledCount, brightness);
          break;
        case 4: //MODE blinks out badge chal URL
          binaryBlink(message,80);
          break;
        case 5: //MODE strobes colors together
          party();
          break;
        case 6: //MODE chase LED, color change each loop
          party_chase();
          break;  
      }
    }
}

void solid_color(int r, int g, int b){
  if(interupted == 1) {
    return;
  }
  for(uint16_t i = 0; i < ledCount; i++){
    colors[i].red = g;
    colors[i].green = b;
    colors[i].blue = r;
  }
  ledStrip.write(colors, ledCount, brightness);
}

rgb_color hsvToRgb(uint16_t h, uint8_t s, uint8_t v){
    uint8_t f = (h % 60) * 255 / 60;
    uint8_t p = (255 - s) * (uint16_t)v / 255;
    uint8_t q = (255 - f * (uint16_t)s / 255) * (uint16_t)v / 255;
    uint8_t t = (255 - (255 - f) * (uint16_t)s / 255) * (uint16_t)v / 255;
    uint8_t r = 0, g = 0, b = 0;
    switch((h / 60) % 6){
        case 0: r = v; g = t; b = p; break;
        case 1: r = q; g = v; b = p; break;
        case 2: r = p; g = v; b = t; break;
        case 3: r = p; g = q; b = v; break;
        case 4: r = t; g = p; b = v; break;
        case 5: r = v; g = p; b = q; break;
    }
    return rgb_color(r, g, b);
}

void rainbow(int x){
  uint8_t time = millis() >> 4;
  for(uint16_t i = 0; i < ledCount; i++)
  {
    uint8_t p = time - i * x; //seems to be the delay between LEDs. low they all change together, higer they are more seperate
    colors[i] = hsvToRgb((uint32_t)p * 359 / 256, 255, 255);
  }
  ledStrip.write(colors, ledCount, brightness);
  //delay(10);
}

void binaryBlink(byte code[], int codeLength) {
    solid_color(0,0,255);
    delay(50);
    for(int index = 0; index < codeLength; index++) {
      if(interupted == 1) {
            return;
      }
        if(code[index] == 0) {
            solid_color(255,0,0);
            delay(50);
        }
        else {
            solid_color(0,255,0);
            delay(50);
        }

       if(interupted == 1) {
        return;
        }
        solid_color(0,0,0);
        delay(50);
    }
}

void party(){
    solid_color(55,0,0);delay(10);
    solid_color(0,255,0);delay(10);
    solid_color(0,0,255);delay(10);
    solid_color(255,255,0);delay(10);
    solid_color(0,255,255);delay(10);
    solid_color(255,0,255);delay(10);
    //solid_color(192,192,192);delay(5);
    //solid_color(128,128,128);delay(5);
    solid_color(128,0,0);delay(10);
    solid_color(128,128,0);delay(10);
    solid_color(0,128,0);delay(10);
    solid_color(128,0,128);delay(10);
    solid_color(0,128,128);delay(10);
    solid_color(0,0,128);delay(10);
  }
  
void party_chase(){
    chase(55,0,0);
    chase(0,255,0);
    chase(0,0,255);
    chase(255,255,0);
    chase(0,255,255);
    chase(255,0,255);
    chase(192,192,192);
    chase(128,128,128);
    chase(128,0,0);
    chase(128,128,0);
    chase(0,128,0);
    chase(128,0,128);
    chase(0,128,128);
    chase(0,0,128);
}

void chase(int r, int g, int b){
  for(uint16_t x = 0; x < ledCount; x++){
      if(interupted == 1) {
        return;
      }
      for(uint16_t i = 0; i < ledCount; i++){
        if(interupted == 1) {
           return;
        }
        colors[i].red = 0;
        colors[i].green = 0;
        colors[i].blue = 0;
      }
      colors[x].red = g;
      colors[x].green = b;
      colors[x].blue = r;
      ledStrip.write(colors, ledCount, brightness);
      if(interupted == 1) {
            return;
      }
  delay(5);
  }

}

// interupt function. gets called when button is pressed.
ISR(INT0_vect)
{
      mode++;
      secret_mode++;
      mode = mode%7;
      delay(10); //debounce delay
      interupted = 1;
      return;
}
