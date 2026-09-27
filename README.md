# Email Client

A small Python email subject checker that dispatches matching messages to configured use cases.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup

Install the project dependencies with:

```powershell
uv sync
```

## Run

Run the sample entry point with:

```powershell
uv run .\main.py
```

The current sample subject is configured to trigger `case_a` and prints:

```text
case_a triggered by tester with subject Test usecase for testing purposes only and attachment: False!
```

## Configuration

Subject patterns and their use cases are defined in `scenario.yaml`:

```yaml
"Test usecase for testing purposes only": "case_a"
"db update": "case_b"
```

`checker.inspect()` checks the configured patterns against the start of the subject, ignoring letter case. It returns the first matching use-case name or `False` when there is no match.

## Adding a Use Case

1. Add a subject pattern and package name to `scenario.yaml`.
2. Create a package under `usecases/` with the same name.
3. Add a `main.py` containing an asynchronous `entry_point(sender, subject, att)` function.

For example:

```text
usecases/
  invoice_review/
    __init__.py
    main.py
```

```python
async def entry_point(sender: str, subject: str, att: bool = False):
    return f"invoice review triggered for {sender}: {subject} (attachment: {att})"
```

The dispatcher imports the matching module dynamically and awaits its `entry_point()` function with the sender, subject, and attachment flag.

## Project Layout

```text
checker.py       Match subjects to configured use cases.
main.py          Run the checker and dispatch a use case.
settings.py      Load `scenario.yaml`.
scenario.yaml    Map subject patterns to use-case names.
usecases/        Store individual use-case implementations.
```
