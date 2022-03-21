import numpy as np
import matplotlib.pyplot as plt

def isobstacle(clearance, x, y, threshold):
    if (0 <= x <= (400 / threshold)) and (0 <= y <= (250 / threshold)):
    #polygon Obstracle
        l1 = y - ((0.316) *x) - 173.608 + clearance 
        l2 = y - 0.857*x - 111.42 +clearance
        l3 = y + (0.1136*x) - 189.09 +clearance
        l4 = y + (3.2 * x) - 436 +clearance
        l5 = y + (1.23 * x) - 229.34 + clearance
        l6 =  y + (0.1136*x) - 189.09 +clearance
    # Hexagon Obstracle
        #h1 = y - 0.577*x - 24.97 +clearance
        #h2 = y + 0.577*x - 255.82 +clearance
        #h3 = x - 235 +clearance
        #h6 = x - 165 +clearance
        #h5 = y + 0.577*x - 175 +clearance
        #h4 = y - 0.577*x + 55.82+clearance
    #circle obstracle
        #if ((x - round(300/threshold)) ** 2 + (y - round(185/threshold)) ** 2 - ((40/threshold) + clearance) ** 2) <= 0:
            #return True

        if (l1<0 and l2>0 and l3>0):
            return True
        elif (l4<0 and l5>0 and l6<0):
            return True
        #elif (h1<0 and h2<0 and h3<0 and h4>0 and h5>0 and h6>0):
            #return True
        else:
            return False

def finalmap(clearance):
    #Background
    # Geometrical definition of the obstacle space
    obstaclespace = np.zeros(shape=(int(251), int(401))) 
    # Defining the boundary
    boundary_x = []
    boundary_y = []

    for i in range(401):
        boundary_x.append(i)
        boundary_y.append(0)
        obstaclespace[0][i] = -1

        boundary_x.append(i)
        boundary_y.append(250)
        obstaclespace[200][i] = -1

    for i in range(251):
        boundary_x.append(0)
        boundary_y.append(i)
        obstaclespace[i][0] = -1

        boundary_x.append(400)
        boundary_y.append(i)
        obstaclespace[i][400] = -1

    # Object 1 = Circle
    circle = []
    for x in range(401):
        for y in range(251):
            figure1 = (x - 300) ** 2 + (y - 185) ** 2 - (40) ** 2
            if figure1 <= 0:
                circle.append((x, y))

    circle_x = [x[0] for x in circle]
    circle_y = [x[1] for x in circle]
    plt.scatter(circle_x, circle_y, color='b')
    for i in circle:
        obstaclespace[i[1]][i[0]] = -1

    # Object 2= polygon 1st half
    sideA = []
    sideB = []
    sideC = []
    
    for x in range(401):
        for y in range(251):
            A =  y - ((0.316) *x) - 173.608
            if A <= 0:
                sideA.append((x, y))
            C = y + (0.1136*x) - 189.09 
            if C >= 0:
                sideC.append((x, y))
            B = y - 0.857*x - 111.42
            if B >= 0:
                sideB.append((x, y))
           
    polygon1side = list(set(sideA) & set(sideB) & set(sideC))
    for i in polygon1side:
        obstaclespace[i[1]][i[0]] = -1
    x_polygon = [x[0] for x in polygon1side]
    y_polygon = [x[1] for x in polygon1side]
    plt.scatter(x_polygon, y_polygon, color='b')

# Object 3= polygon 2st half
    sideD = []
    sideE = []
    sideL = []
    
    for x in range(401):
        for y in range(251):
            E =  y + (3.2 * x) - 436 +clearance
            if E <= 0:
                sideE.append((x, y))
            D = y + (0.1136*x) - 189.09 
            if D <= 0:
                sideD.append((x, y))
            L = y + (1.23 * x) - 229.34 + clearance
            if L >= 0:
                sideL.append((x, y))
           
    polygon2side = list(set(sideD) & set(sideE) & set(sideL))
    for i in polygon2side:
        obstaclespace[i[1]][i[0]] = -1
    x_polygon2 = [x[0] for x in polygon2side]
    y_polygon2 = [x[1] for x in polygon2side]
    plt.scatter(x_polygon2, y_polygon2, color='b')

    #Object 3 = Hexagon
    sideF = []
    sideG = []
    sideH = []
    sideI = []
    sideJ = []
    sideK = []
    for x in range(401):
        for y in range(251):
            F = y - 0.577*x - 24.97
            if F < 0:
                sideF.append((x, y))
            G = y + 0.577*x - 255.82
            if G < 0:
                sideG.append((x, y))
            H = x - 235 
            if H < 0:
                sideH.append((x, y))
            I = y - 0.577*x + 55.82
            if I > 0:
                sideI.append((x, y))
            J = y + 0.577*x - 175
            if J > 0:
                sideJ.append((x, y))
            K = x - 165
            if K > 0:
                sideK.append((x, y))
    hexagon = list(set(sideF) & set(sideG) & set(sideH) & set(sideI) & set(sideJ) & set(sideK))
    for i in hexagon:
        obstaclespace[i[1]][i[0]] = -1
    x_hexagon = [x[0] for x in hexagon]
    y_hexagon = [x[1] for x in hexagon]
    plt.scatter(x_hexagon, y_hexagon, color='b')
    
    obstacle_t = obstaclespace.T
    obs = []
    for i in range(300):
        obs.append(obstacle_t[i])
    
    plt.scatter(boundary_x, boundary_y, color='g')
    plt.savefig("Map.png")
    return obs, boundary_x, boundary_y
    