#include <SPI.h>
#include <RH_RF95.h>

#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3

// Initialize the RFM95 module
RH_RF95 rf95(RFM95_CS, RFM95_INT);

void setup() {
    Serial.begin(9600);
    while (!Serial) {
        ; // Wait for the serial port to connect. Needed for native USB port only
    }

    pinMode(RFM95_RST, OUTPUT);
    digitalWrite(RFM95_RST, HIGH);

    // Reset the RFM95 module
    delay(10);
    digitalWrite(RFM95_RST, LOW);
    delay(10);
    digitalWrite(RFM95_RST, HIGH);
    delay(10);

    if (!rf95.init()) {
        Serial.println("RFM95 LoRa radio initialization failed!");
        while (1);
    }

    Serial.println("RFM95 LoRa radio initialization successful!");
}

void loop() {
    if (Serial.available() > 0) {
        Serial.println("Reading serialized data from Python...");

        // Read data from the serial port
        String input = Serial.readStringUntil('\n'); // Assuming data ends with a newline character

        // Debug print the received data
        Serial.println("Received data:");
        Serial.println(input);

        // Now transmit the data via LoRa
        Serial.println("Transmitting via LoRa...");
        rf95.send((uint8_t *)input.c_str(), input.length());
        rf95.waitPacketSent();

        Serial.println("Data transmitted via LoRa");
    }
}
