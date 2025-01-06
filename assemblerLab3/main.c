#include <math.h>

double check(bool condition);

double access2(double xmm0, int edx, float xmm2, double xmm3) 
{
    double xmm6, xmm7;
    // double xmm8 = xmm3;
    // xmm6 = xmm2;
    // xmm8 = xmm3;

    // double xmm1 = double(edx);
    xmm7 = pow(xmm0, double(edx));
    xmm6 = sin(xmm2);
    xmm6 = log10(xmm3) + xmm6;

    return check(xmm6 > xmm7);

}