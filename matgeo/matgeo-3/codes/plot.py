import matplotlib.pyplot as plt
import math

# Read coordinates from the text file
with open("output.txt", "r") as file:
    lines = file.readlines()

# Extracting coordinates from the text file
A_coords = list(map(float, lines[0].split()[1:]))
B_coords = list(map(float, lines[1].split()[1:]))
C_coords = list(map(float, lines[2].split()[1:]))

# Define points A, B, and C
A = (A_coords[0], A_coords[1])
B = (B_coords[0], B_coords[1])
C = (C_coords[0], C_coords[1])

# Function to calculate the distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances AB and AC
AB = calculate_distance(A, B)
AC = calculate_distance(A, C)

# Plotting points A, B, and C
plt.plot(*A, 'ro')  # A is red
plt.plot(*B, 'bo')  # B is blue
plt.plot(*C, 'go')  # C is green

# Labeling points directly on the graph
plt.text(A[0], A[1], f"A{A}", fontsize=12, ha='right', va='bottom')
plt.text(B[0], B[1], f"B{B}", fontsize=12, ha='right', va='bottom')
plt.text(C[0], C[1], f"C{C}", fontsize=12, ha='right', va='bottom')

# Plotting lines AB and AC
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')  # Line AB in blue
plt.plot([A[0], C[0]], [A[1], C[1]], 'g-')  # Line AC in green

# Plot circles with radius AB at B and radius AC at C
circle_B = plt.Circle(B, AB, color='b', fill=False, linestyle='--', label=f"Circle at B with radius AB = {AB:.2f}")
circle_C = plt.Circle(C, AC, color='g', fill=False, linestyle='--', label=f"Circle at C with radius AC = {AC:.2f}")

# Adding circles to the plot
plt.gca().add_patch(circle_B)
plt.gca().add_patch(circle_C)

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot of points A, B, C, lines AB, AC, and circles with radius AB and AC")

# Equal scaling and showing the grid
plt.axis('equal')
plt.grid(True)

# Show plot
plt.show()

