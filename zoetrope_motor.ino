// モーター制御
const int motorA = 7;
const int motorB = 8;
const int PWM_mot = 9;
void setup(){
  pinMode(3,OUTPUT);
  pinMode(motorA,OUTPUT); //信号用ピン
  pinMode(motorB,OUTPUT); //信号用ピン
  Serial.begin(9600);

}

void loop(){
    int val;
    val = map(analogRead(0), 0, 1023, 100, 250);
    digitalWrite(motorA,HIGH);
    digitalWrite(motorB,LOW);
    analogWrite(PWM_mot,val);
    Serial.println(val);
    //for(int i=100; i<180; i++){
    //   analogWrite(PWM_mot,i);
    //   delay(1600);
    //   Serial.println(i);
    //}
    //for(int i=180; i>100; i--){
    //   analogWrite(PWM_mot,i);
    //   delay(1600);
    //   Serial.println(i);
    //}
}
