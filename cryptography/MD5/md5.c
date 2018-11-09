#include "md5.h"

//Constants for MD5 rounds
#define S11 7
#define S12 12
#define S13 17
#define S14 22
#define S21 5
#define S22 9
#define S23 14
#define S24 20
#define S31 4
#define S32 11
#define S33 16
#define S34 23
#define S41 6
#define S42 10
#define S43 15
#define S44 21

//Constant functions defined as marco
#define ROTATE_LEFT(x,n) (((x)<<(n))|((x)>>(32-(n))))
#define F(x, y, z) (((x) & (y)) | ((~x) & (z)))
#define G(x, y, z) (((x) & (z)) | ((y) & (~z)))
#define H(x, y, z) ((x) ^ (y) ^ (z))
#define I(x, y, z) ((y) ^ ((x) | (~z)))

#define FR(a, b, c, d, x, s, ac) { \
(a) += F ((b), (c), (d)) + (x) + (UINT4)(ac); \
(a) = ROTATE_LEFT ((a), (s)); \
(a) += (b);}
#define GR(a, b, c, d, x, s, ac) { \
(a) += G ((b), (c), (d)) + (x) + (UINT4)(ac); \
(a) = ROTATE_LEFT ((a), (s)); \
(a) += (b);}
#define HR(a, b, c, d, x, s, ac) { \
(a) += H ((b), (c), (d)) + (x) + (UINT4)(ac); \
(a) = ROTATE_LEFT ((a), (s)); \
(a) += (b);}
#define IR(a, b, c, d, x, s, ac) { \
(a) += I ((b), (c), (d)) + (x) + (UINT4)(ac); \
(a) = ROTATE_LEFT ((a), (s)); \
(a) += (b);}

// assign size_t if it is not mentioned before
#ifndef size_t
#define size_t unsigned short
#endif

// funstion only used in this c file
static void md5Transform(int [4],  unsigned char [64]);
static void encode(unsigned char *, unsigned int  *, unsigned int);
static void decode(unsigned int  *, unsigned char *, unsigned int);

#ifndef memcpy
void *memcpy(void *dest, const void *src, size_t len)
{
	char *d = dest;
	const char *s = src;
	while (len--)
		*d++ = *s++;
	return dest;
}
#endif

#ifndef memset
void *memset(void *dest, const void c, size_t n)
{
	if(n)
	{
		char *d = dest;
		while(n--)
			*d++ = c;
	}
	return dest
}
#endif

const unsigned char PADDING[64] = {0x80,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0};

void md5Init(md5Context *context)
{
	context -> count[0] = 0;
	context -> count[1] = 1;
	context -> state[0] = 0x67452301;
	context -> state[1] = 0xefcdab89;
	context -> state[2] = 0x98badcfe;
	context -> state[3] = 0x10325476;	
}

