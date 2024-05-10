#include <iostream>
using namespace std;



void loot_drop_system(){
    string item_rareity_list[6] {"common","uncommon","rare","epic","legendary","hero's"};
    /*
    int possable_number_of_effects[6] {0,1,2,4,6,9};
    */
    string possable_item_effects[4] {"fire damage","frost damage","crit chance","crit damage"};
    for (string i : item_rareity_list){
              cout << i << "\n";
}
}

int main() {
  loot_drop_system();
  return 0;
}
/*
int all_possable_item_stats(){
    string item_rareity_list[6] {"common","uncommon","rare","epic","legendary","hero's"};
    int possable_number_of_effects[6] {0,1,2,4,6,9};
    string possable_item_effects[4] {"fire damage","frost damage","crit chance","crit damage"};
    return
}
*/

  /*
  int i = 0;
  for (;i < 101; i++ )
  {
    if ((i % 2) == 1) {
      cout << i << " is odd\n" ;
    }
    else {
      cout << i << " is even\n" ;
    }
  }
  return 0;
  */
