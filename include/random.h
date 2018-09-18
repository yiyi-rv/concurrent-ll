#ifndef _H_RANDOM_
#define _H_RANDOM_

#ifndef __APPLE__
#include <malloc.h>
#elif defined(__APPLE__)
#include <stdlib.h>
#endif

#define LOCAL_RAND
#if defined(LOCAL_RAND)
extern __thread unsigned long *seeds;
#endif

#define my_random xorshf96

/* Mac OSX lack of memalign but has posix_memalign */
#if defined(__APPLE__)
static inline
void *memalign(size_t size, size_t alignment)
{
    void *buffer;
    posix_memalign(&buffer, alignment, size);
    return buffer;
}
#endif

/* fast but weak random number generator */
static inline
uint32_t fast_rand()
{
    return ((getticks() & 4294967295UL) >> 4);
}

static inline
unsigned long *seed_rand()
{
    unsigned long *seeds;
    seeds = (unsigned long *)memalign(64, 64);
    seeds[0] = getticks() % 123456789;
    seeds[1] = getticks() % 362436069;
    seeds[2] = getticks() % 521288629;
    return seeds;
}

static inline
unsigned long *yiyi_seed_rand()
{
    unsigned long *seeds;
    seeds = (unsigned long *)memalign(64, 64);
    seeds[0] = 16387575;
    seeds[1] = 256656994;
    seeds[2] = 501352646;
    return seeds;
}

/* Marsaglia's xorshf generator */
static inline
unsigned long xorshf96(unsigned long *x,
                       unsigned long *y,
                       unsigned long *z)
{
    /* period 2^96-1 */
    unsigned long t;
    (*x) ^= (*x) << 16;
    (*x) ^= (*x) >> 5;
    (*x) ^= (*x) << 1;

    t = *x;
    (*x) = *y;
    (*y) = *z;
    (*z) = t ^ (*x) ^ (*y);

    return *z;
}

static inline
long rand_range(long r)
{
#if defined(LOCAL_RAND)
    long v = xorshf96(seeds, seeds + 1, seeds + 2) % r;
    v++;
#else
    int m = RAND_MAX;
    long d, v = 0;

    do {
        d = (m > r ? r : m);
        v += 1 + (long)(d * ((double)rand() / ((double)(m) + 1.0)));
        r -= m;
    } while (r > 0);
#endif
    return v;
}

/* Re-entrant version of rand_range(r) */
static inline
long rand_range_re(unsigned int *seed, long r)
{
#if defined(LOCAL_RAND)
    long v = xorshf96(seeds, seeds + 1, seeds + 2) % r;
    v++;
#else
    int m = RAND_MAX;
    long d, v = 0;

    do {
        d = (m > r ? r : m);
        v += 1 + (long)(d * ((double)rand_r(seed) / ((double)(m) + 1.0)));
        r -= m;
    } while (r > 0);
#endif
    return v;
}

#endif
