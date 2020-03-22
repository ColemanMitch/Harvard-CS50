# Questions

## What's `stdint.h`?

It's a header file that declares a set of ints with a fixed width

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

The typedef uint N_t where N is a power of 2 designates an unsigned integer type with width N

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1 byte, 4 bytes, 4 bytes, 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

"B" and "M" in ASCII

## What's the difference between `bfSize` and `biSize`?

'biSize' is the number of bytes for the bitmap info header structure while 'bfSize' is the size of the bitmap file

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

If the pointer to the file does not exist, 'fopen' will return 'NULL'

## Why is the third argument to `fread` always `1` in our code?

Because it's only reading one element at a time

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

Sets the current position of the stream to a certain offset

## What is `SEEK_CUR`?

The current position of the file pointer
