# ============================================================
#  ROBOT TEMPLATE  --  4 missions, arrow menu
# ============================================================
#  HOW TO RUN:
#   1. Open https://code.pybricks.com, paste this whole file in.
#   2. Connect the hub and click Download/Run.
#   3. On the hub:  RIGHT arrow = pick a mission (1, 2, 3)
#                   LEFT  arrow = RUN the mission shown
#                   (do NOT press the center button -- it STOPS the program)
# ============================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# ============================================================
#  ROBOT SETUP  --  already calibrated, do not change
# ============================================================

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)   # left wheel
right_motor = Motor(Port.B, Direction.CLOCKWISE)          # right wheel
motor_c = Motor(Port.C)                                   # attachment C
motor_d = Motor(Port.D)                                   # attachment D

WHEEL_DIAMETER  = 62.4    # mm   (calibrated)
AXLE_TRACK      = 153     # mm   (calibrated)
TURN_CORRECTION = 1.011   # makes turns land on the exact angle (calibrated)

drive_base = DriveBase(left_motor, right_motor,
                       wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
drive_base.use_gyro(True)   # gyro keeps straights straight and turns accurate

CRUISE_SPEED = 300           # normal driving speed, mm per second
TURN_SPEED   = 150           # normal turning speed, degrees per second
CRUISE_ACCEL = (400, 400)    # (speed up, slow down)

MAX_SPEED = int(left_motor.control.limits()[0] * WHEEL_DIAMETER * 3.1416 / 360)

drive_base.settings(
    straight_speed=CRUISE_SPEED,
    straight_acceleration=CRUISE_ACCEL,
    turn_rate=TURN_SPEED,
    turn_acceleration=(300, 300),
)


# ============================================================
#  COMMANDS  --  these are your coding blocks
# ============================================================
#   CODE you type                  WHAT IT DOES
#   -------------                  -------------------
#   forward(200)                   move forward 20 cm  (distance in mm; 200 = 20 cm)
#   backward(200)                  move backward 20 cm
#   forward(200, 500)              forward FAST  (2nd number = speed in mm/s)
#   forward(200, 120)              forward SLOW  (lower number = slower)
#   forward(200, MAX_SPEED)        forward at FULL speed
#   forward(200, 300, (400, 100))  forward with a gentle stop (3rd part = (speed up, slow down);
#                                                         small slow-down number = smooth stop)
#   left(90)                       turn left 90 degrees
#   right(90)                      turn right 90 degrees
#   curve(200, 90)                CURVE turn -- drive an arc (radius 200 mm, 90 deg)
#                                    small radius = tight curve, big = gentle sweep
#   curve(200, -90)                curve to the left
#   curve(200, -90)                drive the curve in REVERSE (negative angle)
#   C(1)                           run motor C 1 rotation  (use -1 for other way)
#   D(2)                           run motor D 2 rotations
#   pause(1)                       wait 1 second

#   ---- DOING TWO THINGS AT ONCE ----
#   start_C(2)                     start motor C and KEEP GOING (do the next line too) 2=rotations
#   start_D(1)                     start motor D and KEEP GOING
#     e.g.  start_C(2)             <- these two lines run
#           backward(300)             AT THE SAME TIME
# ============================================================

def forward(distance_mm, speed=CRUISE_SPEED, accel=CRUISE_ACCEL):
    drive_base.stop()
    drive_base.settings(straight_speed=min(speed, MAX_SPEED),
                        straight_acceleration=accel)
    drive_base.straight(distance_mm)

def backward(distance_mm, speed=CRUISE_SPEED, accel=CRUISE_ACCEL):
    drive_base.stop()
    drive_base.settings(straight_speed=min(speed, MAX_SPEED),
                        straight_acceleration=accel)
    drive_base.straight(-distance_mm)

def right(degrees):
    wait(120)
    drive_base.turn(degrees * TURN_CORRECTION)

def left(degrees):
    wait(120)
    drive_base.turn(-degrees * TURN_CORRECTION)

def C(rotations, speed_pct=60):
    motor_c.run_angle(speed_pct * 10, rotations * 360)

def D(rotations, speed_pct=60):
    motor_d.run_angle(speed_pct * 10, rotations * 360)

def pause(seconds):
    wait(seconds * 1000)

def curve(radius_mm, degrees, speed=CRUISE_SPEED):
    drive_base.stop()
    drive_base.settings(straight_speed=min(speed, MAX_SPEED))
    drive_base.curve(radius_mm, degrees)

def start_C(rotations, speed_pct=60):
    motor_c.run_angle(speed_pct * 10, rotations * 360, wait=False)   # start C, keep going

def start_D(rotations, speed_pct=60):
    motor_d.run_angle(speed_pct * 10, rotations * 360, wait=False)   # start D, keep going

# ============================================================
#  MISSIONS
# ============================================================

def mission_1():
    forward(500)
    left(90)
    right(90)
    backward(500)
    C(1)
    pause(1)
    D(2)
    start_C(3)
    start_D(3)


def mission_2():
    pass

def mission_3():
    pass

def mission_4():
    pass



    






# ============================================================
#  MENU  --  RIGHT = next mission, LEFT = run the mission shown
# ============================================================

missions = [mission_1, mission_2, mission_3, mission_4]
selected = 0

while True:
    hub.display.number(selected + 1)       # show 1, 2, or 3
    pressed = hub.buttons.pressed()

    if Button.RIGHT in pressed:
        selected = (selected + 1) % len(missions)
        while hub.buttons.pressed():        # wait for release
            wait(10)

    elif Button.LEFT in pressed:
        while hub.buttons.pressed():        # wait for release first
            wait(10)
        missions[selected]()
        drive_base.stop()

    wait(20)





# ============================================================
#  Notes
# ============================================================

#   SPEED = how fast it's going
#   forward(mm, Speed)
#   forward(200)              # cruise (uses the default, 300 mm/second)
#   forward(200, 150)         # slow
#   forward(200, 400)         # 3/4 --quick
#   forward(200, MAX_SPEED)   # full speed (about 540 mm/s)


#   ACCELERAION = how quickly it gets there
#   The default set is (400,400) -- (speed up, slow down)
#   What the 400 actually means: the robot gains 400 mm/s of speed every second. 
#   So with 400, starting from a standstill it takes about ¾ of a second to reach cruise speed.
#   Big number (e.g. 1000) = flooring the gas. Snappy, jerky, might spin the wheels.
#   Small number (e.g. 100) = easing onto the pedal. Smooth, gentle, gliding stops.
#   e.g. (400, 100) = speed up fast, but ease gently to a stop
#   You can adjust the acceleration on the go, without touching the default block
#   forward(600, 300, (1000, 1000))   # jerky -- snaps up and slams to a stop
#   forward(600, 300, (100, 100))   # smooth -- eases up and glides to a stop

#   NOTE: speed has a ceiling (~540). Acceleration does NOT -- it's a
#   different thing (how fast we climb to the speed, not how fast we go).


#   TURNS -- we have two kinds
#   left(90) / right(90)   = PIVOT turn: spin on the spot (exact, needs no room)
#   curve(200, 90)         = CURVE turn: drive an arc (smooth, but needs floor space)
#                           (radius 200 mm, 90 deg)
#   We pivot to line up precisely; we curve to flow around objects quickly.


#   THE GYRO  (drive_base.use_gyro(True))
#   The gyro is a sensor inside the hub that measures which way we are pointing.
#   WHY we use it: it keeps our straights straight and makes our turns land on
#   the exact angle, by correcting the motors if the robot starts to drift.
#   Say to a judge: "Our gyro measures our heading and the code corrects the
#   motors, so we drive straight and turn accurately every run."


#   CALIBRATION -- the numbers at the top (do not change)
#   WHEEL_DIAMETER  = how big our wheels are  -> makes DISTANCE accurate
#   AXLE_TRACK      = distance between wheels  -> makes TURNS accurate
#   TURN_CORRECTION = fine-tune so turns land exactly on the angle
#   WHY: so forward(300) really travels 300 mm and a 90 turn is really 90.
#   We measured these, then tested and adjusted until the robot was accurate.


#   WHY WE MADE OUR OWN COMMANDS (forward, left, C ...)
#   These are commands WE built out of the robot's basic code.
#   WHY: our missions read like simple steps, they're easy to reuse, and if we
#   want to change how the robot drives we fix it in ONE place, not everywhere.


#   THE SETTLE PAUSE (the wait(120) inside left/right)
#   A tiny pause before each turn lets the robot stop wobbling so the gyro
#   reading is stable -- this makes our turns more accurate and repeatable.


#   DOING TWO THINGS AT ONCE
#   Normally each command finishes before the next one starts.
#   start_C / start_D start a motor and KEEP GOING, so the next line runs at
#   the same time (e.g. run an attachment WHILE driving).


#   MOTOR C and D = our attachment motors
#   C(1) / D(2) = number of rotations. Second number is speed as a PERCENT
#   (1-100), so C(1, 50) is half speed, C(1, 100) is full. Use -1 to reverse.


#   THE MENU -- how we pick missions
#   The hub shows a mission number. RIGHT arrow scrolls to the next mission,
#   LEFT arrow runs the one shown. This lets us run any mission at the table
#   without plugging in or re-downloading between rounds.







# ============================================================
#  Juding Session Notes- HOW WE TESTED OUR ROBOT FOR ACCURACY
# ============================================================

#   WHY WE TEST:
#   The robot only does what the numbers tell it. If our settings are a little
#   off, forward(300) won't really go 300 mm and a 90 turn won't really be 90.
#   So we tested and adjusted until the robot was accurate AND repeatable.


#   TESTING DISTANCE  (getting WHEEL_DIAMETER right)
#   1. We told the robot to drive a known distance, e.g. forward(500).
#   2. We measured how far it ACTUALLY went with a tape measure.
#   3. We compared: did it travel exactly 500 mm?
#        - Went too FAR  -> WHEEL_DIAMETER was too small, so we made it bigger.
#        - Went too SHORT -> WHEEL_DIAMETER was too big, so we made it smaller.
#   4. We repeated until the measured distance matched the code. Now distance
#      is accurate, and it stays accurate because wheels don't change size.


#   TESTING TURNS  (checking the gyro + TURN_CORRECTION)
#   We used the gyro to check our own turns:
#        hub.imu.reset_heading(0)      # call the way we're facing "0"
#        right(90)                     # do the turn
#        wait(500)                     # let it settle
#        print(hub.imu.heading())      # read what we ACTUALLY turned
#
#   1. We did FOUR 90 turns in a row -- they should add up to 360 (a full circle).
#   2. We RAN IT SEVERAL TIMES, not just once, to see if the result was the same
#      every time. Doing it once could just be luck.
#   3. What we learned from the numbers:
#        - Same error EVERY time  = a calibration problem -> we fixed it by
#          adjusting TURN_CORRECTION until the turns landed on target.
#        - A little DIFFERENT each time = normal robot "noise" -> we don't chase
#          it; a couple of degrees of wobble is expected on any robot.
#   4. To make turns even better we lowered the turn speed and added a tiny
#      settle pause before each turn, then re-tested to confirm it improved.


#   WHAT "ACCURATE" MEANS TO US (two different things):
#     ACCURATE  = lands on the right number (fixed by calibration)
#     CONSISTENT = does nearly the same thing every run (this is what wins games)
#   Our final turn test landed within about 1 degree, every single run.