#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Keypad.h>
#include <Servo.h>

#define servoPin 11

#define pass_length 8

char data[pass_length];
char master[pass_length] = "12345678";

byte count = 0;

char customKey;

LiquidCrystal_I2C lcd(0x27, 16, 2);

const byte ROWS = 4; // four rows
const byte COLS = 3; // four columns
char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'D', '0', '=',}
};
byte rowPins[ROWS] = {9, 8, 7, 6}; // connect to the row pinouts of the keypad
byte colPins[COLS] = {5, 4, 3}; // connect to the column pinouts of the keypad

Keypad customKeypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

Servo myservo;

int pos = 0;

void setup() {
  lcd.backlight();
  lcd.init();
  delay(2000);
  lcd.clear();
  myservo.attach(11);
}

void loop() {
  lcd.setCursor(0,0);
  lcd.print("Enter Password: ");
  customKey = customKeypad.getKey();

  if (customKey){
    if (customKey == '=' && count == pass_length){
      lcd.clear();
      if(!strncmp(data, master, pass_length)){
        lcd.print("Correct");
        myservo.write(190);
        delay(5000);
        myservo.write(0);
    }else {
      lcd.print("Incorrect");
      delay(1000);
    }
    lcd.clear();
    ClearData();
  }else if(count < pass_length){
    data[count] = customKey;
    lcd.setCursor(count,1);
    lcd.print('*');
    count++;
    }
  }
}


void ClearData(){
  while (count != 0) {
    data[count--] = 0;
  }
  return;
}

