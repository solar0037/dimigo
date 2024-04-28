int red = 10;
int green = 11;
int blue = 12;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(red, OUTPUT); // 디지털 핀 10을 출력핀으로 설정
  pinMode(green, OUTPUT); // 디지털 핀 11을 출력핀으로 설정
  pinMode(blue, OUTPUT); // 디지털 핀 12을 출력핀으로 설정

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '0') { // all off
      digitalWrite(red, LOW); // 디지털 핀 10 LOW 설정
      digitalWrite(green, LOW); // 디지털 핀 11 LOW 설정
      digitalWrite(blue, LOW); // 디지털 핀 12 LOW 설정
    } else if (c == '1') { // red on
      digitalWrite(red, HIGH); // 디지털 핀 10 HIGH 설정
      digitalWrite(green, LOW); // 디지털 핀 11 LOW 설정
      digitalWrite(blue, LOW); // 디지털 핀 12 LOW 설정
    } else if (c == '2') { // green on
      digitalWrite(red, LOW); // 디지털 핀 10 LOW 설정
      digitalWrite(green, HIGH); // 디지털 핀 11 HIGH 설정
      digitalWrite(blue, LOW); // 디지털 핀 12 LOW 설정
    } else if (c == '3') { //blue on
      digitalWrite(red, LOW); // 디지털 핀 10 LOW 설정
      digitalWrite(green, LOW); // 디지털 핀 11 LOW 설정
      digitalWrite(blue, HIGH); // 디지털 핀 12 HIGH 설정
    } else if (c == '9') { // all on
      digitalWrite(red, HIGH); // 디지털 핀 10 HIGH 설정
      digitalWrite(green, HIGH); // 디지털 핀 11 HIGH 설정
      digitalWrite(blue, HIGH); // 디지털 핀 12 HIGH 설정
    }
  }

}
