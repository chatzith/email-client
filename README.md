# Email Client

A small asynchronous Python email subject checker. It matches an incoming subject against the patterns in `scenario.yaml`, then dispatches matching messages to the configured use-case module.

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

The sample subject is configured to trigger `case_a` and prints:

```text
case_a triggered by "tester" with subject "test usecase for testing purposes only" and attachment: False
```

## Configuration

Subject patterns and their use cases are defined in `scenario.yaml`:

```yaml
"Test usecase for testing purposes only": "case_a"
"db update": "case_b"
```

`checker.inspect()` checks the configured regular-expression patterns against the start of the subject, ignoring letter case. It returns the first matching use-case name or `False` when there is no match. Patterns are checked in the order they appear in the YAML file.

## Adding a Use Case

1. Add a subject pattern and package name to `scenario.yaml`.
2. Create a package under `usecases/` with the same name.
3. Add a `main.py` containing an asynchronous `entry_point(sender, subject, att=False)` function.

For example:

```text
usecases/
  invoice_review/
    __init__.py
    main.py
```

```python
async def entry_point(sender: str, subject: str, att: bool = False):
  return (
    f'invoice review triggered by "{sender}" with '
    f'subject "{subject}" and attachment: {att}'
  )
```

When a pattern matches, the dispatcher imports `usecases.<name>.main` dynamically and awaits its `entry_point()` function with the sender, subject, and attachment flag. When no pattern matches, the sample entry point produces no output.

## Project Layout

```text
checker.py       Match subjects to configured use cases.
main.py          Run the checker and dispatch a use case.
settings.py      Load `scenario.yaml`.
scenario.yaml    Map subject patterns to use-case names.
usecases/        Store individual use-case implementations.
```

## Current Use Cases

- `case_a`: Handles subjects beginning with `Test usecase for testing purposes only`.
- `case_b`: Handles subjects beginning with `db update`.
