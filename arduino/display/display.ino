#include <LiquidCrystal.h>
int seconds = 0;
LiquidCrystal lcd_1(12,11, 5,4,3,2);

void setup(){
  lcd_1.begin(16, 2);
  lcd_1.print("Hello word");
}

void loop(){
  lcd_1.setCursor(0,1);
  lcd_1.print(seconds);
  delay(1000);
  seconds += 1;

}