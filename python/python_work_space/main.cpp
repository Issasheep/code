#include <iostream>
#include <random>
#include<stdlib.h>
using namespace std; 


void randomGenerator()
{
    int i;          //loop counter
    int num;        //store random number

    int randomize();    //call it once to generate random number
    for(i=1;i<=10;i++)
    {
        num=rand()%100; //get random number
        cout << num << "\n";
    }

}

int main(){
    randomGenerator();
    return 0;
}

void loot_drop_system(){
    string item_rareity_list[6] {"common","uncommon","rare","epic","legendary","hero's"};
    int possable_number_of_effects[6] {0,1,2,4,6,9};
    string possable_item_effects[4] {"fire damage","frost damage","crit chance","crit damage"};
    for (string i : item_rareity_list){
      cout << i << "\n";
    }
    for (string index : possable_item_effects){
      cout << index << "\n";
}
}
int random_number_gen(){
  random_device srand;  
    mt19937 gen(srand());  
  uniform_int_distribution<int>dis(1, 1000);  

    int random_number = dis(gen);  
  return random_number; 
}

/*
int main(){
  for (int i = 0; i < 5; i++){
    cout << random_number_gen(); cout << "\n";
  }
    for (int i = 0; i < 5; i++){
    cout << random_number_gen(); cout << "\n";
  }
  cout << random_number_gen();
  return 0;
}
*/