# Questions

## What's `stdint.h`?

stdint.h is a standard library in C that allows users to use typedefs to define exact width of an integer and the maximum and minimum allowed values for it, using macros.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

It is used to declare an int along with specifications of its size and its sign.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE is 1 byte, DWORD is 4 bytes, LONG is 4 bytes and WORD is 2 bytes.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The first two bytes in ASCII are "B" and "M", and in hexadecimal are 0x42 and 0x4D respectively.

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the bitmap file, and biSize is the size of the BITMAPINFOHEADER file.

## What does it mean if `biHeight` is negative?

If biHeight is negative, th bitmap is bottom-down, which means that it starts from the top left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

If the infiles and outfiles do not exist, fopen may return NULL.

## Why is the third argument to `fread` always `1` in our code?

Because we want to read one byte at a time, since one byte specifies one color out of red, green or blue.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

fseek is used to move file pointer to different positions in the file.

## What is `SEEK_CUR`?

It is used to move file pointer to a given location.

## Whodunit?

It was Professor Plum with the candlestick in the library
