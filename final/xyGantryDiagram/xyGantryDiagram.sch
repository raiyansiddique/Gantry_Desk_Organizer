EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Driver_Motor:Pololu_Breakout_A4988 StepperMotorDriverForY
U 1 1 639917BE
P 7500 2350
F 0 "StepperMotorDriverForY" H 7550 3231 50  0000 C CNN
F 1 "Pololu_Breakout_A4988" H 7550 3140 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 7775 1600 50  0001 L CNN
F 3 "https://www.pololu.com/product/2980/pictures" H 7600 2050 50  0001 C CNN
	1    7500 2350
	1    0    0    -1  
$EndComp
$Comp
L Driver_Motor:Pololu_Breakout_A4988 StepperMotorDriverForX
U 1 1 63992789
P 7500 4450
F 0 "StepperMotorDriverForX" H 7550 5331 50  0000 C CNN
F 1 "Pololu_Breakout_A4988" H 7550 5240 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 7775 3700 50  0001 L CNN
F 3 "https://www.pololu.com/product/2980/pictures" H 7600 4150 50  0001 C CNN
	1    7500 4450
	1    0    0    -1  
$EndComp
$Comp
L Motor:Stepper_Motor_bipolar M?
U 1 1 63993AC3
P 8600 2750
F 0 "M?" H 8788 2874 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 8788 2783 50  0000 L CNN
F 2 "" H 8610 2740 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 8610 2740 50  0001 C CNN
	1    8600 2750
	1    0    0    -1  
$EndComp
$Comp
L Device:Battery PowerSupply12V
U 1 1 6399BE34
P 10050 2150
F 0 "PowerSupply12V" H 10158 2196 50  0000 L CNN
F 1 "PowerSupply" H 10158 2105 50  0000 L CNN
F 2 "" V 10050 2210 50  0001 C CNN
F 3 "~" V 10050 2210 50  0001 C CNN
	1    10050 2150
	1    0    0    -1  
$EndComp
$Comp
L Motor:Stepper_Motor_bipolar M?
U 1 1 639944CA
P 8600 4900
F 0 "M?" H 8788 5024 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 8788 4933 50  0000 L CNN
F 2 "" H 8610 4890 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 8610 4890 50  0001 C CNN
	1    8600 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	8000 5000 8000 4650
Wire Wire Line
	8000 5000 8300 5000
Wire Wire Line
	8300 4800 8150 4800
Wire Wire Line
	8150 4800 8150 4550
Wire Wire Line
	8150 4550 8000 4550
Wire Wire Line
	8500 4600 8500 4450
Wire Wire Line
	8500 4450 8000 4450
Wire Wire Line
	8700 4600 8700 4350
Wire Wire Line
	8700 4350 8000 4350
Wire Wire Line
	8300 2850 8000 2850
Wire Wire Line
	8000 2850 8000 2550
Wire Wire Line
	8300 2650 8100 2650
Wire Wire Line
	8100 2650 8100 2450
Wire Wire Line
	8100 2450 8000 2450
Wire Wire Line
	8500 2450 8500 2350
Wire Wire Line
	8500 2350 8000 2350
Wire Wire Line
	8700 2450 8700 2250
Wire Wire Line
	8700 2250 8000 2250
Wire Wire Line
	7500 1650 6700 1650
Wire Wire Line
	6700 1650 6700 2300
Wire Wire Line
	6000 2300 6000 2350
Wire Wire Line
	6700 2300 6000 2300
Wire Wire Line
	6700 2300 6700 3750
Wire Wire Line
	6700 3750 7500 3750
Connection ~ 6700 2300
Wire Wire Line
	10050 1950 10050 1650
Wire Wire Line
	10050 1650 9400 1650
Wire Wire Line
	10050 2400 10050 3100
Wire Wire Line
	10050 3100 9900 3100
Wire Wire Line
	7700 3100 7700 3150
Wire Wire Line
	9400 1650 9400 3750
Wire Wire Line
	9400 3750 7700 3750
Connection ~ 9400 1650
Wire Wire Line
	9400 1650 7700 1650
Wire Wire Line
	9900 3100 9900 5250
Wire Wire Line
	9900 5250 7700 5250
Connection ~ 9900 3100
Wire Wire Line
	9900 3100 7700 3100
Wire Wire Line
	5900 5250 6550 5250
Wire Wire Line
	6550 5250 6550 3200
Wire Wire Line
	6550 3200 7500 3200
Wire Wire Line
	7500 3200 7500 3150
Connection ~ 6550 5250
Wire Wire Line
	6550 5250 7500 5250
Wire Wire Line
	7100 2050 6950 2050
Wire Wire Line
	6950 2050 6950 1950
Wire Wire Line
	6950 1950 7100 1950
Wire Wire Line
	7100 4150 6800 4150
Wire Wire Line
	6800 4150 6800 4050
Wire Wire Line
	6800 4050 7100 4050
$Comp
L MCU_Module:Arduino_UNO_R2 A?
U 1 1 63A05909
P 5800 3350
F 0 "A?" H 5800 4531 50  0000 C CNN
F 1 "Arduino_UNO_R2" H 5800 4440 50  0000 C CNN
F 2 "Module:Arduino_UNO_R2" H 5800 3350 50  0001 C CIN
F 3 "https://www.arduino.cc/en/Main/arduinoBoardUno" H 5800 3350 50  0001 C CNN
	1    5800 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 3750 5300 3750
Wire Wire Line
	5300 3850 5100 3850
Wire Wire Line
	5100 3850 5100 4550
Wire Wire Line
	5100 4550 7100 4550
Wire Wire Line
	5000 4750 6850 4750
Wire Wire Line
	6850 4750 6850 4450
Wire Wire Line
	6850 4450 7100 4450
Wire Wire Line
	5000 3750 5000 4750
Wire Wire Line
	5900 4450 5900 5250
Wire Wire Line
	5300 3150 4800 3150
Wire Wire Line
	4800 3150 4800 2100
Wire Wire Line
	4800 2100 6850 2100
Wire Wire Line
	6850 2100 6850 2450
Wire Wire Line
	6850 2450 7100 2450
Wire Wire Line
	7100 2350 6900 2350
Wire Wire Line
	6900 2350 6900 1950
Wire Wire Line
	6900 1950 5100 1950
Wire Wire Line
	5100 1950 5100 3050
Wire Wire Line
	5100 3050 5300 3050
$EndSCHEMATC
