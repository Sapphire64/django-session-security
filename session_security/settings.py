"""
Settings for django-session-security.

WARN_AFTER
    Time (in seconds) counting *forward* from when user session begins
    until when user is warned that session will expire because of
    inactivity. Default 540. Can be set in
    ``settings.SESSION_SECURITY_WARN_AFTER``.

WARN_BEFORE
    Time (in seconds) counting *back* from session expiration when user
    is warned that session will expire because of inactivity. Can be set
    in ``settings.SESSION_SECURITY_WARN_BEFORE``.

EXPIRE_AFTER
    Time (in seconds) before the user should be logged out if inactive. Default
    is 600. Can be set in ``settings.SESSION_SECURITY_EXPIRE_AFTER``.

EXPIRE_AFTER_CUSTOM_SESSION_KEY
    Session key to set a custom EXPIRE_AFTER value. Can be set in
    ``settings.SESSION_SECURITY_CUSTOM_SESSION_KEY``
    Use case: per-user EXPIRE_AFTER

PASSIVE_URLS
    List of urls that should be ignored by the middleware. For example the ping
    ajax request of session_security is made without user intervention, as such
    it should not be used to update the user's last activity datetime. Can be
    set in ``settings.SESSION_SECURITY_PASSIVE_URLS``.

Note that this module will raise a warning if
``settings.SESSION_EXPIRE_AT_BROWSER_CLOSE`` is not True, because it makes no
sense to use this app with ``SESSION_EXPIRE_AT_BROWSER_CLOSE`` to False.
"""

import warnings

from django.core import urlresolvers
from django.conf import settings

__all__ = ['EXPIRE_AFTER', 'WARN_BEFORE', 'WARN_AFTER',
           'PASSIVE_URLS', 'EXPIRE_AFTER_CUSTOM_SESSION_KEY']

EXPIRE_AFTER = getattr(settings, 'SESSION_SECURITY_EXPIRE_AFTER', 600)

EXPIRE_AFTER_CUSTOM_SESSION_KEY = getattr(
    settings, 'SESSION_SECURITY_CUSTOM_SESSION_KEY', None)

WARN_BEFORE = getattr(
    settings, 'SESSION_SECURITY_WARN_BEFORE', None)

WARN_AFTER = getattr(
    settings,
    'SESSION_SECURITY_WARN_AFTER',
    (EXPIRE_AFTER - WARN_BEFORE if WARN_BEFORE else 540)
)

PASSIVE_URLS = getattr(settings, 'SESSION_SECURITY_PASSIVE_URLS', [])
PASSIVE_URLS += [
    urlresolvers.reverse('session_security_ping'),
]

if not getattr(settings, 'SESSION_EXPIRE_AT_BROWSER_CLOSE', False):
    warnings.warn('settings.SESSION_EXPIRE_AT_BROWSER_CLOSE is not True')