#include <stdio.h>

int main() 
{
int coins = 0;
	printf("\n Enter the amount of coins: ");
	scanf("%d", &coins);

	if (coins >= 100)
	{
		printf("\nYou are a rich person!");
	}
	else if(coins >= 50)
	{
		printf("\n You are doing OK");
	}
	else if(coins >= 10)
	{
		printf("\n You need to do better");
	}
	else if(coins >= 5)
	{
		printf("\n You need to work harder");
	}
	else if(coins >= 0)
	{
		printf("\n You really suck");
	}
	else
	{// This should not happen
		printf("\nYou did something wrong");
	}
	return 0;
}
