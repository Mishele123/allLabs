#include <stdio.h>


int array[100];

// 6 7 4 0 1 7 4 1

int main()
{
	// сортировка вставками ОБЫЧНАЯ
	unsigned n;

	scanf("%u", &n);

	for (unsigned i = 0; i < n; i++)
	{
		scanf("%d", &array[i]);
	}
	// 3 2 1
	for (unsigned i = 1; i < n; i++)
	{
		for (unsigned j = i; j > 0; j--)
		{
			if (array[j] < array[j - 1])
			{	
				int temp = array[j - 1];
				array[j - 1] = array[j];
				array[j] = temp;
			}
		}
	}

	for (auto& i : array)
	{
		printf("%d ", i);
	}

	return 0;
}
