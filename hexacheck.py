import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as lin

def generate_hexa(vertex):
    """
    The function generate_hexa takes in a vertex (an array of 8 points in 3D space) 
    as its input and returns two arrays: centers and normals.
    It first calculates the centers of the six faces of the hexahedron by taking 
    the average of the four vertices that make up each face.
    Next, it calculates the normals of each face using the vector product of two edges of the face.
    The normals are then normalized using the L2 norm.
    The function then plots the vertex points, the centers and the normals using matplotlib. 
    The plot shows the hexahedron with the bottom face colored in one color and the top face 
    colored in another color
    The function returns centers and normals
    This function is used to generate and hexahedron data and display its centers and normals.
            z
            |
       .5------6  y
     .' |    .'|.'
    4---+--7'  |    
    |   |  | --|----->x 
    |  .1--+---2
    |.'    | .'
    0------3'
    
    Bottom face = 0, top face = 5, front face = 1, left = 2, rear = 3, right = 4
    """
    # Create centers
    centers = []
    centers.append((vertex[0]+vertex[1]+vertex[2]+vertex[3])/4)
    centers.append((vertex[0]+vertex[4]+vertex[7]+vertex[3])/4)
    centers.append((vertex[0]+vertex[1]+vertex[4]+vertex[5])/4)
    centers.append((vertex[1]+vertex[2]+vertex[5]+vertex[6])/4)
    centers.append((vertex[2]+vertex[3]+vertex[7]+vertex[6])/4)
    centers.append((vertex[4]+vertex[5]+vertex[6]+vertex[7])/4)
    centers=np.array(centers)

    # Create normals based on vector product
    normals=[]
    normals.append(np.cross(vertex[1]-vertex[0],vertex[3]-vertex[0]))
    normals.append(np.cross(vertex[3]-vertex[0],vertex[4]-vertex[0]))
    normals.append(np.cross(vertex[4]-vertex[0],vertex[1]-vertex[0]))
    normals.append(np.cross(vertex[5]-vertex[1],vertex[2]-vertex[1]))
    normals.append(np.cross(vertex[2]-vertex[3],vertex[7]-vertex[3]))
    normals.append(np.cross(vertex[7]-vertex[4],vertex[5]-vertex[4]))
    normals = np.array(normals)
    
    # Normalize normals
    for i in range(6):
        normals[i]=normals[i]/lin.norm(normals[i])
    
    # Display
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(vertex[:,0], vertex[:,1], vertex[:,2])
    ax.scatter(centers[:,0], centers[:,1], centers[:,2],c='red')
    for i in range(6):
        ax.quiver(centers[i,0], centers[i,1], centers[i,2], normals[i,0], normals[i,1], normals[i,2], color='blue')
    
    # Plot surfaces
    X=vertex[0:4,0]
    Y=vertex[0:4,1]
    Z=vertex[0:4,2]
    surf = ax.plot_trisurf(X, Y, Z,alpha=0.4)
    X=vertex[4:,0]
    Y=vertex[4:,1]
    Z=vertex[4:,2]
    surf = ax.plot_trisurf(X, Y, Z,alpha=0.4)
    ax.set_aspect('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    plt.close() 
    return centers,normals

def point_is_in_hexa(point,centers,normals):
    """
    This function takes in three parameters: point, centers, and normals. 
    
    The point is a single point in 3D space, 
    centers is an array of six points representing the centers of each face of the hexahedron, 
    and normals is an array of six vectors representing the normals of each face of a hexahedron.
    
    The function first calculates the vector from each face center to the point 
    and stores them in the vect list. Then it calculates the dot product of each 
    vector with the corresponding face normal and stores them in the prod list.

    Then, it checks if all dot products are non-positive, and returns 1 if they are 
    and -1 otherwise. This is used to determine whether the point is inside or outside 
    of the hexahedron.
    """
 
    vect=[]
    prod=[]
    for i in range(6):
        vect.append(point-centers[i])
    vect= np.array(vect)
    for i in range(6):
        prod.append(np.dot(vect[i],normals[i]))
    prod=np.array(prod)
    if all(prod <= 0):
        is_in_hexa = 1
    else:
       is_in_hexa = -1
    return is_in_hexa

def generate_random_points():
    """Generate a points list to check the result"""
    
    x = np.random.uniform(-1, 1, 200)
    y = np.random.uniform(-1, 1, 200)
    z = np.random.uniform(-1, 1, 200)
    points = np.column_stack((x, y, z))
    return points
 
def check_and_plot_points_in_hexa(point_list, centers, normals,vertex):
    """Display the result"""
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    blue_point=[]
    red_point=[]

    for point in point_list:
        is_in_hexa=point_is_in_hexa(point,centers,normals)
        if (is_in_hexa == 1):
            blue_point.append(point)
        else:
            red_point.append(point)

    blue_point=np.array(blue_point)
    red_point=np.array(red_point)
    if(len(blue_point)>0):
        ax.scatter(blue_point[:,0], blue_point[:,1], blue_point[:,2], c='blue')
    if(len(red_point)>0):
        ax.scatter(red_point[:,0], red_point[:,1], red_point[:,2], c='red')
    # Plot surface
    X=vertex[0:4,0]
    Y=vertex[0:4,1]
    Z=vertex[0:4,2]
    surf = ax.plot_trisurf(X, Y, Z,alpha=0.4)
    X=vertex[4:,0]
    Y=vertex[4:,1]
    Z=vertex[4:,2]
    surf = ax.plot_trisurf(X, Y, Z,alpha=0.4)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    plt.show()
# Main
# hexa
vertex = np.array([[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[-0.5,-0.5,0.1],[-0.5,0.5,0.75],[0.5,0.5,0.75],[0.5,-0.5,0.1]])
centers,normals=generate_hexa(vertex)
point_list=generate_random_points()
check_and_plot_points_in_hexa(point_list, centers, normals,vertex)



