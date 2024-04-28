int cds1 = A0;
int cds2 = A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(cds1, INPUT);
  pinMode(cds2, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(cds1));
  Serial.print(" ");
  Serial.print(analogRead(cds2));
  Serial.println();
  delay(500);

}
