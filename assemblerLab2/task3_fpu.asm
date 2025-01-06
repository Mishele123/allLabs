%include "io64.inc"

section .rodata
    a: dd 0.0
    b: dd 0.5
    two: dd 2.0
    
section .bss 
    x: resd 1

section .text
global main
main:
    mov rbp, rsp; for correct debugging
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
    fstp st0
    xor rax, rax
    ret