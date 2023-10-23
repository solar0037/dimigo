int cds_onoff = A0;
int cds_signal = A1;
int buff[100] = {};
int result[100] = {};
int CDS_CONST_1 = 1000;
int CDS_CONST_2 = 600;

bool is_on = false;

int i;
int j;

const int morse[11][100] = {
  {1, 0, 1, 1, 1}, // a
  {1}, // e
  {1, 1, 1, 0, 1, 1, 1, 0, 1}, // g
  {1, 0, 1}, // i
  {1, 1, 1, 0, 1, 1, 1}, // m
  {1, 1, 1, 0, 1}, // n
  {1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1}, // p
  {1, 0, 1, 1, 1, 0, 1}, // r
  {1, 0, 1, 0, 1}, // s
  {1, 1, 1}, // t
  {1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1} // y
};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(cds_onoff, INPUT);
  pinMode(cds_signal, INPUT);
  i = 0;
  j = 0;

  emptyarr(buff, 100);
  fillarr(morse[0], 5, 100);
  fillarr(morse[1], 1, 100);
  fillarr(morse[2], 9, 100);
  fillarr(morse[3], 3, 100);
  fillarr(morse[4], 7, 100);
  fillarr(morse[5], 5, 100);
  fillarr(morse[6], 11, 100);
  fillarr(morse[7], 7, 100);
  fillarr(morse[8], 5, 100);
  fillarr(morse[9], 3, 100);
  fillarr(morse[10], 13, 100);

  for (int k=0; k<100; k++) Serial.print(buff[k]);
  Serial.println();
  Serial.println(buff[0] == 0);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (is_on == 0) {
    if (analogRead(cds_onoff) < CDS_CONST_1){
      is_on = !is_on;
      Serial.println("START!!!");
      delay(10); // 99
    }
  } else {
    if (analogRead(cds_onoff) >= CDS_CONST_1){
      is_on = !is_on;
      Serial.println("END!!!");
      delay(10); // 9
    }
  }

  if (is_on) {
    delay(10); // 9
    int sig = analogRead(cds_signal);
    if (sig < CDS_CONST_2) buff[i] = 1;
    else buff[i] = 0;
    
    Serial.print("buff: ");
    Serial.println(buff[i]);
//    for (int k=0; k<100; k++) Serial.print(buff[k]);
//    Serial.println();
    
    // check three gaps
    if (i>=2) {
      if ((buff[i-2] == 0) && (buff[i-1] == 0) && (buff[i] == 0)) {
        // check character
        if (comparr(buff, morse[0], 100)) Serial.print('a');
        if (comparr(buff, morse[1], 100)) Serial.print('e');
        if (comparr(buff, morse[2], 100)) Serial.print('g');
        if (comparr(buff, morse[3], 100)) Serial.print('i');
        if (comparr(buff, morse[4], 100)) Serial.print('m');
        if (comparr(buff, morse[5], 100)) Serial.print('n');
        if (comparr(buff, morse[6], 100)) Serial.print('p');
        if (comparr(buff, morse[7], 100)) Serial.print('r');
        if (comparr(buff, morse[8], 100)) Serial.print('s');
        if (comparr(buff, morse[9], 100)) Serial.print('t');
        if (comparr(buff, morse[10], 100)) Serial.print('y');
        else Serial.println('?');
        
        emptyarr(buff, 100);
        i = 0;
      }
    }
    i++;
    delay(90);
  }

}

int comparr(int a[], int b[], int n) {
  for (int k=0; k<n; k++) {
    if (a[k] != b[k]) return 0;
  } return 1;
}

int emptyarr(int* a, int n) {
  // init -1
  for (int k=0; k<n; k++) a[k] = -1;
}

int fillarr(int*a, int start, int fin) {
  for (int k=start; k<fin; k++) a[k] = -1;
}
