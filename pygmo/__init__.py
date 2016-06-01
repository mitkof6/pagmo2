# -*- coding: utf-8 -*-

from __future__ import absolute_import as _ai

__all__ = ['core']

# Problem extract functionality.
def _problem_extract(self,t):
    """Extract user-defined problem instance.

    If *t* is the same type of the user-defined problem used to construct this problem, then a deep copy of
    the user-defined problem will be returned. Otherwise, ``None`` will be returned.

    :param t: the type of the user-defined problem to extract
    :type t: ``type``
    :returns: a deep-copy of the internal user-defined problem if it is of type *t*, or ``None`` otherwise
    :rtype: *t*
    :raises: :exc:`TypeError` if *t* is not a type

    """
    if not isinstance(t,type):
        raise TypeError("the 't' parameter must be a type")
    if hasattr(t,"_pygmo_cpp_problem"):
        try:
            return self._cpp_extract(t())
        except TypeError:
            return None
    try:
        return self._py_extract(t)
    except TypeError:
        return None

def _problem_is(self,t):
    """Check the type of the user-defined problem instance.

    If *t* is the same type of the user-defined problem used to construct this problem, then ``True`` will be
    returned. Otherwise, ``False`` will be returned.

    :param t: the type of the user-defined problem to extract
    :type t: ``type``
    :returns: a boolean indicating whether the user-defined problem is of type *t* or not
    :rtype: ``bool``
    :raises: :exc:`TypeError` if *t* is not a type

    """
    return not self.extract(t) is None

# Algorithm extract functionality.
def _algorithm_extract(self,t):
    """Extract user-defined algorithm instance.

    If *t* is the same type of the user-defined algorithm used to construct this algorithm, then a deep copy of
    the user-defined algorithm will be returned. Otherwise, ``None`` will be returned.

    :param t: the type of the user-defined algorithm to extract
    :type t: ``type``
    :returns: a deep-copy of the internal user-defined algorithm if it is of type *t*, or ``None`` otherwise
    :rtype: *t*
    :raises: :exc:`TypeError` if *t* is not a type

    """
    if not isinstance(t,type):
        raise TypeError("the 't' parameter must be a type")
    if hasattr(t,"_pygmo_cpp_algorithm"):
        try:
            return self._cpp_extract(t())
        except TypeError:
            return None
    try:
        return self._py_extract(t)
    except TypeError:
        return None

def _algorithm_is(self,t):
    """Check the type of the user-defined algorithm instance.

    If *t* is the same type of the user-defined algorithm used to construct this algorithm, then ``True`` will be
    returned. Otherwise, ``False`` will be returned.

    :param t: the type of the user-defined algorithm to extract
    :type t: ``type``
    :returns: a boolean indicating whether the user-defined algorithm is of type *t* or not
    :rtype: ``bool``
    :raises: :exc:`TypeError` if *t* is not a type

    """
    return not self.extract(t) is None

from .core import *

# Setup the extract and is methods for problem and meta-problems.
setattr(problem,"extract",_problem_extract)
setattr(problem,"is_",_problem_is)
setattr(translate,"extract",_problem_extract)
setattr(translate,"is_",_problem_is)

# Same for algorithm and meta-algorithms.
setattr(algorithm,"extract",_algorithm_extract)
setattr(algorithm,"is_",_algorithm_is)

# Register the cleanup function.
import atexit as _atexit
from .core import _cleanup
_atexit.register(lambda : _cleanup())
