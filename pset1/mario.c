#include <cs50.h>
#include <stdio.h>

int get_height(string prompt);

int main(void)
{
    int h = get_height("Height: ");
    while(h < 1 || h >8)
    {
        h = get_height("Height: ");
    }
    
    for(int i=1; i <= h; i++)
    {
        for(int k=0; k < h-i; k++) // prints the spaces in front of left side 
        {
            printf(" ");            
        }
        for(int k=0; k < i; k++) // prints left side hashes
        {
            printf("#");            
        }
        printf("  "); // two spaces in between the pyramids
        for(int j=0; j<i; j++) // prints the right side of pyramid
        {
            printf("#");
        }
        printf("\n");
    }
    
}

int get_height(string prompt)
{
    int h;
    do
    {
        h = get_int("%s", prompt);
        //printf("%i", h);
    }
    while (h < 1 && h > 8);
    return h;
}
