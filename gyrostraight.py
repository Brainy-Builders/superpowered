from common import * # includes gyro
from gyroturno import gyroturno

def gyro_straight(distance, speed, reset_angle=None, GCV=2.5):
  # If no "reset_angle" is given, continue in the same direction
  # heading is the direction the robot will go
  backwards = speed <= 0
  if(reset_angle is None):
    heading = gyro.angle()
  else:
    heading = -reset_angle # negative due to inverted gyro sensor

  if backwards:
    end_distance = robot.distance()-distance
  else:
    end_distance = robot.distance()+distance
  
  if backwards:
    while robot.distance() > end_distance:
      correction = (heading-gyro.angle()) * GCV
      robot.drive(speed, -correction)
  else:
    while robot.distance() < end_distance:
      correction = - (heading-gyro.angle()) * GCV
      robot.drive(speed, correction)
      #print("robot distnace is", robot.distance())
  return robot.distance()  

def test1():
    gyro_straight(distance=400, speed=-300, reset_angle=0, GCV=2.5)
    ev3.speaker.beep()
    time.sleep(2)
    