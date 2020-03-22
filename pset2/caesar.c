#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    int k;
    string key_str;
    if (argc == 2) 
    {
            key_str = argv[1];
            int n = strlen(key_str);
            for(int i = 0; i < n; i++) //iterate    
            {
                
                if (!isdigit(key_str[i])) // executes if a non-numeric argument is passed
                {
                    printf("Usage: ./caesar key\n");
                    return 1;   
                }
            }
            k = atoi(argv[1]);   
            k %= 26;
            //printf("%i\n", k);
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    
    string pt = get_string("plaintext: ");
    printf("ciphertext: ");
    for (int i=0; i < strlen(pt); i++) 
    {
        if (pt[i] >= 'A' && pt[i] <= 'Z') // 65 - 90
        {
            if ((int)pt[i] + k > 90) 
            {
                printf("%c", pt[i] + k - 91 + 65);
            }
            else
            {
                 printf("%c", pt[i] + k);
            }
        }
        else if (pt[i] >= 'a' && pt[i] <= 'z') // 97 - 122
        {
            if ((int)pt[i] + k > 122) 
            {
                printf("%c", pt[i] + k - 123 + 97);
            }
            else
            {
                printf("%c", pt[i] + k);
       
            }
        }
       else
       {
           printf("%c", pt[i]);    
       }
    }
    printf("\n");
}
