// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];


int word_count = 0;

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char w[LENGTH + 1];
    int h;
    // Insert words into hash table
    while (fscanf(file, "%s", w) != EOF)
    {
        // TO DO
        node *new_node = malloc(sizeof(node)); // allocate enough memory for a node pointer
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        strcpy(new_node->word, w); // copies the string into the node
        h = hash(w);
        new_node->next = hashtable[h];
        hashtable[h] = new_node;
        word_count++;
        //printf("%s\n",w);
       // free(new_node);
    }

    // Close dictionary
    fclose(file);

    //printf("word count: %i", word_count);


    // Indicate success
    return true;

}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int i = hash(word);
    node *head = hashtable[i];
    node *cursor = head;

    while(cursor != NULL)
    {
        char wordCopy[LENGTH + 1];
        strcpy(wordCopy, cursor->word);
        if (strcasecmp(word, wordCopy) == 0) // strings are equivalent
        {
            return true;
        }
        cursor = head->next;
        head = cursor;
    }

    return false; // will only return false if it goes throught the entire linked list
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i=0; i < N; i++)
    {
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;

}
