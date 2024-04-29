#include <SPI.h>
#include <RH_RF95.h>

#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3

RH_RF95 rf95(RFM95_CS, RFM95_INT);

void setup() {
  Serial.begin(9600);
  while (!Serial);

  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  if (!rf95.init()) {
    Serial.println("RFM95 LoRa radio initialization failed!");
    while (1);
  }
  Serial.println("RFM95 LoRa radio initialization successful!");

  rf95.setTxPower(23, false);  // Set the transmitter power to 23dBm (optional)
}

void loop() {
  if (rf95.available()) {
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf95.recv(buf, &len)) {
      Serial.print("Received message: ");
      Serial.println((char*)buf);
    }
  }
}
