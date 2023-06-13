##########################################################################
#
# Processor specific code

# 13/6/2023: 6801 / 6803 support added by Merlin Skinner-Oakes for Jeff
#            Tranter's Universal Disassembler (udis)

# CPU = "6801"
# Description = "Motorola 6801/6803 8-bit microprocessor."
# DataWidth = 8  # 8-bit data
# AddressWidth = 16  # 16-bit addresses

# Maximum length of an instruction (for formatting purposes)
maxLength = 3

# Leadin bytes for multibyte instructions
leadInBytes = []

# Addressing mode table
# List of addressing modes and corresponding format strings for operands.
addressModeTable = {
"implied"     : "",
"immediate"   : "#${0:02X}",
"immediatex"  : "#${0:02X}{1:02X}",
"direct"      : "${0:02X}",
"indexed"     : "${0:02X},x",
"extended"    : "${0:02X}{1:02X}",
"relative"    : "${0:04X}",
}

# Op Code Table
# Key is numeric opcode (possibly multiple bytes)
# Value is a list:
#   # bytes
#   mnemonic
#   addressing mode
#   flags (e.g. pcr)
opcodeTable = {
0x01 : [ 1, "nop",  "implied"        ],
0x04 : [ 1, "lsld", "implied"        ],     # 6801 / 6803 only
0x05 : [ 1, "asld", "implied"        ],     # 6801 / 6803 only
0x06 : [ 1, "tap",  "implied"        ],
0x07 : [ 1, "tpa",  "implied"        ],
0x08 : [ 1, "inx",  "implied"        ],
0x09 : [ 1, "dex",  "implied"        ],
0x0a : [ 1, "clv",  "implied"        ],
0x0b : [ 1, "sev",  "implied"        ],
0x0c : [ 1, "clc",  "implied"        ],
0x0d : [ 1, "sec",  "implied"        ],
0x0e : [ 1, "cli",  "implied"        ],
0x0f : [ 1, "sei",  "implied"        ],

0x10 : [ 1, "sba",  "implied"        ],
0x11 : [ 1, "cba",  "implied"        ],
0x16 : [ 1, "tab",  "implied"        ],
0x17 : [ 1, "tba",  "implied"        ],
0x19 : [ 1, "daa",  "implied"        ],
0x1b : [ 1, "aba",  "implied"        ],

0x20 : [ 2, "bra",  "relative", pcr  ],
0x21 : [ 2, "brn",  "relative", pcr  ],     # 6801 / 6803 only
0x22 : [ 2, "bhi",  "relative", pcr  ],
0x23 : [ 2, "bls",  "relative", pcr  ],
0x24 : [ 2, "bcc",  "relative", pcr  ],
0x25 : [ 2, "bcs",  "relative", pcr  ],
0x26 : [ 2, "bne",  "relative", pcr  ],
0x27 : [ 2, "beq",  "relative", pcr  ],
0x28 : [ 2, "bvc",  "relative", pcr  ],
0x29 : [ 2, "bvs",  "relative", pcr  ],
0x2a : [ 2, "bpl",  "relative", pcr  ],
0x2b : [ 2, "bmi",  "relative", pcr  ],
0x2c : [ 2, "bge",  "relative", pcr  ],
0x2d : [ 2, "blt",  "relative", pcr  ],
0x2e : [ 2, "bgt",  "relative", pcr  ],
0x2f : [ 2, "ble",  "relative", pcr  ],

0x30 : [ 1, "tsx",  "implied"        ],
0x31 : [ 1, "ins",  "implied"        ],
0x32 : [ 1, "pula", "implied"        ],
0x33 : [ 1, "pulb", "implied"        ],
0x34 : [ 1, "des",  "implied"        ],
0x35 : [ 1, "txs",  "implied"        ],
0x36 : [ 1, "psha", "implied"        ],
0x37 : [ 1, "pshb", "implied"        ],
0x38 : [ 1, "pulx", "implied"        ],     # 6801 / 6803 only
0x39 : [ 1, "rts",  "implied"        ],
0x3a : [ 1, "abx",  "implied"        ],     # 6801 / 6803 only
0x3b : [ 1, "rti",  "implied"        ],
0x3c : [ 1, "pshx", "implied"        ],     # 6801 / 6803 only
0x3d : [ 1, "mul",  "implied"        ],     # 6801 / 6803 only
0x3e : [ 1, "wai",  "implied"        ],
0x3f : [ 1, "swi",  "implied"        ],

0x40 : [ 1, "nega", "implied"        ],
0x43 : [ 1, "coma", "implied"        ],
0x44 : [ 1, "lsra", "implied"        ],
0x46 : [ 1, "rora", "implied"        ],
0x47 : [ 1, "asra", "implied"        ],
0x48 : [ 1, "asla", "implied"        ],
0x49 : [ 1, "rola", "implied"        ],
0x4a : [ 1, "deca", "implied"        ],
0x4c : [ 1, "inca", "implied"        ],
0x4d : [ 1, "tsta", "implied"        ],
0x4f : [ 1, "clra", "implied"        ],

0x50 : [ 1, "negb", "implied"        ],
0x53 : [ 1, "comb", "implied"        ],
0x54 : [ 1, "lsrb", "implied"        ],
0x56 : [ 1, "rorb", "implied"        ],
0x57 : [ 1, "asrb", "implied"        ],
0x58 : [ 1, "aslb", "implied"        ],
0x59 : [ 1, "rolb", "implied"        ],
0x5a : [ 1, "decb", "implied"        ],
0x5c : [ 1, "incb", "implied"        ],
0x5d : [ 1, "tstb", "implied"        ],
0x5f : [ 1, "clrb", "implied"        ],

0x60 : [ 2, "neg",  "indexed"        ],
0x63 : [ 2, "com",  "indexed"        ],
0x64 : [ 2, "lsr",  "indexed"        ],
0x66 : [ 2, "ror",  "indexed"        ],
0x67 : [ 2, "asr",  "indexed"        ],
0x68 : [ 2, "asl",  "indexed"        ],
0x69 : [ 2, "rol",  "indexed"        ],
0x6a : [ 2, "dec",  "indexed"        ],
0x6c : [ 2, "inc",  "indexed"        ],
0x6d : [ 2, "tst",  "indexed"        ],
0x6e : [ 2, "jmp",  "indexed"        ],
0x6f : [ 2, "clr",  "indexed"        ],

0x70 : [ 3, "neg",  "extended"       ],
0x73 : [ 3, "com",  "extended"       ],
0x74 : [ 3, "lsr",  "extended"       ],
0x76 : [ 3, "ror",  "extended"       ],
0x77 : [ 3, "asr",  "extended"       ],
0x78 : [ 3, "asl",  "extended"       ],
0x79 : [ 3, "rol",  "extended"       ],
0x7a : [ 3, "dec",  "extended"       ],
0x7c : [ 3, "inc",  "extended"       ],
0x7d : [ 3, "tst",  "extended"       ],
0x7e : [ 3, "jmp",  "extended"       ],
0x7f : [ 3, "clr",  "extended"       ],

0x80 : [ 2, "suba", "immediate"      ],
0x81 : [ 2, "cmpa", "immediate"      ],
0x82 : [ 2, "sbca", "immediate"      ],
0x83 : [ 3, "subd", "immediatex"     ],     # 6801 / 6803 only
0x84 : [ 2, "anda", "immediate"      ],
0x85 : [ 2, "bita", "immediate"      ],
0x86 : [ 2, "ldaa", "immediate"      ],
0x88 : [ 2, "eora", "immediate"      ],
0x89 : [ 2, "adca", "immediate"      ],
0x8a : [ 2, "oraa", "immediate"      ],
0x8b : [ 2, "adda", "immediate"      ],
0x8c : [ 3, "cpx",  "immediatex"     ],
0x8d : [ 2, "bsr",  "relative", pcr  ],
0x8e : [ 3, "lds",  "immediatex"     ],

0x90 : [ 2, "suba", "direct"         ],
0x91 : [ 2, "cmpa", "direct"         ],
0x92 : [ 2, "sbca", "direct"         ],
0x93 : [ 2, "subd", "direct"         ],     # 6801 / 6803 only
0x94 : [ 2, "anda", "direct"         ],
0x95 : [ 2, "bita", "direct"         ],
0x96 : [ 2, "ldaa", "direct"         ],
0x97 : [ 2, "staa", "direct"         ],
0x98 : [ 2, "eora", "direct"         ],
0x99 : [ 2, "adca", "direct"         ],
0x9a : [ 2, "oraa", "direct"         ],
0x9b : [ 2, "adda", "direct"         ],
0x9c : [ 2, "cpx",  "direct"         ],
0x9d : [ 2, "jsr",  "direct"         ],     # 6801 / 6803 only
0x9e : [ 2, "lds",  "direct"         ],
0x9f : [ 2, "sts",  "direct"         ],

0xa0 : [ 2, "suba", "indexed"        ],
0xa1 : [ 2, "cmpa", "indexed"        ],
0xa2 : [ 2, "sbca", "indexed"        ],
0xa3 : [ 2, "subd", "indexed"        ],     # 6801 / 6803 only
0xa4 : [ 2, "anda", "indexed"        ],
0xa5 : [ 2, "bita", "indexed"        ],
0xa6 : [ 2, "ldaa", "indexed"        ],
0xa7 : [ 2, "staa", "indexed"        ],
0xa8 : [ 2, "eora", "indexed"        ],
0xa9 : [ 2, "adca", "indexed"        ],
0xaa : [ 2, "oraa", "indexed"        ],
0xab : [ 2, "adda", "indexed"        ],
0xac : [ 2, "cpx",  "indexed"        ],
0xad : [ 2, "jsr",  "indexed"        ],
0xae : [ 2, "lds",  "indexed"        ],
0xaf : [ 2, "sts",  "indexed"        ],

0xb0 : [ 3, "suba", "extended"       ],
0xb1 : [ 3, "cmpa", "extended"       ],
0xb2 : [ 3, "sbca", "extended"       ],
0xb3 : [ 3, "subd", "extended"       ],     # 6801 / 6803 only
0xb4 : [ 3, "anda", "extended"       ],
0xb5 : [ 3, "bita", "extended"       ],
0xb6 : [ 3, "ldaa", "extended"       ],
0xb7 : [ 3, "staa", "extended"       ],
0xb8 : [ 3, "eora", "extended"       ],
0xb9 : [ 3, "adca", "extended"       ],
0xba : [ 3, "oraa", "extended"       ],
0xbb : [ 3, "adda", "extended"       ],
0xbc : [ 3, "cpx",  "extended"       ],
0xbd : [ 3, "jsr",  "extended"       ],
0xbe : [ 3, "lds",  "extended"       ],
0xbf : [ 3, "sts",  "extended"       ],

0xc0 : [ 2, "subb", "immediate"      ],
0xc1 : [ 2, "cmpb", "immediate"      ],
0xc2 : [ 2, "sbcb", "immediate"      ],
0xc3 : [ 3, "addd", "immediatex"     ],     # 6801 / 6803 only
0xc4 : [ 2, "andb", "immediate"      ],
0xc5 : [ 2, "bitb", "immediate"      ],
0xc6 : [ 2, "ldab", "immediate"      ],
0xc8 : [ 2, "eorb", "immediate"      ],
0xc9 : [ 2, "adcb", "immediate"      ],
0xca : [ 2, "orab", "immediate"      ],
0xcb : [ 2, "addb", "immediate"      ],
0xcc : [ 3, "ldd",  "immediatex"     ],     # 6801 / 6803 only
0xce : [ 3, "ldx",  "immediatex"     ],

0xd0 : [ 2, "subb", "direct"         ],
0xd1 : [ 2, "cmpb", "direct"         ],
0xd2 : [ 2, "sbcb", "direct"         ],
0xd3 : [ 2, "addd", "direct"         ],     # 6801 / 6803 only
0xd4 : [ 2, "andb", "direct"         ],
0xd5 : [ 2, "bitb", "direct"         ],
0xd6 : [ 2, "ldab", "direct"         ],
0xd7 : [ 2, "stab", "direct"         ],
0xd8 : [ 2, "eorb", "direct"         ],
0xd9 : [ 2, "adcb", "direct"         ],
0xda : [ 2, "orab", "direct"         ],
0xdb : [ 2, "addb", "direct"         ],
0xdc : [ 2, "ldd",  "direct"         ],     # 6801 / 6803 only
0xdd : [ 2, "std",  "direct"         ],     # 6801 / 6803 only
0xde : [ 2, "ldx",  "direct"         ],
0xdf : [ 2, "stx",  "direct"         ],

0xe0 : [ 2, "subb", "indexed"        ],
0xe1 : [ 2, "cmpb", "indexed"        ],
0xe2 : [ 2, "sbcb", "indexed"        ],
0xe3 : [ 2, "addd", "indexed"        ],     # 6801 / 6803 only
0xe4 : [ 2, "andb", "indexed"        ],
0xe5 : [ 2, "bitb", "indexed"        ],
0xe6 : [ 2, "ldab", "indexed"        ],
0xe7 : [ 2, "stab", "indexed"        ],
0xe8 : [ 2, "eorb", "indexed"        ],
0xe9 : [ 2, "adcb", "indexed"        ],
0xea : [ 2, "orab", "indexed"        ],
0xeb : [ 2, "addb", "indexed"        ],
0xec : [ 2, "ldd",  "indexed"        ],     # 6801 / 6803 only
0xed : [ 2, "std",  "indexed"        ],     # 6801 / 6803 only
0xee : [ 2, "ldx",  "indexed"        ],
0xef : [ 2, "stx",  "indexed"        ],

0xf0 : [ 3, "subb", "extended"       ],
0xf1 : [ 3, "cmpb", "extended"       ],
0xf2 : [ 3, "sbcb", "extended"       ],
0xf3 : [ 3, "addd", "extended"       ],     # 6801 / 6803 only
0xf4 : [ 3, "andb", "extended"       ],
0xf5 : [ 3, "bitb", "extended"       ],
0xf6 : [ 3, "ldab", "extended"       ],
0xf7 : [ 3, "stab", "extended"       ],
0xf8 : [ 3, "eorb", "extended"       ],
0xf9 : [ 3, "adcb", "extended"       ],
0xfa : [ 3, "orab", "extended"       ],
0xfb : [ 3, "addb", "extended"       ],
0xfc : [ 3, "ldd",  "extended"       ],     # 6801 / 6803 only
0xfd : [ 3, "std",  "extended"       ],     # 6801 / 6803 only
0xfe : [ 3, "ldx",  "extended"       ],
0xff : [ 3, "stx",  "extended"       ],

}

# End of processor specific code
##########################################################################
