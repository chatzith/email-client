"""Provide the asynchronous entry point for the database update case."""


async def entry_point(sender: str, subject: str, att: bool = False):
    """Return a message describing the triggered database update use case.

    Args:
        sender: Email sender.
        subject: Email subject.
        att: Whether the email has an attachment.

    Returns:
        A message describing the triggered database update use case.
    """
    return (
        f'case_a triggered by "{sender}" with subject "{subject}" and attachment: {att}'
    )
