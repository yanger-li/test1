#include <iostream>

using namespace std;

class ADCompany {
public:
  ADCompany();                      // This is constructor declaration
  ~ADCompany();                     // This is destructor declaration
  void addInfo (string companyNameVal, int NoOfEmployeesVal) {
    companyName = companyNameVal;
    NoOfEmployees = NoOfEmployeesVal;
  }

  void printInfo() {
    cout << "This company's name is " << companyName << "," << endl;
    cout << "This company has " << NoOfEmployees << " employees." << endl;
  }

private:
  string companyName;
  int NoOfEmployees;
};

ADCompany::ADCompany (void) {
  cout << "A new company is being added. " << endl;
}

ADCompany::~ADCompany (void) {
  cout << "A new company is being deleted. " << endl;
}
