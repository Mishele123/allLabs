%include "io64.inc"

section .rodata
a: dd 1.0
b: dd 0.3
two: dd 2.0
    
section .bss 
    x: resd 1

section .text
global main
main:
    ; x = arctg(2^b) - a
    fld dword[b]
    fld dword[two]
    fyl2x 
    fld1 
    fld st1 
    fprem 
    f2xm1 
    fadd
    fscale 
    fstp st1 
    fld1
    fpatan
    fld dword[a]
    fsub
    fstp dword[x]
    xor rax, rax
    ret