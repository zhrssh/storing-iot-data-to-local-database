#include "ESP_MICRO.h"

#define SSID "wifi-ssid"
#define PASS "wifi-password"

#define TEMP_SENSE A0
#define LDR D0
#define LED D1

#define DEVICE_ID "1234567"

class Data {
    String deviceId;
    float tempValue;
    int ldrValue;

    public: 
    Data(float tempValue, int ldrValue)
    {
      this->deviceId = DEVICE_ID;
      this->tempValue = tempValue;
      this->ldrValue = ldrValue;
    }

    String GetDeviceID() {
      return deviceId;
    }

    float GetTempValue() {
      return tempValue;
    }

    String ConstructData(){
      String data = "";
      data += DEVICE_ID;
      data += "$";
      data += String(tempValue);
      data += "$";
      data += String(ldrValue);

      return data;
    }
};

void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);

    pinMode(LDR, INPUT);
    pinMode(LED, OUTPUT);
  
    start(SSID, PASS);
  
    digitalWrite(LED, HIGH);
}

void loop() {
    // put your main code here, to run repeatedly:

    // Waits for request
    waitUntilNewReq();

    // Read LDR
    int ldrValue = digitalRead(LDR);

    // Read temperature sensor
    float reading = analogRead(TEMP_SENSE);
    float tempC = (reading * (3300.0 / 1023.0)) / 10.0;

    // Constructs the data
    Data d(tempC, ldrValue);
  
    // Transmit data to the requester
    returnThisStr(d.ConstructData());
}
