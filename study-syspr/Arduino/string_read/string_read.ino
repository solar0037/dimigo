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
//    char c = Serial.read();
    String led = readstring();
    delay(50);
    Serial.println(led);
    if (led == "off\n") { // all off
      digitalWrite(red, LOW); // 디지털 핀 10 LOW 설정
      digitalWrite(green, LOW); // 디지털 핀 11 LOW 설정
      digitalWrite(blue, LOW); // 디지털 핀 12 LOW 설정
    } else if (led == "red\n") { // red on
      digitalWrite(red, HIGH); // 디지털 핀 10 HIGH 설정
      digitalWrite(green, LOW); // 디지털 핀 11 LOW 설정
      digitalWrite(blue, LOW); // 디지털 핀 12 LOW 설정
    } else if (led == "green\n") { // green on
      digitalWrite(red, LOW); // 디지털 핀 10 LOW 설정
      digitalWrite(green, HIGH); // 디지털 핀 11 HIGH 설정
      digitalWrite(blue, LOW); // 디지털 핀 12 LOW 설정
    } else if (led == "blue\n") { // blue on
      digitalWrite(red, LOW); // 디지털 핀 10 LOW 설정
      digitalWrite(green, LOW); // 디지털 핀 11 LOW 설정
      digitalWrite(blue, HIGH); // 디지털 핀 12 HIGH 설정
    } else if (led == "white\n") { // all on
      digitalWrite(red, HIGH); // 디지털 핀 10 HIGH 설정
      digitalWrite(green, HIGH); // 디지털 핀 11 HIGH 설정
      digitalWrite(blue, HIGH); // 디지털 핀 12 HIGH 설정
    }
  }

}

String readstring() {
  char chari;
  String stro = "";
  while (Serial.available() > 0) {
    chari = Serial.read();
    delay(5);
    stro += chari;
  }
  return stro;
}
