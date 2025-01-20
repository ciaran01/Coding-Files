#include <stdio.h>
#include <math.h>

float V_adc(n, VRef);

int main()
{
    // Define VRef
    const float VRef = 5.0;
    float V_a0, V_a1;
    // Define Thermistor constants
    int a0, a1;
    // User input for pins A0 and A1
    printf("a0: ");
    scanf("%d", &a0);
    printf("\na1: ");
    scanf("%d", &a1);

    V_a0 = V_adc((float) a0, VRef);    
    V_a1 = V_adc((float) a1, VRef);

    printf("\nV_a0 = %.2f\nV_a1 = %.2f\n", V_a0, V_a1);
}


float V_adc(float n, float VRef)
{
    float Vadc;
    Vadc = ((float)n*(float)VRef)/1024;
    return Vadc;
}