#include <Arduino.h>

/* A custom structure to hold the time and action values */
struct TimeAction {
  unsigned long time;
  String action;
};

// Array to store time-action pairs
TimeAction timeActionArray[10];
int numTimeActions = 0;

// Pin numbers related to color sensor:
#define S0_PIN 5
#define S1_PIN 4
#define S2_PIN 7
#define S3_PIN 6
#define OUT_PIN  8

// Pin numbers related to solenoids:
#define SOL1_PIN 10
#define SOL2_PIN 9

// Pin numbers for the arm:
#define A1_PIN 11

// Delays:
int black_delay = 1480;
int white_delay = 2400;
int kaun_delay = 5000;
int solenoid_delay = 100;
int sensor_delay = 1000;

bool sensorIsAvailable = true; // To avoid that the same disk gets scanned multiple times

// Counters for black and white disks:
int black_disks = 0;
int white_disks = 0;

//boolean
bool last = false;

/* This method will run only one time when the programs starts running.
* Here all the initializations are done. */
void setup() {

  // Colorsensor init:
  pinMode(S0_PIN, OUTPUT);
  pinMode(S1_PIN, OUTPUT);
  pinMode(S2_PIN, OUTPUT);
  pinMode(S3_PIN, OUTPUT);
  pinMode(OUT_PIN, INPUT);
  digitalWrite(S0_PIN, HIGH);
  digitalWrite(S1_PIN, LOW);
  Serial.begin(9600);

  // Solenoids init:
  pinMode(SOL1_PIN, OUTPUT);
  pinMode(SOL2_PIN, OUTPUT);

  // Arm init:
  pinMode(A1_PIN, OUTPUT);
  digitalWrite(A1_PIN, LOW);

  //Start timer
  millis();
}

/* This function loops forever. In the beginning of the loop, the red value gets measured.
* After this, we check if the red value is the value for a black disk or a white disk.
* If this is the case, we will put the time in the array when the solenoids need to push
* and we will set both solenoids to high. If we do not do this, the stones cannot pass.
* Then we do a quick check if the array is empty, which means the solenoids
* can relax again with low voltage. Finally, we go through the whole array and check if
* any actions need to be done. */
void loop() {

  if ((black_disks + white_disks) <= 8) {
    int r;
    r = process_red_value();  // Retrieve red value

    //print the red value (for testing):
    Serial.print("red = ");
    Serial.print(r);
    Serial.print(" ");
    Serial.println();

    // Black disk detection:
    if ((r >= 800 && r <= 880) && (sensorIsAvailable)) {
      digitalWrite(SOL1_PIN, HIGH);
      digitalWrite(SOL2_PIN, HIGH);
      black_disks++;
      timeActionArray[numTimeActions].time = millis() + black_delay;
      timeActionArray[numTimeActions].action = "SOL1_push";

      sensorIsAvailable = false;
      timeActionArray[numTimeActions + 1].time = millis() + sensor_delay;
      timeActionArray[numTimeActions + 1].action = "sensor_enable";
      numTimeActions += 2;
    } 
    // White disk detection:
    else if ((r >= 380 && r <= 430) && (sensorIsAvailable)) { 
      digitalWrite(SOL1_PIN, HIGH);
      digitalWrite(SOL2_PIN, HIGH);
      white_disks++;
      timeActionArray[numTimeActions].time = millis() + white_delay;
      timeActionArray[numTimeActions].action = "SOL2_push";

      sensorIsAvailable = false;
      timeActionArray[numTimeActions + 1].time = millis() + sensor_delay;
      timeActionArray[numTimeActions + 1].action = "sensor_enable";
      numTimeActions += 2;
    }

    // Other disk detection:
    //else if ((!(r >= 620 && r <= 700)) && !() && () && (sensorIsAvailable)) {
      //digitalWrite(SOL1_PIN, HIGH);
      //digitalWrite(SOL2_PIN, HIGH);

      //timeActionArray[numTimeActions].time = millis() + kaun_delay;
      //timeActionArray[numTimeActions].action = "SOL12_none";

      //sensorIsAvailable = false;
      //timeActionArray[numTimeActions + 1].time = millis() + sensor_delay;
      //timeActionArray[numTimeActions + 1].action = "sensor_enable";
      //numTimeActions += 2;
    //}

    /* If there is nothing in the array it means there are no stones on the belt,
    * so the solenoids are turned off to avoid overheating */
    if (numTimeActions == 0) {
      digitalWrite(SOL1_PIN, LOW);
      digitalWrite(SOL2_PIN, LOW);
    } 

    // This loops through the whole array
    for (int i = 0; i < numTimeActions; i++) {
      unsigned long actionTime = timeActionArray[i].time;
      String actionType = timeActionArray[i].action;

      // If this is the case it means there needs to be done something
      if (millis() > actionTime) {

        // This action means the solenoids should push out (black disk)
        if (actionType == "SOL1_push") {
          digitalWrite(SOL1_PIN, LOW);

          // The solenoid needs time to push out, so it needs a small delay before it pulls:
          timeActionArray[numTimeActions].time = millis() + solenoid_delay;
          timeActionArray[numTimeActions].action = "SOL1_pull";
          numTimeActions++;
        }

        // This action means the solenoids should push out (white disk)
        if (actionType == "SOL2_push") {
          digitalWrite(SOL2_PIN, LOW);

          // The solenoid needs time to push out, so it needs a small delay before it pulls:
          timeActionArray[numTimeActions].time = millis() + solenoid_delay;
          timeActionArray[numTimeActions].action = "SOL2_pull";
          numTimeActions++;
        }

        // This action means the solenoids should push out after long time (other disk)
        if (actionType == "SOL12_none") {
          numTimeActions++;
        }

        if (actionType == "SOL1_pull") {
          digitalWrite(SOL1_PIN, HIGH);
        }
        if (actionType == "SOL2_pull") {
          digitalWrite(SOL2_PIN, HIGH);
        }

        if (actionType == "sensor_enable") {
          sensorIsAvailable = true;
        }

        // Remove the processed action from the array by shifting the remaining elements
        for (int j = i; j < numTimeActions - 1; j++) {
          timeActionArray[j] = timeActionArray[j + 1];
        }
        numTimeActions--;
      }
    }
  }

  if ((black_disks + white_disks) > 8) {
    int r = process_red_value();  // Retrieve red value

    //print the red value (for testing):
    Serial.print("red = ");
    Serial.print(r);
    Serial.print(" ");
    Serial.println();

    digitalWrite(SOL1_PIN, HIGH);
    digitalWrite(SOL2_PIN, HIGH);

    // Black disk detection:
    if ((r >= 800 && r <= 880)) {
      //raise arm to let disks pass through to other robots
      digitalWrite(A1_PIN, HIGH);
      delay(30);
      delay(black_delay - 200);
      digitalWrite(SOL1_PIN, LOW);
      digitalWrite(SOL2_PIN, LOW);

      last = true;
    }

    // White disk detection:
    if ((r >= 380 && r <= 430)) { //FINISH
      //raise arm to let disks pass through to other robots
      digitalWrite(A1_PIN, HIGH);
      delay(200);
      digitalWrite(A1_PIN, LOW);
      delay(white_delay - 200);
      digitalWrite(SOL1_PIN, LOW);
      digitalWrite(SOL2_PIN, LOW);

      last = true;
    }

    if (last) {
      //stop the rasied arm
      digitalWrite(SOL1_PIN, LOW);
      digitalWrite(SOL2_PIN, LOW);
      delay(10000); //for now increase later
    }
  }
}

/* Function that computes the red value */
int process_red_value() {
  digitalWrite(S2_PIN, LOW);
  digitalWrite(S3_PIN, LOW);
  int pulse_length = pulseIn(OUT_PIN, LOW);
  return pulse_length;
}

int process_green_value() {
  digitalWrite(S2_PIN, HIGH);
  digitalWrite(S3_PIN, HIGH);
  int pulse_length = pulseIn(OUT_PIN, LOW);
  return pulse_length;
}

int process_blue_value() {
  digitalWrite(S2_PIN, LOW);
  digitalWrite(S3_PIN, HIGH);
  int pulse_length = pulseIn(OUT_PIN, LOW);
  return pulse_length;
}