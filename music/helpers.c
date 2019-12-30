// Helper functions for music
#include<stdio.h>
#include <cs50.h>
#include <math.h>
#include<string.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // TODO
    int numerator = fraction[0] - '0';
    int denominator = fraction[2] - '0';
    return ((numerator*8)/denominator);
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // TODO
    int octave1;
    char key[3];


    if(note[1] == '#' || note[1] == 'b')
    {
        octave1 = note[2] - '0';
        key[0]=note[0];
        key[1]=note[1];
        key[2]= '\0';
    }
    else
    {
        key[0] = note[0];
        key[1] = '\0';
        octave1 = note[1] - '0';
    }
    int x;
    int y=0;
    x= 12*(octave1 -4);
    string keys[] = {"C", "C#", "D", "D#", "E", "F",
                    "F#", "G", "G#", "A", "A#", "B"};

    string keys1[] = {"C", "Db", "D", "Eb", "E", "F",
                    "Gb", "G", "Ab", "A", "Bb", "B"};

    int index=10;
    for(int i=0; i<12; i++)
    {

        if(strcmp(key, keys[i])==0)
        {
            index = i-9;
            break;
        }
        else if(strcmp(key, keys1[i])==0)
        {
            index = i-9;
            break;
        }
        else
        {
            continue;
        }
    }

    float q=0;
    q = index + x;
    float f = q/12;
    return (int)round(pow(2, f) * 440);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    // TODO
    if(s[0]=='\0')
    {
        return true;
    }
    else

        return false;

}
