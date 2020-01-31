#include <SoftwareSerial.h>
const byte rxpin=10;
const byte txpin=11;
SoftwareSerial ESP8266(rxpin,txpin);

String NomduReseauWifi ="wifi"; // Garder les guillements
String MotDePasse      = "jamal123"; // Garder les guillements
unsigned long lastTimeMillis = 0;
/****************************************************************/
/*                             INIT                             */
/****************************************************************/
const byte TRIGGER_PIN = 2; // Broche TRIGGER
const byte ECHO_PIN = 3;    // Broche ECHO
 
/* Constantes pour le timeout */
const unsigned long MEASURE_TIMEOUT = 25000UL; // 25ms = ~8m à 340m/s

/* Vitesse du son dans l'air en mm/us */
const float SOUND_SPEED = 340.0 / 1000;

void setup()
{
  Serial.begin(9600);
  ESP8266.begin(115200);
  pinMode(TRIGGER_PIN, OUTPUT);
  digitalWrite(TRIGGER_PIN, LOW); // La broche TRIGGER doit être à LOW au repos
  pinMode(ECHO_PIN, INPUT);
  initESP8266();
}
/****************************************************************/
/*                        BOUCLE INFINIE                        */
/****************************************************************/
void loop()
{  
  float d= getDistance();
  sendRequest("192.168.43.148","/users/setSensor/?id=1&val="+ String((int)d),"8000");
  delay(2000);

}
/****************************************************************/
/*                Fonction qui initialise l'ESP8266             */
/****************************************************************/
void initESP8266()
{  
  Serial.println("**********************************************************");  
  Serial.println("**************** DEBUT DE L'INITIALISATION ***************");
  Serial.println("**********************************************************");  
  envoieAuESP8266("AT+RST");
  recoitDuESP8266(2000);
  Serial.println("**********************************************************");
  envoieAuESP8266("AT+CWMODE=3");
  recoitDuESP8266(5000);
  Serial.println("**********************************************************");
  envoieAuESP8266("AT+CWJAP=\""+ NomduReseauWifi + "\",\"" + MotDePasse +"\"");
  recoitDuESP8266(10000);
  Serial.println("**********************************************************");
  envoieAuESP8266("AT+CIFSR");
  recoitDuESP8266(1000);
  Serial.println("**********************************************************");
  envoieAuESP8266("AT+CIPMUX=1");   
  recoitDuESP8266(1000);
  Serial.println("**********************************************************");
  envoieAuESP8266("AT+CIPSERVER=1,80");
  recoitDuESP8266(1000);
  Serial.println("**********************************************************");
  Serial.println("***************** INITIALISATION TERMINEE ****************");
  Serial.println("**********************************************************");
  Serial.println("");  
}

/****************************************************************/
/*        Fonction qui envoie une commande à l'ESP8266          */
/****************************************************************/
void envoieAuESP8266(String commande)
{  
  ESP8266.println(commande);
}
/****************************************************************/
/*Fonction qui lit et affiche les messages envoyés par l'ESP8266*/
/****************************************************************/
void recoitDuESP8266(const int timeout)
{
  String reponse = "";
  long int time = millis();
  while( (time+timeout) > millis())
  {
    while(ESP8266.available())
    {
      char c = ESP8266.read();
      reponse+=c;
    }
  }
  Serial.print(reponse);   
}

void printResponse() {
  while (ESP8266.available()) {
    Serial.println(ESP8266.readStringUntil('\n')); 
  }
}
// sending request to server 
void sendRequest(String host,String path,String port){
    Serial.println("sending request............");
    ESP8266.println("AT+CIPMUX=1");
    delay(1000);
    printResponse();
    ESP8266.println("AT+CIPSTART=4,\"TCP\",\""+host+"\","+port);
    delay(1000);
    printResponse();
    String cmd = "GET " + path +" HTTP/1.1";
    ESP8266.println("AT+CIPSEND=4," + String(cmd.length() + 4));
    delay(1000);
    ESP8266.println(cmd);
    delay(1000);
    ESP8266.println(""); 
    Serial.println("end request............");
    
    
  }

// get distance of capteur utrason
float getDistance(){
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  
  /* 2. Mesure le temps entre l'envoi de l'impulsion ultrasonique et son écho (si il existe) */
  long measure = pulseIn(ECHO_PIN, HIGH, MEASURE_TIMEOUT);
   
  /* 3. Calcul la distance à partir du temps mesuré */
  float distance_mm = measure / 2.0 * SOUND_SPEED;
  Serial.println(distance_mm);

  return distance_mm;

}
  
