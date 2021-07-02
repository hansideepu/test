# -*- coding: utf-8 -*-
"""
    flask._compat
    ~~~~~~~~~~~~~

    Some py2/py3 compatibility support based on a stripped down
    version of six so we don't have to depend on a specific version
    of it.

    :copyright: 2010 Pallets
    :license: BSD-3-Clause
"""
import sys

PY2 = sys.version_info[0] == 2
_identity = lambda x: x

try:  # Python 2
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)
except NameError:  # Python 3
    text_type = str
    string_types = (str,)
    integer_types = (int,)

if not PY2:
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    from inspect import getfullargspec as getargspec
    from io import StringIO
    import collections.abc as collections_abc

    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value

    implements_to_string = _identity

else:
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

    from inspect import getargspec
    from cStringIO import StringIO
    import collections as collections_abc

    exec("def reraise(tp, value, tb=None):\n raise tp, value, tb")

    def implements_to_string(cls):
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda x: x.__unicode__().encode("utf-8")
        return cls


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instantiation that replaces
    # itself with the actual metaclass.
    class metaclass(type):
        def __new__(metacls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, "temporary_class", (), {})


# Certain versions of pypy have a bug where clearing the exception stack
# breaks the __exit__ function in a very peculiar way.  The second level of
# exception blocks is necessary because pypy seems to forget to check if an
# exception happened until the next bytecode instruction?
#
# Relevant PyPy bugfix commit:
# https://bitbucket.org/pypy/pypy/commits/77ecf91c635a287e88e60d8ddb0f4e9df4003301
# According to ronan on #pypy IRC, it is released in PyPy2 2.3 and later
# versions.
#
# Ubuntu 14.04 has PyPy 2.2.1, which does exhibit this bug.
BROKEN_PYPY_CTXMGR_EXIT = False
if hasattr(sys, "pypy_version_info"):

    class _Mgr(object):
        def __enter__(self):
            return self

        def __exit__(self, *args):
            if hasattr(sys, "exc_clear"):
                # Python 3 (PyPy3) doesn't have exc_clear
                sys.exc_clear()

    try:
        try:
            with _Mgr():
                raise AssertionError()
        except:  # noqa: B001
            # We intentionally use a bare except here. See the comment above
            # regarding a pypy bug as to why.
            raise
    except TypeError:
        BROKEN_PYPY_CTXMGR_EXIT = True
    except AssertionError:
        pass


try:
    from os import fspath
except ImportError:
    # Backwards compatibility as proposed in PEP 0519:
    # https://www.python.org/dev/peps/pep-0519/#backwards-compatibility
    def fspath(path):
        return path.__fspath__() if hasattr(path, "__fspath__") else path


class _DeprecatedBool(object):
    def __init__(self, name, version, value):
        self.message = "'{}' is deprecated and will be removed in version {}.".format(
            name, version
        )
        self.value = value

    def _warn(self):
        import warnings

        warnings.warn(self.message, DeprecationWarning, stacklevel=2)

    def __eq__(self, other):
        self._warn()
        return other == self.value

    def __ne__(self, other):
        self._warn()
        return other != self.value

    def __bool__(self):
        self._warn()
        return self.value

    __nonzero__ = __bool__


json_available = _DeprecatedBool("flask.json_available", "2.0.0", True)
