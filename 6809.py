##########################################################################
#
# Processor specific code

# CPU = "6809"
# Description = "Motorola 6809 8-bit microprocessor."
# DataWidth = 8 # 8-bit data
# AddressWidth = 16 # 16-bit addresses

# Maximum length of an instruction (for formatting purposes)
maxLength = 4

# Leadin bytes for multbyte instructions
leadInBytes = [0x10, 0x11]

# Notes:
# Not all addressing modes are implemented.

# Addressing mode table
addressModeTable = {
"inherent"    : "",
"imm8"        : "#${0:02X}",
"imm16"       : "#${0:02X}{1:02X}",
"direct"      : "${0:02X}",
"indexed"     : "${0:02X},x",
"extended"    : "${0:02X}{1:02X}",
"rel8"        : "${0:04X}",
"rel16"       : "${0:02X}{1:02X}",
"r1,r2"       : "${0:02X}",  # Not fully implemented
# Extended Indirect
# Relative Indirect
# Zero-offset Indexed
# Zero-offset Indexed Indirect
# Constant-offset Indexed
# Constant-offset Indexed Indirect
# Accumulator-offset Indexed
# Accumulator-offset Indexed Indirect
# Auto-Increment Indexed
# Auto-Increment Indexed Indirect
# Auto-Decrement Indexed
# Auto-Decrement Indexed Indirect
}

# Op Code Table
# Key is numeric opcode (possibly multiple bytes)
# Value is a list:
#   # bytes
#   mnemonic
#   addressing mode.
#   flags (e.g. pcr)
opcodeTable = {

0x3a   :  [ 1, "abx",  "inherent"        ],
0x89   :  [ 2, "adca", "imm8"            ],
0x99   :  [ 2, "adca", "direct"          ],
0xa9   :  [ 2, "adca", "indexed"         ],
0xb9   :  [ 3, "adca", "extended"        ],
0xc9   :  [ 2, "adcb", "imm8"            ],
0xd9   :  [ 2, "adcb", "direct"          ],
0xe9   :  [ 2, "adcb", "indexed"         ],
0xf9   :  [ 3, "adcb", "extended"        ],
0x8b   :  [ 2, "adda", "imm8"            ],
0x9b   :  [ 2, "adda", "direct"          ],
0xab   :  [ 2, "adda", "indexed"         ],
0xbb   :  [ 3, "adda", "extended"        ],
0xcb   :  [ 2, "addb", "imm8"            ],
0xdb   :  [ 2, "addb", "direct"          ],
0xeb   :  [ 2, "addb", "indexed"         ],
0xfb   :  [ 3, "addb", "extended"        ],
0xc3   :  [ 3, "addd", "imm16"           ],
0xd3   :  [ 2, "addd", "direct"          ],
0xe3   :  [ 2, "addd", "indexed"         ],
0xf3   :  [ 3, "addd", "extended"        ],
0x84   :  [ 2, "anda", "imm8"            ],
0x94   :  [ 2, "anda", "direct"          ],
0xa4   :  [ 2, "anda", "indexed"         ],
0xb4   :  [ 3, "anda", "extended"        ],
0xc4   :  [ 2, "andb", "imm8"            ],
0xd4   :  [ 2, "andb", "direct"          ],
0xe4   :  [ 2, "andb", "indexed"         ],
0xf4   :  [ 3, "andb", "extended"        ],
0x1c   :  [ 2, "andcc","imm8"            ],
0x48   :  [ 1, "asla", "inherent"        ],
0x58   :  [ 1, "aslb", "inherent"        ],
0x08   :  [ 2, "asl",  "direct"          ],
0x68   :  [ 2, "asl",  "indexed"         ],
0x78   :  [ 3, "asl",  "extended"        ],
0x47   :  [ 1, "asra", "inherent"        ],
0x57   :  [ 1, "asrb", "inherent"        ],
0x07   :  [ 2, "asr",  "direct"          ],
0x67   :  [ 2, "asr",  "indexed"         ],
0x77   :  [ 3, "asr",  "extended"        ],
0x85   :  [ 2, "bita", "imm8"            ],
0x95   :  [ 2, "bita", "direct"          ],
0xa5   :  [ 2, "bita", "indexed"         ],
0xb5   :  [ 3, "bita", "extended"        ],
0xc5   :  [ 2, "bitb", "imm8"            ],
0xd5   :  [ 2, "bitb", "direct"          ],
0xe5   :  [ 2, "bitb", "indexed"         ],
0xf5   :  [ 3, "bitb", "extended"        ],
0x4f   :  [ 1, "clra", "inherent"        ],
0x5f   :  [ 1, "clrb", "inherent"        ],
0x0f   :  [ 2, "clr",  "direct"          ],
0x6f   :  [ 2, "clr",  "indexed"         ],
0x7f   :  [ 3, "clr",  "extended"        ],
0x81   :  [ 2, "cmpa", "imm8"            ],
0x91   :  [ 2, "cmpa", "direct"          ],
0xa1   :  [ 2, "cmpa", "indexed"         ],
0xb1   :  [ 3, "cmpa", "extended"        ],
0xc1   :  [ 2, "cmpb", "imm8"            ],
0xd1   :  [ 2, "cmpb", "direct"          ],
0xe1   :  [ 2, "cmpb", "indexed"         ],
0xf1   :  [ 3, "cmpb", "extended"        ],
0x1083 :  [ 4, "cmpd", "imm16"           ],
0x1093 :  [ 3, "cmpd", "direct"          ],
0x10a3 :  [ 3, "cmpd", "indexed"         ],
0x10b3 :  [ 4, "cmpd", "extended"        ],
0x118c :  [ 4, "cmps", "imm16"           ],
0x119c :  [ 3, "cmps", "direct"          ],
0x11ac :  [ 3, "cmps", "indexed"         ],
0x11bc :  [ 4, "cmps", "extended"        ],
0x1183 :  [ 4, "cmpu", "imm16"           ],
0x1193 :  [ 3, "cmpu", "direct"          ],
0x11a3 :  [ 3, "cmpu", "indexed"         ],
0x11b3 :  [ 4, "cmpu", "extended"        ],
0x8c   :  [ 3, "cmpx", "imm16"           ],
0x9c   :  [ 2, "cmpx", "direct"          ],
0xac   :  [ 2, "cmpx", "indexed"         ],
0xbc   :  [ 3, "cmpx", "extended"        ],
0x108c :  [ 4, "cmpy", "imm16"           ],
0x109c :  [ 3, "cmpy", "direct"          ],
0x10ac :  [ 3, "cmpy", "indexed"         ],
0x10bc :  [ 4, "cmpy", "extended"        ],
0x43   :  [ 1, "coma", "inherent"        ],
0x53   :  [ 1, "comb", "inherent"        ],
0x03   :  [ 2, "comb", "direct"          ],
0x63   :  [ 2, "comb", "indexed"         ],
0x73   :  [ 3, "comb", "extended"        ],
0x3c   :  [ 2, "cwai", "imm8"            ],
0x19   :  [ 1, "daa",  "inherent"        ],
0x4a   :  [ 1, "deca", "inherent"        ],
0x5a   :  [ 1, "decb", "inherent"        ],
0x0a   :  [ 2, "dec",  "direct"          ],
0x6a   :  [ 2, "dec",  "indexed"         ],
0x7a   :  [ 3, "dec",  "extended"        ],
0x88   :  [ 2, "eora", "imm8"            ],
0x98   :  [ 2, "eora", "direct"          ],
0xa8   :  [ 2, "eora", "direct"          ],
0xb8   :  [ 3, "eora", "extended"        ],
0xc8   :  [ 2, "eorb", "imm8"            ],
0xd8   :  [ 2, "eorb", "direct"          ],
0xe8   :  [ 2, "eorb", "direct"          ],
0xf8   :  [ 3, "eorb", "extended"        ],
0x1e   :  [ 2, "exg",  "r1,r2"           ],
0x4c   :  [ 1, "inca", "inherent"        ],
0x5c   :  [ 1, "incb", "inherent"        ],
0x0c   :  [ 2, "inc",  "indexed"         ],
0x6c   :  [ 2, "inc",  "direct"          ],
0x7c   :  [ 3, "inc",  "extended"        ],
0x0e   :  [ 2, "jmp",  "indexed"         ],
0x6e   :  [ 2, "jmp",  "direct"          ],
0x7e   :  [ 3, "jmp",  "extended"        ],
0x9d   :  [ 2, "jsr",  "indexed"         ],
0xad   :  [ 2, "jsr",  "direct"          ],
0xbd   :  [ 3, "jsr",  "extended"        ],
0x86   :  [ 2, "lda",  "imm8"            ],
0x96   :  [ 2, "lda",  "direct"          ],
0xa6   :  [ 2, "lda",  "indexed"         ],
0xb6   :  [ 3, "lda",  "extended"        ],
0xc6   :  [ 2, "ldb",  "imm8"            ],
0xd6   :  [ 2, "ldb",  "direct"          ],
0xe6   :  [ 2, "ldb",  "indexed"         ],
0xf6   :  [ 3, "ldb",  "extended"        ],
0xcc   :  [ 3, "ldd",  "imm16"           ],
0xdc   :  [ 2, "ldd",  "direct"          ],
0xec   :  [ 2, "ldd",  "indexed"         ],
0xfc   :  [ 3, "ldd",  "extended"        ],
0x10ce :  [ 4, "lds",  "imm16"           ],
0x10de :  [ 3, "lds",  "direct"          ],
0x10ee :  [ 3, "lds",  "indexed"         ],
0x10fe :  [ 4, "lds",  "extended"        ],
0xce   :  [ 3, "ldu",  "imm16"           ],
0xde   :  [ 2, "ldu",  "direct"          ],
0xee   :  [ 2, "ldu",  "indexed"         ],
0xfe   :  [ 3, "ldu",  "extended"        ],
0x8e   :  [ 3, "ldx",  "imm16"           ],
0x9e   :  [ 2, "ldx",  "direct"          ],
0xae   :  [ 2, "ldx",  "indexed"         ],
0xbe   :  [ 3, "ldx",  "extended"        ],
0x108e :  [ 4, "ldy",  "imm16"           ],
0x109e :  [ 4, "ldy",  "direct"          ],
0x10ae :  [ 4, "ldy",  "indexed"         ],
0x10be :  [ 4, "ldy",  "extended"        ],
0x32   :  [ 2, "leas", "indexed"         ],
0x33   :  [ 2, "leau", "indexed"         ],
0x30   :  [ 2, "leax", "indexed"         ],
0x31   :  [ 2, "leay", "indexed"         ],
0x48   :  [ 1, "lsla", "inherent"        ],
0x58   :  [ 1, "lslb", "inherent"        ],
0x08   :  [ 2, "lsl",  "direct"          ],
0x68   :  [ 2, "lsl",  "indexed"         ],
0x78   :  [ 3, "lsl",  "extended"        ],
0x44   :  [ 1, "lsra", "inherent"        ],
0x54   :  [ 1, "lsrb", "inherent"        ],
0x04   :  [ 2, "lsr",  "direct"          ],
0x64   :  [ 2, "lsr",  "indexed"         ],
0x74   :  [ 3, "lsr",  "extended"        ],
0x3d   :  [ 1, "mul",  "inherent"        ],
0x40   :  [ 1, "nega", "inherent"        ],
0x50   :  [ 1, "negb", "inherent"        ],
0x00   :  [ 2, "neg",  "direct"          ],
0x60   :  [ 2, "neg",  "indexed"         ],
0x70   :  [ 3, "neg",  "extended"        ],
0x12   :  [ 1, "nop",  "inherent"        ],
0x8a   :  [ 2, "ora",  "imm8"            ],
0x9a   :  [ 2, "ora",  "direct"          ],
0xaa   :  [ 2, "ora",  "indexed"         ],
0xba   :  [ 3, "ora",  "extended"        ],
0xca   :  [ 2, "orb",  "imm8"            ],
0xda   :  [ 2, "orb",  "direct"          ],
0xea   :  [ 2, "orb",  "indexed"         ],
0xfa   :  [ 3, "orb",  "extended"        ],
0x1a   :  [ 2, "orcc", "imm8"            ],
0x34   :  [ 2, "pshs", "imm8"            ],
0x36   :  [ 2, "pshu", "imm8"            ],
0x35   :  [ 2, "puls", "imm8"            ],
0x37   :  [ 2, "pulu", "imm8"            ],
0x49   :  [ 1, "rola", "inherent"        ],
0x59   :  [ 1, "rolb", "inherent"        ],
0x09   :  [ 2, "rol",  "direct"          ],
0x69   :  [ 2, "rol",  "indexed"         ],
0x79   :  [ 3, "rol",  "extended"        ],
0x46   :  [ 1, "rora", "inherent"        ],
0x56   :  [ 1, "rorb", "inherent"        ],
0x06   :  [ 2, "ror",  "direct"          ],
0x66   :  [ 2, "ror",  "indexed"         ],
0x76   :  [ 3, "ror",  "extended"        ],
0x3b   :  [ 1, "rti",  "inherent"        ],
0x39   :  [ 1, "rts",  "inherent"        ],
0x82   :  [ 2, "sbca", "imm8"            ],
0x92   :  [ 2, "sbca", "direct"          ],
0xa2   :  [ 2, "sbca", "indexed"         ],
0xb2   :  [ 3, "sbca", "extended"        ],
0xc2   :  [ 2, "sbcb", "imm8"            ],
0xd2   :  [ 2, "sbcb", "direct"          ],
0xe2   :  [ 2, "sbcb", "indexed"         ],
0xf2   :  [ 3, "sbcb", "extended"        ],
0x1d   :  [ 1, "sex",  "inherent"        ],
0x97   :  [ 2, "sta",  "direct"          ],
0xa7   :  [ 2, "sta",  "indexed"         ],
0xb7   :  [ 3, "sta",  "extended"        ],
0xd7   :  [ 2, "stb",  "direct"          ],
0xe7   :  [ 2, "stb",  "indexed"         ],
0xf7   :  [ 3, "stb",  "extended"        ],
0xdd   :  [ 2, "std",  "direct"          ],
0xed   :  [ 2, "std",  "indexed"         ],
0xfd   :  [ 3, "std",  "extended"        ],
0x10df :  [ 3, "sts",  "direct"          ],
0x10ef :  [ 3, "sts",  "indexed"         ],
0x10ff :  [ 4, "sts",  "extended"        ],
0xdf   :  [ 2, "stu",  "direct"          ],
0xef   :  [ 2, "stu",  "indexed"         ],
0xff   :  [ 3, "stu",  "extended"        ],
0x9f   :  [ 2, "stx",  "direct"          ],
0xaf   :  [ 2, "stx",  "indexed"         ],
0xbf   :  [ 3, "stx",  "extended"        ],
0x109f :  [ 3, "sty",  "direct"          ],
0x10af :  [ 3, "sty",  "indexed"         ],
0x10bf :  [ 4, "sty",  "extended"        ],
0x80   :  [ 2, "suba", "imm8"            ],
0x90   :  [ 2, "suba", "direct"          ],
0xa0   :  [ 2, "suba", "indexed"         ],
0xb0   :  [ 3, "suba", "extended"        ],
0xc0   :  [ 2, "subb", "imm8"            ],
0xd0   :  [ 2, "subb", "direct"          ],
0xe0   :  [ 2, "subb", "indexed"         ],
0xf0   :  [ 3, "subb", "extended"        ],
0x83   :  [ 3, "subd", "imm16"           ],
0x93   :  [ 2, "subd", "direct"          ],
0xa3   :  [ 2, "subd", "indexed"         ],
0xb3   :  [ 3, "subd", "extended"        ],
0x3f   :  [ 1, "swi",  "inherent"        ],
0x103f :  [ 2, "swi2", "inherent"        ],
0x113f :  [ 2, "swi3", "inherent"        ],
0x13   :  [ 1, "sync", "inherent"        ],
0x1f   :  [ 2, "tfr",  "r1,r2"           ],
0x4d   :  [ 1, "tsta", "inherent"        ],
0x5d   :  [ 1, "tstb", "inherent"        ],
0x0d   :  [ 2, "tst",  "direct"          ],
0x6d   :  [ 2, "tst",  "indexed"         ],
0x7d   :  [ 3, "tst",  "extended"        ],
0x24   :  [ 2, "bcc",  "rel8", pcr       ],
0x1024 :  [ 2, "lbcc", "rel16"           ],
0x25   :  [ 2, "bcs",  "rel8", pcr       ],
0x1025 :  [ 2, "lbcs", "rel16"           ],
0x27   :  [ 2, "beq",  "rel8", pcr       ],
0x1027 :  [ 2, "lbeq", "rel16"           ],
0x2c   :  [ 2, "bge",  "rel8", pcr       ],
0x102c :  [ 2, "lbge", "rel16"           ],
0x2e   :  [ 2, "bgt",  "rel8", pcr       ],
0x102e :  [ 2, "lbgt", "rel16"           ],
0x22   :  [ 2, "bhi",  "rel8", pcr       ],
0x1022 :  [ 2, "lbhi", "rel16"           ],
0x24   :  [ 2, "bhs",  "rel8", pcr       ],
0x1024 :  [ 2, "lbhs", "rel16"           ],
0x2f   :  [ 2, "ble",  "rel8", pcr       ],
0x102f :  [ 2, "lble", "rel16"           ],
0x25   :  [ 2, "blo",  "rel8", pcr       ],
0x1025 :  [ 2, "lblo", "rel16"           ],
0x23   :  [ 2, "bls",  "rel8", pcr       ],
0x1023 :  [ 2, "lbls", "rel16"           ],
0x2d   :  [ 2, "blt",  "rel8", pcr       ],
0x102d :  [ 2, "lblt", "rel16"           ],
0x2b   :  [ 2, "bmi",  "rel8", pcr       ],
0x102b :  [ 2, "lbmi", "rel16"           ],
0x26   :  [ 2, "bne",  "rel8", pcr       ],
0x1026 :  [ 4, "lbne", "rel16"           ],
0x2a   :  [ 2, "bpl",  "rel8", pcr       ],
0x102a :  [ 4, "lbpl", "rel16"           ],
0x20   :  [ 2, "bra",  "rel8", pcr       ],
0x16   :  [ 3, "lbra", "rel16"           ],
0x21   :  [ 2, "brn",  "rel8", pcr       ],
0x1021 :  [ 4, "lbrn", "rel16"           ],
0x8d   :  [ 2, "bsr",  "rel8", pcr       ],
0x17   :  [ 3, "lbsr", "rel16"           ],
0x28   :  [ 2, "bvc",  "rel8", pcr       ],
0x1028 :  [ 4, "lbvc", "rel16"           ],
0x29   :  [ 2, "bvs",  "rel8", pcr       ],
0x1029 :  [ 4, "lbvs", "rel16"           ],

}

# End of processor specific code
##########################################################################