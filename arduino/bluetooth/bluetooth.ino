int ldvm=8, ldam=9,ldvd=10;

void setup(){
  pinMode(ldvm, OUTPUT);
  pinMode(ldam, OUTPUT);
  pinMode(ldvd, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()){
    char tc = Serial.read();
    switch(tc){
      case'1':
      digitalWrite(ldvm, 1);
      digitalWrite(ldam, 0);
      digitalWrite(ldvd, 0);
      break;
      case'2':
      digitalWrite(ldvm, 0);
      digitalWrite(ldam, 1);
      digitalWrite(ldvd, 0);
      break;
      case'3':
      digitalWrite(ldvm, 0);
      digitalWrite(ldam, 0);
      digitalWrite(ldvd, 1);
      break;
      case'0':
      digitalWrite(ldvm, 0);
      digitalWrite(ldam, 0);
      digitalWrite(ldvd, 0);
      break;
    }
  }
}