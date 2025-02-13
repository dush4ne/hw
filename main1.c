#include <stdio.h>

int main() {
	
	char c = 'a';

	switch(c)
	{
		case 'a':
			printf("\n This is the first character in the alphabet");
			break;
		case 'b':
			printf("\n This is the second character in the alphabet");
			break;
		case 'z':
			printf("\n This is the last character in the alphabet");
			break;
		default:
			printf("\n This input is not supported");
			break;
	}

	return 0;

}
