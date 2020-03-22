#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int shift(char c);

int main(int argc, string argv[])
{
    string key;
    if (argc == 2) 
    {
            key = argv[1];
            int n = strlen(key);
            for(int i = 0; i < n; i++) //iterate over the second command line arg   
            {
                
                if (!isalpha(key[i])) // executes if a non-alphabetic argument is passed
                {
                    printf("Usage: ./vigenere keyword\n");
                    return 1;   
                }
            }    
            int k = shift(argv[1][0]);
            int len = strlen(argv[1]);
            string pt = get_string("plaintext: ");
            printf("ciphertext: ");
            int j = 1;
            for (int i=0; i < strlen(pt); i++) 
            {
                
                 if (j == len) // reset index of j back to zero
                {
                    j = 0;
                }  
                if (pt[i] >= 'A' && pt[i] <= 'Z') // 65 - 90
                {
                    if ((int)pt[i] + k > 90) 
                    {
                        printf("%c", pt[i] + k - 91 + 65);
                        j++;
                        k = shift(argv[1][j-1]);
                    }
                    else
                    {
                        printf("%c", pt[i] + k);
                        j++;
                        k = shift(argv[1][j-1]);
                    }
                }
                else if (pt[i] >= 'a' && pt[i] <= 'z') // 97 - 122
                {
                    if ((int)pt[i] + k > 122) 
                    {
                        printf("%c", pt[i] + k - 123 + 97);
                        j++;
                        k = shift(argv[1][j-1]);
                    }
                    else
                    {
                        printf("%c", pt[i] + k);
                        j++;
                        k = shift(argv[1][j-1]);
                    }
                }
               else // if the plain text isn't alphabetic
               {
                   printf("%c", pt[i]); 
               }
            }
          
            printf("\n");
    }
    else
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
    
    
}

int shift(char c) 
{
    if (isupper(c)) // uppercase
    {
        return (int) c - 65;
    }
    else if (islower(c))
    {
        return (int) c - 97;
    }
    else // case if not alphabetic char is provided
    {
        return 0;    
    }
}
