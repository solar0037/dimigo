int digits[4] = {3, 4, 5, 6};
int segments[7] = {7, 8, 9, 10, 11, 12, 13};
char ns[4][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}  // 3
};

void setup() {
  // put your setup code here, to run once:
  for (int i=0; i<4; i++) pinMode(digits[i], OUTPUT);
  for (int i=0; i<7; i++) pinMode(segments[i], OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  // 3
  digitalWrite(digits[0], LOW);
  digitalWrite(digits[1], HIGH);
  digitalWrite(digits[2], HIGH);
  digitalWrite(digits[3], HIGH);
  for (int i=0; i<7; i++) digitalWrite(segments[i], ns[3][i]);
  delay(5);

  // 3
  digitalWrite(digits[0], HIGH);
  digitalWrite(digits[1], LOW);
  digitalWrite(digits[2], HIGH);
  digitalWrite(digits[3], HIGH);
  for (int i=0; i<7; i++) digitalWrite(segments[i], ns[3][i]);
  delay(5);

  // 2
  digitalWrite(digits[0], HIGH);
  digitalWrite(digits[1], HIGH);
  digitalWrite(digits[2], LOW);
  digitalWrite(digits[3], HIGH);
  for (int i=0; i<7; i++) digitalWrite(segments[i], ns[2][i]);
  delay(5);

  // 3
  digitalWrite(digits[0], HIGH);
  digitalWrite(digits[1], HIGH);
  digitalWrite(digits[2], HIGH);
  digitalWrite(digits[3], LOW);
  for (int i=0; i<7; i++) digitalWrite(segments[i], ns[3][i]);
  delay(5);

}
