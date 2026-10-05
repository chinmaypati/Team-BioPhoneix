from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()

Left_Drive_Wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Right_Drive_Wheel = Motor(Port.F, Direction.CLOCKWISE)
Left_Attachment_Motor = Motor(Port.A, Direction.CLOCKWISE)
Right_Attachment_Motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(Left_Drive_Wheel, Right_Drive_Wheel, 62.4, 151.0)

def Mission8():
    drive_base.reset(0, 0)
    drive_base.straight(610)
    drive_base.turn(90)
    drive_base.straight(310)
    drive_base.turn(-90)
    Right_Attachment_Motor.run_angle(3000, 275)
    drive_base.straight(50)
    Right_Attachment_Motor.run_angle(3000, -120)
    drive_base.straight(-70)

def Mission9():


# The main program starts here.
prime_hub.imu.reset_heading(0)
drive_base.use_gyro(True)
drive_base.settings(straight_speed=500)
drive_base.settings(turn_rate=300)
drive_base.settings(straight_acceleration=300)
drive_base.settings(turn_acceleration=150)
Left_Drive_Wheel.control.target_tolerances(25, 0)
Right_Drive_Wheel.control.target_tolerances(25, 0)
Left_Drive_Wheel.control.limits(acceleration=300)
Right_Drive_Wheel.control.limits(acceleration=300)

Mission8()
Mission9()



def Mission2():
    drive_base.reset(0, 0)
    # Heading straight to MIssion 2
    drive_base.straight(150)
    drive_base.turn(-40)
    #drive_base.turn(-41)
    #drive_base.straight(180, then=Stop.COAST)
    Right_Attachment_Motor.run_angle(100, 1400)
    drive_base.turn(30)
    Left_Attachment_Motor.run_angle(1000, 1400)
    print(prime_hub.imu.heading())
    print(drive_base.distance())
    drive_base.reset(0, 0)
