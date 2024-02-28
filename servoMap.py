#This is my current servo mapping settings. (02/28/2024) These figures may change over time and this document is being created as a backup copy for my own usage. 
#Please only use these figures as reference if viewing this document as you mapping values may not be the same as mine. 

###Notes###
#All "Input" Min/Max settings are (Input Min: 0 / Input Max: 180) unless listed otherwise.
#All servos are NOT inverted, unless listed otherwise. Example: "Invert: Yes"

######EYES######
Servo: LeftEyeLR
Arduino: ArduinoHead
Pin: 45
TimeOut: 3
Output Min: 75
Output Max: 115
Rest: 90

Servo: LeftEyeUD
Arduino: ArduinoHead
Pin: 44
TimeOut: 3
Output Min: 70
Output Max: 110
Rest: 90

Servo: RightEyeLR
Arduino: ArduinoHead
Pin: 41
TimeOut: 3
Output Min: 75
Output Max: 115
Rest: 90

Servo: RightEyeUD
Arduino: ArduinoHead
Pin: 40
Invert: YES
TimeOut: 3
Output Min: 70
Output Max: 110
Rest: 90

######EYELIDS######
Servo: LeftEyelidUpper
Arduino: ArduinoHead
Pin: 43
TimeOut: 3
Output Min: 66
Output Max: 95
Rest: 90

Servo: LeftEyelidLower
Arduino: ArduinoHead
Pin: 42
Invert: Yes
TimeOut: 3
Output Min: 65
Output Max: 93
Rest: 90

Servo: RightEyelidUpper
Arduino: ArduinoHead
Pin: 39
Invert: Yes
TimeOut: 3
Output Min: 93
Output Max: 122
Rest: 90

Servo: RightEyelidLower
Arduino: ArduinoHead
Pin: 38
TimeOut: 3
Output Min: 83
Output Max: 111
Rest: 90

######EYEBROWS######
Servo: LeftOuterEyebrow
Arduino: ArduinoHead
Pin: 33
TimeOut: 3
Output Min: 68
Output Max: 144
Rest: 90

Servo: LeftInnerEyebrow
Arduino: ArduinoHead
Pin: 32
Invert: Yes 
TimeOut: 3
Output Min: 68
Output Max: 132
Rest: 90

Servo: RightOuterEyebrow
Arduino: ArduinoHead
Pin: 31
Invert: Yes 
TimeOut: 3
Output Min: 68
Output Max: 144
Rest: 90

Servo: RightInnerEyebrow
Arduino: ArduinoHead
Pin: 30
TimeOut: 3
Output Min: 68
Output Max: 132
Rest: 90

######JAW######
Servo: Jaw 
Arduino: ArduinoHead
Pin: 36
TimeOut: 3
Output Min: 71
Output Max: 100
Rest: 0

Servo: LateralJaw
Arduino: ArduinoHead
Pin: 37
TimeOut: 3
Output Min: 67
Output Max: 105
Rest: 90

######NECK & STOMACH######
Servo: Neck
Arduino: ArduinoLeft
Pin: 12
TimeOut: 2
Output Min: 30
Output Max: 120
Rest: 90

Servo: NeckRoll
Arduino: ArduinoRight
Pin: 12
Invert: Yes
TimeOut: 3
Output Min: 53
Output Max: 117
Rest: 90

Servo: NeckRot
Arduino: ArduinoHead
Pin: 35
TimeOut: 5
Output Min: 45
Output Max: 141
Rest: 90

Servo: StomTop
Arduino: ArduinoLeft
Pin: 27
TimeOut: 3
Output Min: 64
Output Max: 110
Rest: 90

Servo: StomMid
Arduino: ArduinoLeft
Pin: 28
TimeOut: 3
Output Min: 60
Output Max: 120
Rest: 90

######LEFT ARM & HAND######
Servo: LeftArmBicep
Arduino: ArduinoLeft
Pin: 8
TimeOut: 5
Output Min: 9
Output Max: 89
Rest: 0

Servo: LeftArmRotate
Arduino: ArduinoLeft
Pin: 9
TimeOut: 5
Input Min: 52
Input Max: 175
Output Min: 52
Output Max: 175
Rest: 90

Servo: LeftArmShoulder
Arduino: ArduinoLeft
Pin: 10
TimeOut: 8
Output Min: 0
Output Max: 180
Rest: 30

Servo: LeftArmOmoplate
Arduino: ArduinoLeft
Pin: 11
TimeOut: 3
Output Min: 10
Output Max: 80
Rest: 0

Servo: LeftHandThumb
Arduino: ArduinoLeft
Pin: 2
TimeOut: 5
Output Min: 0
Output Max: 160
Rest: 0

Servo: LeftHandIndex
Arduino: ArduinoLeft
Pin: 3
TimeOut: 5
Output Min: 0
Output Max: 165
Rest: 0

Servo: LeftHandMiddle
Arduino: ArduinoLeft
Pin: 4
TimeOut: 5
Output Min: 0
Output Max: 166
Rest: 0

Servo: LeftHandRing
Arduino: ArduinoLeft
Pin: 5
TimeOut: 5
Output Min: 0 
Output Max: 148
Rest: 0

Servo: LeftHandPinky
Arduino: ArduinoLeft
Pin: 6
TimeOut: 5 
Output Min: 0
Output Max: 135
Rest: 0

Servo: LeftHandWrist
Arduino: ArduinoLeft
Pin: 7
TimeOut: 5 
Output Min: 0
Output Max: 180
Rest: 0

######RIGHT ARM AND HAND######
Servo: RightArmBicep
Arduino: ArduinoRight
Pin: 8
TimeOut: 5
Output Min: 10
Output Max: 80
Rest: 0

Servo: RightArmRotate
Arduino: ArduinoRight
Pin: 9
TimeOut: 5
Input Min: 50
Input Max: 170
Output Min: 45
Output Max: 165
Rest: 90

Servo: RightArmShoulder
Arduino: ArduinoRight
Pin: 10
TimeOut: 7
Output Min: 0
Output Max: 180
Rest: 30

Servo: RightArmOmoplate
Arduino: ArduinoRight
Pin: 11
TimeOut: 3
Output Min: 8
Output Max: 80
Rest: 0

Servo: RightHandThumb
Arduino: ArduinoRight
Pin: 2
TimeOut: 5 
Output Min: 0
Output Max: 144
Rest: 0

Servo: RightHandIndex
Arduino: ArduinoRight
Pin: 3
TimeOut: 5 
Output Min: 0 
Output Max: 180
Rest: 0

Servo: RightHandMiddle
Arduino: ArduinoRight
Pin: 4
TimeOut: 5 
Output Min: 0
Output Max: 164
Rest: 0

Servo: RightHandRing
Arduino: ArduinoRight
Pin: 5
TimeOut: 5 
Output Min: 0
Output Max: 140
Rest: 0

Servo: RightHandPinky
Arduino: ArduinoRight
Pin: 6
TimeOut: 5 
Output Min: 0 
Output Max: 160
Rest: 0

Servo: RightHandWrist
Arduino: ArduinoRight
Pin: 7
TimeOut: 5 
Output Min: 0
Output Max: 180
Rest: 180
