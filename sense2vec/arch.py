available = ['null', 'sse2', 'sse3', 'ssse3', 'sse4_1', 'avx', 'avx2', 'fma', 'fma4', 'xop', 'avx512f']


mapping = {
    'null': (None, None),
    'sse2': ('SIMDPP_ARCH_X86_SSE2', '-msse2'),
    'sse3': ('SIMDPP_ARCH_X86_SSE3', '-msse3'),
    'ssse3': ('SIMDPP_ARCH_X86_SSSE3', '-mssse3'),
    'sse4_1': ('SIMDPP_ARCH_X86_SSE4_1', '-msse4.1'),
    'avx': ('SIMDPP_ARCH_X86_AVX', '-mavx'),
    'avx2': ('SIMDPP_ARCH_X86_AVX2', '-mavx2'),
    'fma': ('SIMDPP_ARCH_X86_FMA3', '-mfma'),
    'fma4': ('SIMDPP_ARCH_X86_FMA4', '-mfma4'),
    'xop': ('SIMDPP_ARCH_X86_XOP', '-mxop'),
    'avx512f': ('SIMDPP_ARCH_X86_AVX512F', '-mavx512f'),
}


def get_supported_mapping(flags):
    if 'null' not in flags:
        flags.append('null')
    return dict([(f, mapping[f]) for f
            in flags
            if f in mapping])


def get_supported(flags):
    supported = get_supported_mapping(flags)
    for flag in reversed(available):
        if flag in supported:
            return flag
