import heapq
import math
import matplotlib.pyplot as plt
from Finalmap import *

def ActionSet(d, theta):
    all_moves = [[d*math.cos(math.radians(theta + 0)), d*math.sin(math.radians(theta + 0)), theta + 0],          # parallel to x / 0
                 [d*math.cos(math.radians(theta + 30)),  d*math.sin(math.radians(theta + 30)), theta + 30],         # positive 30
                 [d*math.cos(math.radians(theta + 60)),  d*math.sin(math.radians(theta + 60)), theta + 60],         # positive 60
                 [d*math.cos(math.radians(theta - 30)), d*math.sin(math.radians(theta -30)), theta - 30],        # negative 30
                 [d*math.cos(math.radians(theta - 60)), d*math.sin(math.radians(theta -60)), theta - 60]]        # negative 60
    return all_moves

def backtracking(closed_list):
    backtrack = []
    length = len(closed_list)
    current_position = closed_list[length - 1][1]
    backtrack.append(current_position)
    parent = closed_list[length - 1][2]
    while parent is not None:
        for i in range(length):
            X = closed_list[i]
            if X[1] == parent:
                parent = X[2]
                current_position = X[1]
                backtrack.append(current_position)
    return backtrack[::-1]

def Astar(start_position, goal_position,step,clearance, threshold):
    
    # each node has three attributes 1) Parent 2) co-ordinates 3) Cost to Come
    d_initial = math.sqrt((goal_position[0] - start_position[0]) ** 2 + (goal_position[1] - start_position[1]) ** 2)
    start_node = (d_initial, start_position, None)
    goal_node = (0, goal_position, None)
    plot_x = []
    plot_y = []
    new_min=[]
    open_list = []

    new_min.append(start_node)
    closed_list = []
    open_list.append(start_node)
    Z = np.zeros((int(400/threshold),int(250/threshold),10))

    theta=30

    while len(open_list) > 0:
        new_min = heapq.nsmallest(5, open_list)
        for element in new_min:
            current_node = element
            theta = current_node[1][2]
            closed_list.append( current_node)

            plot_x.append(current_node[1][0])
            plot_y.append(current_node[1][1])

            res=(((current_node[1][0] - goal_position[0]) ** 2) + ((current_node[1][1]-goal_position[1]) ** 2) )
            if res<=(step*1.5)**2:
                print('Reached Goal Node Succesfully')
                final_path = backtracking(closed_list)
                return final_path
            for j in range(5):
                newnode_position = ActionSet(step, theta)
                # Get node position
                node_position = (round(current_node[1][0] + newnode_position[j][0]),
                                 round(current_node[1][1] + newnode_position[j][1]), newnode_position[j][2])
                node_parent = current_node[1]
                cost_to_come = math.sqrt((goal_position[0] - node_position[0]) ** 2 + (goal_position[1] - node_position[1]) ** 2)
                cost_to_go =  math.sqrt((node_position[0]-node_parent[0]) ** 2 + (node_position[1] - node_parent[1]) ** 2)
                nodeposition_cost = current_node[0] + cost_to_go
                Aux = round(cost_to_go + cost_to_come)
                node_position1=isobstacle(clearance,node_position[0],node_position[1],1)
                if node_position1 == False:
                    if  Z[int(node_position[0]/threshold)][int(node_position[1]/threshold)][int(node_position[2]/30)]==0:
                        Z[int(node_position[0]/threshold)][int(node_position[1]/threshold)][int(node_position[2]/30)]=1
                        new_node = (Aux, node_position, node_parent)
                        heapq.heappush(open_list, new_node)
                    else:
                        continue
                    plt.quiver(new_node[2][0], new_node[2][1], newnode_position[j][0], newnode_position[j][1], units='xy' ,scale=1,color= 'k',headwidth = 1,headlength=0,width=0.2)
                    plt.pause(0.00001)

        heapq.heappop(open_list)