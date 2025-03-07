# -*- coding: utf-8 -*-
'''
SUSE Manager custom wrapper for Salt "module.run" state module.

This wrapper determines the syntax to use for calling the Salt "module.run" state
that has changed between different Salt version.

Using this wrapper we ensure all SUSE Manager SLS files are using the same syntax
regardless the actual Salt version installed on the minion.

'''
from __future__ import absolute_import

# Import salt libs
from salt.utils.odict import OrderedDict
from salt.states import module

import logging

log = logging.getLogger(__name__)

__virtualname__ = 'mgrcompat'


def __virtual__():
    '''
    This module is always enabled while 'module.run' is available.
    '''
    module.__salt__ = __salt__
    module.__opts__ = __opts__
    module.__pillar__ = __pillar__
    module.__grains__ = __grains__
    module.__context__ = __context__
    module.__utils__ = __utils__
    return __virtualname__

def _tailor_kwargs_to_new_syntax(name, **kwargs):
    nkwargs = {}
    _opt_kwargs = None
    for k, v in kwargs.items():
        if k.startswith("m_"):
            nkwargs[k[2:]] = v
        elif k == 'kwargs':
            _opt_kwargs = kwargs[k]
        else:
            nkwargs[k] = v
    ret = {name: [OrderedDict(nkwargs)]}
    if _opt_kwargs:
        ret[name].append(OrderedDict(_opt_kwargs))
    return ret

def module_run(**kwargs):
    '''
    This function execute the Salt "module.run" state passing the arguments
    in the right way according to the supported syntax depending on the Salt
    minion version and configuration

    '''

    # The new syntax will be used as the default
    use_new_syntax = True

    if __grains__['saltversioninfo'][0] > 3004:
        # Only new syntax - default behavior for Phosphorus and future releases
        pass
    elif __grains__['saltversioninfo'][0] > 2016 and 'module.run' in __opts__.get('use_superseded', []):
        # New syntax - explicitely enabled via 'use_superseded' configuration on 2018.3, 2019.2, 3000.x, 3002.x, 3003.x and 3004.x
        pass
    elif __grains__['saltversioninfo'][0] > 2016 and not 'module.run' in __opts__.get('use_superseded', []):
        # Old syntax - default behavior for 2018.3, 2019.2, 3000.x, 3002.x, 3003.x and 3004.x
        use_new_syntax = False
    elif __grains__['saltversioninfo'][0] <= 2016:
        # Only old syntax - the new syntax is not available for 2016.11 and 2015.8
        use_new_syntax = False

    if use_new_syntax:
        log.debug("Minion is using the new syntax for 'module.run' state. Tailoring parameters.")
        log.debug("Old parameters: {}".format(kwargs))
        old_name = kwargs.pop('name')
        new_kwargs = _tailor_kwargs_to_new_syntax(old_name, **kwargs)
        log.debug("New parameters for 'module.run' state: {}".format(new_kwargs))
    else:
        new_kwargs = kwargs

    ret = module.run(**new_kwargs)
    if use_new_syntax:
        if ret['changes']:
            changes = ret['changes'].pop(old_name)
            ret['changes']['ret'] = changes
        ret['name'] = old_name
    return ret
