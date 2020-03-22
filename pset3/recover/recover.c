#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<cs50.h>



//eliminate magic numbers
#define BLOCK 512

//making a struct
typedef unsigned char BYTE;

int main(int argc, char *argv[])
{

    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // remember filenames
    char *card = argv[1];

    FILE *raw_input = fopen(card, "r");
    if (raw_input == NULL)
    {
        printf("Could not open %s.\n", card);
        return 2;
    }

     //buffer array
    BYTE buffer[BLOCK];

    //to count recovered img number
    int count;
    count = 0;
    char filename[8];

    //file pointer i'll be writing to
    FILE* img;

    while(fread(buffer, sizeof(buffer), 1, raw_input)) // while it is still reading in blocks of bytes that are 512 bytes keep running this loop
    {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) // conditional for the start of a JPEG
        {
            if (count == 0) // branch for first JPEG in memory card file
            {
                sprintf(filename,"%03i.jpg", count); // write "00X.jpg" to char array filename
                count++;
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(buffer), 1, img);
            }
            else if (count > 0) // there is an open JPEG, close it
            {

                fclose(img);
                sprintf(filename,"%03i.jpg", count); // write "00X.jpg" to char array filename
                count++;
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(buffer), 1, img);


            }
        }
        else if (count > 0)
        {
            fwrite(buffer, sizeof(buffer), 1, img);
        }
    }

    fclose(img);
    fclose(raw_input);
    //success
    return 0;
}