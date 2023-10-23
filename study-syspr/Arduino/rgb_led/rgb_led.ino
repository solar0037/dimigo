void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT); // 디지털 핀 10을 출력핀으로 설정
  pinMode(11, OUTPUT); // 디지털 핀 11을 출력핀으로 설정
  pinMode(12, OUTPUT); // 디지털 핀 12을 출력핀으로 설정

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(10, HIGH); // 디지털 핀 10 HIGH 설정
  delay(1000); // 1초 기다리기
  digitalWrite(10, LOW); // 디지털 핀 10 LOW 설정
  
  digitalWrite(11, HIGH); // 디지털 핀 11 HIGH 설정
  delay(1000); // 1초 기다리기
  digitalWrite(11, LOW); // 디지털 핀 11 LOW 설정

  digitalWrite(12, HIGH); // 디지털 핀 12 HIGH 설정
  delay(1000); // 1초 기다리기
  digitalWrite(12, LOW); // 디지털 핀 12 LOW 설정

}
