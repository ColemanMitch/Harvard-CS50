#include <cs50.h>
#include <stdio.h>
#include <crypt.h>
#include <string.h>
#include <ctype.h>

#define _XOPEN_SOURCE
#include <unistd.h>



char *crypt(const char *key, const char *salt);

int main(int argc, string argv[])
{
    if (argc != 2) 
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    else
    {
        string hash = argv[1];
        char salt[3] = "50";
        char pw[5] = "test";
        //
        string alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int length = 52; // number of characters 
        //char c = crypt(, salt);
        //printf("%c", c);

        printf ("Hash is: %s\n", hash);
        printf ("Salt is: %s\n", salt);
        printf("%s\n", crypt(pw, salt));

        // check for one letter pws
        char key1[2];
        for (int i=0; i < length; i++)
        {
            //key1 = {alpha[i], '\0'};
            printf("%s\n", crypt(&alpha[i], salt));   
            //if(strcmp(crypt(key1, "50"), hash) == 0)
            //{
            
              //  break;
            //}
        }
        
        return 0; 
    }
    
}
