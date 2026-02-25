#include <iostream>
using namespace std;






void part(int arr[] , int n)
{
    int i = 0;
    int a = 0 ,b = 0;
    int p = arr[n];
    int countleft = 0;
    int countright = 0;
    int left[10];
    int right[10];
    
    
while(i<n-1)
    {
        if(p>=arr[i])
        {
            left[a] = arr[i];
            countleft++;
            a++;
            i++;
        }
        
        else if(p<arr[i])
        {
         right[b] = arr[i];
         countright++;
         b++;
         i++;
        }
    }
    
    part(left  , countleft);
    part(right , countright);

    int idx = 0;
for (int i = 0; i < countleft; i++) {
    arr[idx] = left[i];
    idx++;
}

arr[idx++] = p;
  

for (int i = 0; i < countright; i++) {
    arr[idx] = right[i];
    idx++;
    

}

    
    
}


int main() {
    int arr[6] = {5, 2, 6, 4, 1, 3};
    int n = 6;
    part(arr, n);
    

    cout << "Sorted: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    

    return 0;
} 


// // Online C++ compiler to run C++ program online
// #include <iostream>
// using namespace std;

// int power(int n , int x)
// {
//     if(n==1)
//     {
//         return 1;
//     }
    
//     if(n%2 == 0)
//     {
//         return power(n/2,x);
//     }
//     else
//     {
//         return -1;
//     }
// };

// int main() {
//     int num;
//     cout<<"enter a number";
//     cin>>num;
//     int result = power(num, 2);
//     if(result == -1 || result < 0)
//     {
//         cout<<"false not a power of 2";
//     }
//     else
//     {
//         cout<<"true: yes "<<num<<" is a power of 2";
//     }


//     return 0;
// }



// // Online C++ compiler to run C++ program online
// #include <iostream>
// using namespace std;

// int ser(int n)
// {
//     if(n == 1)
//     {
//         return 1;
//     }
//     if(n==2)
//     {
//         return 2;
//     }
//     if(n == 3)
//     {
//         return 3;
//     }
    
//     return ser(n-1) + ser(n-2) + ser(n-3);
// }


// int main(){
    
//     int result = ser(7);
//     cout<<"result : "<<result;
    
//     return 0;
// }



// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    // Write C++ code here
    int arr[7] = {3,1,9,7,1,2,4};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"\n1st Step\n";
    cout<<"maximum element of array : ";
    int max = arr[0];
    for(int i = 1 ; i<n ;i++)
    {
        if(max < arr[i])
        {
        max = arr[i];
        }
    }
    cout<<max;
    
    
    cout<<"\nsecond step\n";
    
    int count[max];
    int a =0;
    for(int j = 0 ; j <= max ; j++)
    {
        count[j] = a;
    }

    for(int k = 0 ; k<= max ;k++)
    {
        cout<<count[k];
    }

    cout<<"\nthird step\n";
    
    int i = 0;
   int j = 0;
    while(i<n && j<= max)
    {
        if(arr[i] == j)
        {
            count[j]++;
            i++;
            j = -1;
        }
        j++;
    }
    

    for(int k = 0 ; k<= max ;k++)
    {
        cout<<count[k];
    }
    
    cout<<"\n fourth step\n";
    int new_arr[n];
    int k = 0;
    while(j<=max && k < n)
    {
        if(count[j] !=0)
        {
            count[j]--;
            new_arr[k] = j;
            k++;
            if(count[j] != 0)
            {    //j =1;
                j--;  // j =0;
            }
        }
        else 
        {
        j++;
        }// j = 1
    }
    
    for(int i = 0 ; i < n ;i++)
    {
        cout<<" "<<new_arr[i]<<" ";
    }
    


    return 0;
}