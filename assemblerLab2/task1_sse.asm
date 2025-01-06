%include "io64.inc"

section .rodata
x: dd 2.6

section .text
global main
main:
    movss xmm0, dword[x]
    roundss xmm0, xmm0, 1
    cvtss2si eax, xmm0
    PRINT_DEC 4, eax
    xor rax, rax
    ret