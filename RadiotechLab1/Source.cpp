#define _USE_MATH_DEFINES
#include <windows.h>
#include <stdio.h>
#include <math.h>
#include "fftw3.h"


#define FS 1.0E+6 // частота дискретезации
#define FFT_POINTS 1000 // Число точек // для 1000 точек период = 1/100 гц
#define FFT_POINTS2 ((double)FFT_POINTS * (double)FFT_POINTS)


const double F = 10.0E+3; // частота гармонич сигнала
const double F1 = 30.0E+3;
const double F2 = 31.0E+3;

const double Mag = 1.0; // амплитуда
const double DT = 1.0 / FS;
const double DF = FS / FFT_POINTS;
OPENFILENAMEA ofn;
HANDLE hFile;
fftw_complex* In, * Out; // Arrays for FFT
fftw_plan pDir;

double Noise() 
{
	double T = 0.0;
	for (int j = 0; j < 12; j++) T += ((double)rand() / RAND_MAX);
	return (T - 6);
}

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
	LPSTR lpCmdLine, int nCmdShow)
{
	char Txt[512];
	sprintf(Txt, "samples.txt");
	memset(&ofn, 0, sizeof(OPENFILENAME));
	ofn.lStructSize = sizeof(OPENFILENAME);
	ofn.hwndOwner = NULL;
	ofn.lpstrFilter = "Data Files(*.dat)\0*.dat;\0Any Files(*.*)\0\*.*\0";
	ofn.lpstrFile = Txt;
	ofn.nFilterIndex = 1;
	ofn.nMaxFile = sizeof(Txt);
	ofn.lpstrTitle = "Открыть файл";
	ofn.Flags = OFN_EXPLORER | OFN_OVERWRITEPROMPT;
	if (!GetSaveFileNameA(&ofn)) return FALSE;
	hFile = CreateFileA(ofn.lpstrFile, GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hFile == INVALID_HANDLE_VALUE)
	{
		MessageBoxW(NULL, L"File is not created", L"FFT testing", MB_OK);
		return FALSE;
	}

	In = (fftw_complex*)VirtualAlloc(NULL, FFT_POINTS * sizeof(fftw_complex), MEM_COMMIT, PAGE_READWRITE);
	Out = (fftw_complex*)VirtualAlloc(NULL, FFT_POINTS * sizeof(fftw_complex), MEM_COMMIT, PAGE_READWRITE);

	if ((In == NULL) || (Out == NULL))
	{
		MessageBox(NULL, L"Not enough memory", L"FFT testing", MB_OK);
		return FALSE;
	}

	pDir = fftw_plan_dft_1d(FFT_POINTS, In, Out, FFTW_FORWARD, FFTW_ESTIMATE);

	if (pDir == NULL)
	{
		MessageBoxW(NULL, L"FFTW plan was not created", L"FFT testing", MB_OK);
		return FALSE;
	}

	ZeroMemory(In, FFT_POINTS * sizeof(fftw_complex));
	
	int a = 5;

	for (int i = 0; i < FFT_POINTS; i++)
	{
		In[i][0] = Noise() + Mag * cos(2 * M_PI * F * DT * i);
	}

	/*for (int i = 0; i < FFT_POINTS; i++)
	{
		In[i][0] = Mag * cos(2 * M_PI * F * DT * i);
	}*/
	int NP = (int)(1 / F / DT);
	for (int i = 0; i < FFT_POINTS; i++)
		if (i % NP < NP / 2) In[i][0] = Mag; else In[i][0] = -Mag;

	fftw_execute(pDir);
	char buffer[256];
	DWORD ByteNum;
	double P; // частота сигнала sovetkinam@mail.ru

	for (int i = 0; i < FFT_POINTS; i++)
	{
		P = (Out[i][0] * Out[i][0] + Out[i][1] * Out[i][1]) / FFT_POINTS2;
		sprintf(buffer, "%.8g\t%.8g\t%.8g\r\n", i * DF, P, 10 * log10(P));
		WriteFile(hFile, buffer, strlen(buffer), &ByteNum, NULL);
	}

	MessageBoxA(NULL, "Game over", "FFT testing", MB_OK);
	CloseHandle(hFile);
	VirtualFree(In, 0, MEM_RELEASE);
	VirtualFree(Out, 0, MEM_RELEASE);
	fftw_destroy_plan(pDir);
	return 0;
}