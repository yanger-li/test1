#include <iostream>
#include "supplememts/yangliHeader.cpp"

using namespace std;

int main() {
  cout << "Yang Li is a software engineer!" << endl;
  ADCompany x1;
  x1.addInfo("AutoX", 200);
  x1.printInfo();
  return 0;
}
