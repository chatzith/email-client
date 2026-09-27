"""Run a sample email through subject matching and asynchronous dispatch."""

import asyncio
import importlib

import checker

SENDER = "tester"
SUBJECT = "test usecase for testing purposes only"
HAS_ATT = False


async def main():
    """Match the sample email and await its configured use-case entry point."""
    result = checker.inspect(SENDER, SUBJECT, HAS_ATT)

    if result:
        usecase = importlib.import_module(f"usecases.{result}.main")
        print(await usecase.entry_point(SENDER, SUBJECT, HAS_ATT))


asyncio.run(main())
