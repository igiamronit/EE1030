import matplotlib.pyplot as plt

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

# Plotting points
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

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot of points A, B, C and lines AB, AC")

# Show plot with grid
plt.grid(True)
plt.show()

