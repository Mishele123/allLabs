%include "io64.inc"



section .text
global main
main:
    ; sin ( pi / 6)
    fldpi
    fld1
    fld1
    fadd st0, st0
    fadd st0, st0
    fadd st0, st1
    fadd st0, st1
    
    fdiv st2, st0
    fstp st0
    fstp st0
    
    fsin ; sin(st0)
    fstp st0
    xor rax, rax
    ret