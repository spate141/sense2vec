#include <math.h>
#include <simdpp/simd.h>

float num_snrm2(const int N, const float *m1, const int incX)
{
    simdpp::float32<SIMDPP_FAST_FLOAT32_SIZE> x;
    simdpp::float32<SIMDPP_FAST_FLOAT32_SIZE> z = simdpp::make_float(0);

    for (int i=0; i<N; i+=SIMDPP_FAST_FLOAT32_SIZE) {
        x = simdpp::load(&m1[i]);
        z = simdpp::add(simdpp::mul(x, x), z);
    }

    return sqrt(simdpp::reduce_add(z));
}

float num_sdot(const int N, const float *m1, const int incX,
                 const float *m2, const int incY)
{
    simdpp::float32<SIMDPP_FAST_FLOAT32_SIZE> x, y;
    simdpp::float32<SIMDPP_FAST_FLOAT32_SIZE> z = simdpp::make_float(0);

    for (int i=0; i<N; i+=SIMDPP_FAST_FLOAT32_SIZE) {
        x = simdpp::load(&m1[i]);
        y = simdpp::load(&m2[i]);
        z = simdpp::add(simdpp::mul(x, y), z);
    }

    return simdpp::reduce_add(z);
}
