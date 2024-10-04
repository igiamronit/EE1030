#include <stdio.h>

int main() {
    // Points A(0, 2), B(3, p), C(p, 5)
    double A_x = 0, A_y = 2;
    double B_x = 3, B_y, C_x, C_y = 5;
    //9+(2-p)^2 = p^2 + 9
    // p = 1
    double p = 1;
    
    // Coordinates for B(3, p) and C(p, 5)
    B_y = p;
    C_x = p;

    // Output coordinates of A, B, and C to a text file
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the coordinates in a format that can be easily read by Python
    fprintf(file, "A: %lf %lf\n", A_x, A_y);
    fprintf(file, "B: %lf %lf\n", B_x, B_y);
    fprintf(file, "C: %lf %lf\n", C_x, C_y);
    fclose(file);

    printf("Coordinates of A, B, and C have been written to output.txt\n");
    return 0;
}

