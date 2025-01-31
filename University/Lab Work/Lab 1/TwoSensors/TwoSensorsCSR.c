#include <stdio.h>
#include <math.h>

// Forward TC function
float NISTdegCtoMilliVoltsKtype(float tempDegC);  // returns EMF in millivolts

// Inverse TC function
float NISTmilliVoltsToDegCKtype(float tcEMFmV);  // returns temp in degC assuming 0 degC cold jcn

// ADC to Voltage Function
float V_adc(float n, float VRef); // Returns Voltage in Volts

// Celcius to Kelvin Function
float Kelvin_to_C(float K); // Returns Temp in Kelvin

int main()
{
    // Define VRef
    const float VRef = 5.0;
    // initialise port voltage variables
    float V_a0, V_a1;
    // Define Thermistor constants
    int a0, a1;
    // User input for pins A0 and A1
    printf("a0: ");
    scanf("%d", &a0);
    printf("\na1: ");
    scanf("%d", &a1);

    

    // Calculate thermistor temperature in degrees C ( Part b, i,ii,iii & v)
    V_a1 = V_adc((float) a1, VRef); // Convert the ADC value to voltage
    float R_a1 = ((10*3.3)/V_a1)-10; //Convert this voltage to resistance

    const float T0 = 298.15; // Define Eq. Constants
    const float R0 = 10.0, B = 3975.0;

    float TK_a1 = 1/((1/T0)+(1/B)*(log(R_a1/R0))); // Convert the resistance to temperature in K

    float TC_a1 = Kelvin_to_C(TK_a1); // Convert the temperature in K to C

    // Calculate thermocouple temperature in degrees C ( Part c, i - iv)
     V_a0 = V_adc((float) a0, VRef);    // Convert the ADC value to voltage
     float E_TC = (V_a0 - 0.35)/54.4; // Calculate the thermocouple voltage
     float E_comp = NISTdegCtoMilliVoltsKtype(TC_a1); //  Convert the thermistor temperature into a compensation EMF
     float T_TC = NISTmilliVoltsToDegCKtype(E_TC * 1000 + E_comp); // Calculate the temperature (Converting E_TC into mV)

    // Output results
    printf("Thermistor temperature (deg C): %f \n", TC_a1);
    printf("Thermocouple temperature with CJC (deg C): %f \n", T_TC);

    return 0;
}

/* Write a function here to convert ADC value to voltages. (Part a, equation 1)
Call it from the main() function above */
float V_adc(float n, float VRef)
{
    float Vadc;
    Vadc = ((float)n*(float)VRef)/1024;
    return Vadc;
}
/* Write a function to convert degrees K to degrees C  (Part b, (iv))
Call it from the main() function above */
float Kelvin_to_C(float K)
{
    float C;
    C = K - 273.15;
    return C;
}

/* returns EMF in millivolts */
float NISTdegCtoMilliVoltsKtype(float tempDegC)
{
    int i;
    float milliVolts = 0;
    if(tempDegC >= -170 && tempDegC < 0)
    {
        const float coeffs[11] =
        {
            0.000000000000E+00,
            0.394501280250E-01,
            0.236223735980E-04,
            -0.328589067840E-06,
            -0.499048287770E-08,
            -0.675090591730E-10,
            -0.574103274280E-12,
            -0.310888728940E-14,
            -0.104516093650E-16,
            -0.198892668780E-19,
            -0.163226974860E-22
        };
        for (i=0; i<=10; i++)
        {
            milliVolts += coeffs[i] * pow(tempDegC,i);
        }
    }
    else if(tempDegC >= 0 && tempDegC <= 1372)
    {
        const float coeffs[10] =
        {
            -0.176004136860E-01,
            0.389212049750E-01,
            0.185587700320E-04,
            -0.994575928740E-07,
            0.318409457190E-09,
            -0.560728448890E-12,
            0.560750590590E-15,
            -0.320207200030E-18,
            0.971511471520E-22,
            -0.121047212750E-25
        };
        const float a0 =  0.118597600000E+00;
        const float a1 = -0.118343200000E-03;
        const float a2 =  0.126968600000E+03;

        for (i=0; i<=9; i++)
        {
            milliVolts += coeffs[i] * pow(tempDegC,i);
        }

        milliVolts += a0*exp(a1*(tempDegC - a2)*(tempDegC - a2));
    }
    else
    {
        milliVolts = 99E99;
    }
    return milliVolts;
}

// returns temperature in deg C.
float NISTmilliVoltsToDegCKtype(float tcEMFmV)
{

        int i, j;
        float tempDegC = 0;
        const float coeffs[11][3] =
        {
          {0.0000000E+00,  0.000000E+00, -1.318058E+02},
         {2.5173462E+01,  2.508355E+01,  4.830222E+01},
         {-1.1662878E+00,  7.860106E-02, -1.646031E+00},
         {-1.0833638E+00, -2.503131E-01,  5.464731E-02},
         {-8.9773540E-01,  8.315270E-02, -9.650715E-04},
         {-3.7342377E-01, -1.228034E-02,  8.802193E-06},
         {-8.6632643E-02,  9.804036E-04, -3.110810E-08},
         {-1.0450598E-02, -4.413030E-05,  0.000000E+00},
         {-5.1920577E-04,  1.057734E-06,  0.000000E+00},
         {0.0000000E+00, -1.052755E-08,  0.000000E+00}
       };
       if(tcEMFmV >=-5.891 && tcEMFmV <=0 )
       {
           j=0;
       }
       else if (tcEMFmV > 0 && tcEMFmV <=20.644  )
       {
           j=1;
       }
       else if (tcEMFmV > 20.644 && tcEMFmV <=54.886  )
       {
           j=2;
       }
       else
       {
           return 99E9;
       }

       for (i=0; i<=9; i++)
        {
            tempDegC += coeffs[i][j] * pow(tcEMFmV,i);
        }
    return tempDegC;
}