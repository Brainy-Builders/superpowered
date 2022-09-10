from common import *
import linefollow
def main():
        linefollow.line_follow(length=350,speed=150,sensor="left",side="right",find_cross=True)
        robot.turn(90)
        linefollow.line_follow(length=450,speed=150,sensor="right",side="left")
        linefollow.line_follow(200, 200, "right", "left")
        robot.stop()
        robot.turn(90)
        