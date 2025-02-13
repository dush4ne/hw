#include <stdio.h>

int main() {

	char ch = 'a';
	scanf("%c", &ch);
	
	switch(ch)
	{
		case 'a':
			printf("\n This character is a vowel");
			break;
		case 'e':
			printf("\n This character is a vowel");
			break;
		case 'i':
			printf("\n You have entered the third vowel!");
			break;
		case 'o':
			printf("\n This character is a vowel");
			break;
		case 'u':
			printf("\n This character is a vowel");
			break;
		default:
			printf("\n This character is not a vowel");
			break;
	return 0;
	}

