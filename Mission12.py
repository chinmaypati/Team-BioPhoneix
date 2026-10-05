from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()

Left_Drive_Wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Right_Drive_Wheel = Motor(Port.E, Direction.CLOCKWISE)
Left_Attachment_Motor = Motor(Port.B, Direction.CLOCKWISE)
Right_Attachment_Motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(Left_Drive_Wheel, Right_Drive_Wheel, 62.4, 151.0)

def Mission12():
    drive_base.reset(0, 0)
    drive_base.straight(525)
    Right_Attachment_Motor.run_angle(200, -250)
    drive_base.straight(-184)
    Right_Attachment_Motor.run_angle(200, 250)
    drive_base.turn(-25)
    drive_base.straight(400)
    drive_base.turn(123)


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

Mission12()
