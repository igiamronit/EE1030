#include <stdio.h>

int main() {
    // Coordinates of A and B in 3D
    int x1 = -2, y1 = 3, z1 = 5;  // Coordinates of A (x1, y1, z1)
    int x2 = 1, y2 = -4, z2 = 6;  // Coordinates of B (x2, y2, z2)

    // The ratio AR : RB = 2 : 3
    int m = 2, n = 3;

    // Coordinates of point R using the section formula in 3D
    // R(x, y, z) = [(m*x2 + n*x1) / (m+n), (m*y2 + n*y1) / (m+n), (m*z2 + n*z1) / (m+n)]
    float xR = (float)(m*x2 + n*x1) / (m+n);
    float yR = (float)(m*y2 + n*y1) / (m+n);
    float zR = (float)(m*z2 + n*z1) / (m+n);

    // Printing the coordinates of points A, B, and R
    printf("A(%d, %d, %d)\n", x1, y1, z1);
    printf("B(%d, %d, %d)\n", x2, y2, z2);
    printf("R(%.2f, %.2f, %.2f)\n", xR, yR, zR);

    // Writing the coordinates to a file named "output.txt"
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // Write points A, B, and R to the file
    fprintf(file, "A(%d, %d, %d)\n", x1, y1, z1);
    fprintf(file, "B(%d, %d, %d)\n", x2, y2, z2);
    fprintf(file, "R(%.2f, %.2f, %.2f)\n", xR, yR, zR);

    // Close the file
    fclose(file);
    printf("Coordinates have been saved to output.txt\n");

    return 0;
}

