#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 20, 4);
int rst = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  pinMode(rst, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.setCursor(0, 0);
  int scaled = ((long long int)analogRead(rst))*100/1023;
  lcd.print(scaled);
  delay(500);
  lcd.clear();

}
