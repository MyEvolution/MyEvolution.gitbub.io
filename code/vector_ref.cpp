#include <iostream>
#include <vector>
int main()
{
std::vector<int> array(1);
int &d = array[0];
d = 100;
for(int i = 0;i!=10;++i)
array.push_back(i);
std::cout<<"d = " <<d << std::endl; 
return 0;
}