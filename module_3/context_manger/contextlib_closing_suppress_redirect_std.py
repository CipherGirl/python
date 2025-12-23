from contextlib import closing, suppress, redirect_stdout, redirect_stderr
import sys

"""
Closing
"""
with closing(open('module_3/context_manger/chat_gpt_notes.md')) as f:
    print(f.read())


"""
Suppress
"""
try:
    1/0
except ZeroDivisionError:
    pass

# Instead we can use suppress

with suppress(ZeroDivisionError):
    1/0

"""
Redirect Standard Output
"""
with(open('module_3/context_manger/help_pow.txt', 'w')) as f:
    with redirect_stdout(f):
        help(pow)

"""
Redirect Standard Error
"""
with(open('module_3/context_manger/error.txt', 'w')) as f:
    with redirect_stderr(f):
        print("Using this as logger", file=sys.stderr)

print("This will only print in std err", file=sys.stderr)