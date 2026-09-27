"""Resolve incoming email subjects to configured use-case module names."""

import re

import settings


def inspect(sender: str, subject: str, att: bool = False) -> str | bool:
    """Return the first case-insensitive subject-prefix match, or ``False``.

    Args:
        sender: Email sender, retained for the checker interface.
        subject: Email subject to compare with configured patterns.
        att: Whether the email has an attachment, retained for the checker
            interface.

    Returns:
        The configured use-case module name, or ``False`` when no pattern
        matches the subject.
    """
    configs = settings.Settings()
    for key, usecase in configs.usecases.items():
        if re.match(key, subject, re.IGNORECASE):
            return usecase
    return False
