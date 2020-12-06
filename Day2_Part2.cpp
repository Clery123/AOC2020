#include<iostream>
#include<fstream>
#include <stdlib.h>
#include<sstream>
#include<string>
#include <Windows.h>
#include<vector>
#include<stdio.h>
int getCount() {
	std::string value;
	std::string password = "";
	char character;
	int number1;
	int number2;
	int count = 0;
	std::ifstream MyreadFile("data.txt");
	while (std::getline(MyreadFile, value)) {
		
		std::string temp = value;
		if (value[1] == '-') {
			temp = temp[0];
		}
		else {
			std::string temp2(1, temp[0]);
			std::string temp3(1, temp[1]);
			temp = temp2 + temp3;
		}
		std::stringstream n(temp);
		n >> number1;
		temp = value;
		int findDash = temp.find("-") + 1;
		
		if (temp[findDash + 1] == ' ') {
			temp = temp[findDash];
		}
		else{
			std::string temp2(1, temp[findDash]);
			std::string temp3(1, temp[findDash + 1]);
			temp = temp2 + temp3;
		}
		std::stringstream m(temp);
		m >> number2;

		int findDot = value.find(":");
		character = value[findDot-1];
		int pos = value.find(": ")+2;
		password = value.substr(pos);
		
		if (password[number1-1] == character && password[number2-1] != character) {
			count++;
		}
		else if (password[number1-1] != character && password[number2-1] == character) {
			count++;
		}
	}
	MyreadFile.close();
	return count;
	
}

int main(void) 
{
	int result = getCount();
	std::cout << result;
}