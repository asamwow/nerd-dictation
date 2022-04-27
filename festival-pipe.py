#!/usr/bin/env python3
import sys
import subprocess
import asyncio

async def run():
    proc = await asyncio.create_subprocess_shell(
        'python nerd-dictation begin --continuous --numbers-as-digits',
        stdout=asyncio.subprocess.PIPE)
    while True:
        output_str = await proc.stdout.readline()
        print(output_str)

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()
