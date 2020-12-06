#include<iostream>
#include<fstream>
#include <stdlib.h>
#include<sstream>
#include<string>
#include <Windows.h>
#include<vector>
#include<stdio.h>
#include<vector>
#include<thread>
#include<math.h>
int getCount() {
	std::string value;
	std::string password = "";
	char character;
	int number1;
	int number2;
	int globalCount=0;
	std::ifstream MyreadFile("data.txt");
	while (std::getline(MyreadFile, value)) {
		int count = 0;
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
		std::string temp2;
		int findDash = 0;
		findDash = temp.find("-") + 1;
		
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
		for (char x : password) {
			if (x == character) {
				count++;
			}
			
		}
		if (count <= number2 && count >= number1) {
			globalCount++;
		}
		
	}
	return globalCount;
	MyreadFile.close();
}

int main(void) 
{

	int result;
	result = getCount();
	std::cout << result;
	



}