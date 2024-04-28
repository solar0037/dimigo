void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); // 디지털 핀 13을 출력핀으로 설정

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH); // 디지털 핀 13 HIGH 설정
  delay(1000); // 1초 기다리기
  digitalWrite(13, LOW); // 디지털 핀 13 LOW 설정
  delay(1000); // 1초 기다리기

}
