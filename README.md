Universal Disassembler program for 8-bit microprocessors

This is a simple disassembler for various 8-bit microprocessors. It
reads a binary file specified on the command line and produces a
disassembly. It requires Python 3. It has been tested on Linux but
should work on any platform that supports Python. See the source code
for more details.

The following CPUs are either supported or planned to be supported:

CPU    Status
---    ------

6502    done

65816   done

65C02   done

6800    done

6801/6803 done

6809    done (incomplete)

6811    done

8080    done

8085    done

8051    done (incomplete)

Z80     done

F8      possible

1802    done

TMS9900 possible


usage: udis.py [-h] [-c CPU] [-n] [-a ADDRESS] [-i] filename

positional arguments:

  filename              Binary file to disassemble

optional arguments:

  -h, --help            show this help message and exit

  -c CPU, --cpu CPU     Specify CPU type (defaults to 6502)

  -n, --nolist          Don't list instruction bytes (make output suitable for assembler)

  -a ADDRESS, --address ADDRESS
                        Specify starting address (defaults to 0)

  -i, --invalid         Show invalid opcodes as ??? rather than constants

Files written by me are released under the following license:

Copyright (C) by Jeff Tranter <tranter@pobox.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Documentation written by me is licensed under a Creative Commons
Attribution 4.0 International License.
See https://creativecommons.org/licenses/by/4.0/
