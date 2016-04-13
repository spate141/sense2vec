import os
import imp

from . import cpuinfo
from . import arch


flag = arch.get_supported(cpuinfo.get_cpu_info()['flags'])
mod_name = __name__.split('.')[-1]
mod_flag_name = '_'.join([mod_name, flag])
fp, pathname, description = imp.find_module(mod_flag_name, [os.path.dirname(__file__)])

try:
    mod = imp.load_module(mod_name, fp, pathname, description)
finally:
    if fp:
        fp.close()

for name in dir(mod):
    if not name.startswith('__'):
        locals()[name] = getattr(mod, name)
