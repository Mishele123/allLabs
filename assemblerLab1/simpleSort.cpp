
#include <stdio.h>


int array[100];

int main()
{
	unsigned n; // r8d
	scanf("%u", &n);
	unsigned i = 0; // ecx
	goto cycle1Start;

cycle1Start:
	if (i == n)
		goto cycle1End;
	scanf("%d", &array[i]);
	i += 1;
	goto cycle1Start;

cycle1End:
	i = 1;
	goto cycle2Start;

cycle2Start:
	if (i == n) goto cycle2End;
	unsigned j = i; // r9d
	int temp = 0; // r10d
	goto cycle3Start;

cycle2End:
	goto printfqwe;

cycle3Start:
	if (j == 0) goto cycle3End;
	if (array[j] < array[j - 1])
	{
		temp = array[j - 1];
		array[j - 1] = array[j];
		array[j] = temp;
	}
	goto skipSwap;

skipSwap:
	j -= 1;
	goto cycle3Start;

cycle3End:
	i += 1;
	goto cycle2Start;

printfqwe:
	for (auto& i : array)
		printf("%d ", i);
}