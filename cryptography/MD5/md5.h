typedef struct{
	unsigned int state[4];
	unsigned int count[2];
	unsigned char buffer[64];
} md5Context;

void md5Init(md5Context*);
void md5Update(md5Context*,unsigned char *, unsigned int);
void md5Final(unsigned char[16],md5Context*);