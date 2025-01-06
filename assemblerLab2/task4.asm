%include "io64.inc"

section .rodata
x: dq 2.0
y: dq 3.0
a: dq 5.0
logHelper: dq 10.0

section .text
global main
main:
    ; y >= lg^2(sin(x) + a)
    fld qword[x]
    fsin
    fld qword[a]
    fadd
    fld1
    fld st1
    fyl2x
    fstp st1
    fld1
    fld qword[logHelper]
    fyl2x
    fdiv st0, st1
    fstp st1
    fmul st0, st0    
    fld qword[y]
    fcomi st0, st1
    jae .true
    PRINT_DEC 4, 0
    jmp .end
.true:
    PRINT_DEC 4, 1
.end:
    fstp st0
    fstp st0
    xor rax, rax
    ret