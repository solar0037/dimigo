int cds = A0;
int led = 9;

void setup() {
  // put your setup code here, to run once:
  pinMode(cds, INPUT);
  pinMode(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int light = analogRead(cds);
  if (light < 200) digitalWrite(led, HIGH);
  else digitalWrite(led, LOW);

}
