#include "pch.h"
#include <stdio.h>

extern "C"
{

	__declspec(dllexport) void hello()
	{
		puts("hello from the dll");
	}

	__declspec(dllexport) int length(char* input)
	{
		return strlen(input);
	}

	__declspec(dllexport) int add(int a, int b) 
	{
		return a + b;
	}

	__declspec(dllexport) void add_p(int* a, int* b, int* result)
	{
		*result = *a + *b;
	}

};