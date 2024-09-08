import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_points(output):
    with open(output, 'r') as file:
        lines = file.readlines()

    # Reading the coordinates of the points from the file
    # Format in the file: A(x1, y1, z1), B(x2, y2, z2), R(xR, yR, zR)
    
    line1 = lines[0].strip().strip('A()')
    A_x, A_y, A_z = map(float, line1.split(','))

    line2 = lines[1].strip().strip('B()')
    B_x, B_y, B_z = map(float, line2.split(','))

    line3 = lines[2].strip().strip('R()')
    R_x, R_y, R_z = map(float, line3.split(','))

    return [[A_x, A_y, A_z], [B_x, B_y, B_z], [R_x, R_y, R_z]]

def plot_coordinates(coordinates):
    # Unpack coordinates
    A_x, A_y, A_z = coordinates[0][0], coordinates[0][1], coordinates[0][2]
    B_x, B_y, B_z = coordinates[1][0], coordinates[1][1], coordinates[1][2]
    R_x, R_y, R_z = coordinates[2][0], coordinates[2][1], coordinates[2][2]

    # Create a new figure for 3D plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the line AB
    ax.plot([A_x, B_x], [A_y, B_y], [A_z, B_z], 'b-', label='Line $AB$')

    # Plot the points A, B, and R
    ax.scatter(A_x, A_y, A_z, color='green', label='Point A', s=50)
    ax.text(A_x, A_y, A_z, f'A({A_x:.2f}, {A_y:.2f}, {A_z:.2f})', color='green')

    ax.scatter(B_x, B_y, B_z, color='blue', label='Point B', s=50)
    ax.text(B_x, B_y, B_z, f'B({B_x:.2f}, {B_y:.2f}, {B_z:.2f})', color='blue')

    ax.scatter(R_x, R_y, R_z, color='red', label='Point R', s=50)
    ax.text(R_x, R_y, R_z, f'R({R_x:.2f}, {R_y:.2f}, {R_z:.2f})', color='red')

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Plot of Line $AB$ with Point $R$')

    # Show the legend and grid
    ax.legend()
    ax.grid(True)

    # Show plot
    plt.show()

if __name__ == "__main__":
    # Fetching coordinates from the file
    coordinates = read_points("output.txt")
    
    # Final plot
    plot_coordinates(coordinates)

