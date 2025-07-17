
const int potpin = 15;
const int ledPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin,OUTPUT);
  
}
void loop() {
  int potvalue = analogRead(potPin);
  int brightness = map(potValue, 0, 4095, 0, 255);

  analohWrite(ledPin, brightness);
  delay(10);
  Serial.printIn(brightness);

  
