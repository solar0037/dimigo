int a = 6;
int b = 7;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(a, OUTPUT); // 디지털 핀 6을 출력핀으로 설정
  pinMode(b, OUTPUT); // 디지털 핀 7을 출력핀으로 설정

}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (Serial.available() > 0) {
    String led = readstring();
    delay(50);
    Serial.println(led);

    int led_a = led[0] - '0'; // 문자 -> 숫자
    int led_b = led[1] - '0'; // 문자 -> 숫자
    
    if (led_a == 0) digitalWrite(a, LOW);
    else digitalWrite(a, HIGH);
    if (led_b == 0) digitalWrite(b, LOW);
    else digitalWrite(b, HIGH);
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
