import time
from Functions import *
from Finalmap import *

userdefined = False
if userdefined:
    start_x = int(input("Start point X: "))
    start_y = int(input("Start point Y: "))
    goal_x = int(input("Goal point X: "))
    goal_y = int(input("Goal point Y: "))
    clearance = int(input("Clearance of the robot"))
    step = int(input("value of the step"))
    threshold =int(input("threshold value"))
    radius =int(input("radius of robot"))
    start_angle = int(input("Angle of start"))
    goal_angle =int(input("Angle of goal"))

else:
    start_x = 50
    start_y = 50
    goal_x = 200
    goal_y = 200
    clearance = 5
    d = 1
    threshold = 1.5
    radius = 10
    start_angle = 30
    goal_angle = 30
d= 10
start_position = (start_x, start_y, start_angle)
goal_position = (goal_x, goal_y, goal_angle)
plt.plot(start_x, start_y, "Dr")
plt.plot(goal_x, goal_y, "Dr")

start_time = time.time()

if __name__ == '__main__':
    final_obstracle, boundary_x, boundary_y = finalmap(clearance)
    if isobstacle(clearance, start_x, start_y, threshold):
        print("Start Position stated is in obstacle space")
    elif isobstacle(clearance, goal_x, goal_y, threshold):
        print("Goal Position stated is in obstacle space")
    else:
        path = Astar(start_position, goal_position, d, clearance,threshold)
        print(path)
        if path is not None:
            scatter_x = [x[0] for x in path]
            scatter_y = [x[1] for x in path]
            plt.plot(scatter_x, scatter_y, color='r', linewidth=4)
            plt.savefig('Path_rigid.png')
            plt.show()
            elapsed_time = time.time() - start_time
            print("Time Required to Solve Probelm: ", round(elapsed_time, 2), "snds")
        else:
            print("No path found")