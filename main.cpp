#include <iostream>
using namespace std;

int main()
{
    int begin, end, i, total=0;
    while(1) {
      cout << " Enter begin and end ";
      cin >> begin >> end;
      if (begin < end)
        break;
    }



    //int flag = 1;
    //while(flag) {
        //cout << " Enter begin and end again ";
        //cin >> begin >> end;
        //if (begin < end)
        //flag = 0;
    
      //}
    if ( begin % 2 == 1)
        begin++;
    i = begin; // 10
    while ( i <= end){
        total = total + i;
        i += 2;
    }
    cout << "Total is " << total << endl;
    return 0;
}