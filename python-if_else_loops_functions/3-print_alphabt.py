#!/usr/bin/python3

print("{}".format("".join(
    [chr(number) for number in range(ord("a"), ord("z") + 1)
     if chr(number) not in ("e", "q")]
)), end="")

