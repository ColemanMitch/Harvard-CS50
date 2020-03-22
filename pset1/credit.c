#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long long cc_num;
    
    cc_num = get_long("Number: "); // acquire number
    
    printf("%lli\n", cc_num);
    long first_num; 
    long first_two;
    int places = 1;
    long cc_num2 = cc_num; // copy of cc number to calculate the number of places
    while (cc_num2 / 10 != 0) {
        cc_num2 /= 10;
        places++; 
        // printf("%li\n", cc_num2);
    }
    //printf("Number of digits: %i\n", places);
    long sum1 = 0; // Luhn's Algo 1st sum - odd place digits
    long sum2 = 0; // Luhn's Algo 2nd sum - even place digits
    first_num = cc_num / ((long)pow(10, places - 1));
    first_two = cc_num / ((long)pow(10, places - 2));
    //printf("First digit = %li\n", first_num);
    //printf("First two digit = %li\n", first_two);
    long long temp_card = cc_num; 
    long digit;
    for (int j = 1; j <= places; j++) 
    {
        digit = (temp_card / (long)pow(10, j - 1)) % 10;
        //printf("Position %i: %li\n", j, digit);
        if (j % 2 == 0) // odd place (10^0, 10^2, etc.)
        {
            digit *= 2;
            if (digit >= 10) 
            {
                digit -= 9;
            }
            sum2 += digit;
            //printf("%i\n",j);
        }
        else // odd place
        {
            sum1 += (digit);
        }      
    }
   long sum3 = sum1 + sum2;     
   
   if (sum3 % 10 != 0 || places > 16 || places < 13) 
   {
       printf("INVALID\n");
   } 
   else if ((first_two == 34 || first_two == 37) && places == 15)
   {
       printf("AMEX\n");
   }
   else if (first_num == 4 && (places == 16 || places == 13))
   {
       printf("VISA\n");
   }
   else if (first_two >= 51 && first_two <= 55 && places == 16)
   {
       printf("MASTERCARD\n");
   }
   else 
   {
       printf("INVALID\n");
   }
}

