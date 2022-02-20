int RelayControl3 = 13;
int RelayControl2 = 12;
int RelayControl1 = 11;
int RelayControl0 = 10;

int button0 = 2;
int button1 = 3;
int button2 = 4;
int button3 = 5;

int buttonVal0 = 0;
int buttonVal1 = 0;
int buttonVal2 = 0;
int buttonVal3 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(RelayControl0, OUTPUT);
  pinMode(RelayControl1, OUTPUT);
  pinMode(RelayControl2, OUTPUT);
  pinMode(RelayControl3, OUTPUT);

  pinMode(button0, INPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  buttonVal0 = digitalRead(button0);
  buttonVal1 = digitalRead(button1);
  buttonVal2 = digitalRead(button2);
  buttonVal3 = digitalRead(button3);

  if (buttonVal0 == 1)
  {
    digitalWrite(RelayControl0, HIGH);
    Serial.write("\nPump 0 on!");
  }

  else
    digitalWrite(RelayControl0, LOW);

  if (buttonVal1 == 1)
  {
    digitalWrite(RelayControl1, HIGH);
    Serial.write("\nPump 1 on!");
  }

  else
    digitalWrite(RelayControl1, LOW);

  if (buttonVal2 == 1)
  {
    digitalWrite(RelayControl2, HIGH);
    Serial.write("\nPump 2 on!");
  }

  else
    digitalWrite(RelayControl2, LOW);

  if (buttonVal3 == 1)
  {
    digitalWrite(RelayControl3, HIGH);
    Serial.write("\nPump 3 on!");
  }

  else
    digitalWrite(RelayControl3, LOW);
  
}
