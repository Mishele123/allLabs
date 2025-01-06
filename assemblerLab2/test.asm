section .data
x_value: dd 1.0

section .text
global main
main:
    movss xmm0, dword[x_value]
    movaps xmm1, xmm0
    mulss xmm1, xmm1
    movss xmm2, xmm0 ; pw
    movss xmm3, dword [one] ; sign
    movss xmm4, dword [one] ; fti
    xor rax, rax ; rax = i

.loop:
    cvtsi2ss xmm6, rax
    mulss xmm6, dword [two]
    addss xmm6, dword [one] ; i * 2 + 1

    movss xmm7, xmm4 ; fti
    divss xmm7, xmm6 ; fti / (i * 2 + 1)

    mulss xmm2, xmm3 ; pw * sign
    mulss xmm2, xmm4 ; pw * sign * fti
    addss xmm0, xmm2 ; result += (pw * sign * fti)

    movss xmm4, xmm7 ; fti / (i * 2 + 1)
    xorps xmm3, xmm3
    movss xmm3, xmm3 ; sign = -sign

    mulss xmm2, xmm1 ; pw *= x^2

    add rax, 2 ; i += 2

    cvtsi2ss xmm6, rax
    ucomiss xmm6, dword [limit] ; i < 25.0
    jae .end

    jmp .loop

.end:
    movss dword [result], xmm0

    fld dword [result]
    
    ret