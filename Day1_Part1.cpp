#include<iostream>
#include<fstream>
#include <stdlib.h>
#include<sstream>
#include <Windows.h>
#include<vector>
#include<stdio.h>
#include<vector>
#include<thread>
#include<math.h>
int getMultiple() {
	std::string value;
	std::string value2;
	int distance1;
	int distance2;
	std::vector<int> vec;
	std::ifstream MyreadFile("data.txt");
	std::ifstream MyreadFile2("data.txt");
	while (std::getline(MyreadFile, value)) {
		std::stringstream n(value);
		n >> distance1;
		vec.push_back(distance1);
		
	}
	for (int i = 0; i < vec.size(); i++) {
		for (int j = 0; j < vec.size(); j++) {
			if (vec.at(i) + vec.at(j) == 2020) {
				//std::cout << "cheche";
				return vec.at(i) * vec.at(j);
			}
		}
	}
	return 0;
	MyreadFile.close();
}

int main(void) 
{

	int result;
	result = getMultiple();
	std::cout << result;
	



}