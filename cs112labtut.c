#include <stdio.h>

int main () {
	char ch = '0';
	printf("\n Enter a character on your keyboard: (any non-alphabetic character to end)");
	ch = getchar();
	getchar();

	while(ch >= 'a' && ch<= 'z')
	{
		switch(ch)
		{
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				printf("\n This character is a vowel");
				if(ch == 'i')
				{
					printf("\n This is the third vowel of the alphabet");
				}
				break;
			default:
				printf("\n This character is not a vowel");
				break;	
		}
		printf("\n Enter a character on your keyboard: (any non-alphabetic character to end)");
		ch = getchar();
		getchar();
	}
	
	return 0;
}	
