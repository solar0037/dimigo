#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 20, 4);

void setup() {
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0,0);
  lcd.print("3323");
  lcd.setCursor(0,1);
  lcd.print("Hojun Sa");
}

void loop() {
}
