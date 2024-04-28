int in1 = 4;
int in2 = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(in1, OUTPUT); // 디지털 핀 4을 출력핀으로 설정
  pinMode(in2, OUTPUT); // 디지털 핀 5을 출력핀으로 설정

}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (Serial.available() > 0) {
    String led = readstring();
    delay(50);
    Serial.println(led);
    if (led == "00\n") {
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
    } else if (led == "01\n") {
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
    } else if (led == "10\n") {
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
    } else if (led == "11\n") {
      digitalWrite(in1, HIGH);
      digitalWrite(in2, HIGH);
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
