void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop() {
  digitalWrite(5, 0);
  digitalWrite(6, 0);
  delay(2000);
  digitalWrite(5, 0);
  digitalWrite(6, 1);
  delay(2000);
  digitalWrite(5, 1);
  digitalWrite(6, 1);
  delay(2000);
  digitalWrite(5, 1);
  digitalWrite(6, 0);
  delay(2000);
}
