section .data
one:     dq 1.0
neg_one: dq -1.0
x_value: dq 2.0

section .bss
result: resq 1


section .text
global main

main:
    movsd xmm1, qword[x_value]
    movaps xmm2, xmm1 ; ; xmm2 = x = pw
    mulsd xmm1, xmm1 ; xmm1 = xx = x^2
    movsd xmm3, qword[one]; xmm3 = fti
    ; xmm4 = result = 0
    movsd xmm5, qword[one] ; xmm5 = sign
    xor rax, rax ; rax = i
    inc rax

.loop:
    cmp rax, 25
    jg .end
    
    cvtsi2sd xmm9, rax ; xmm9 = i
    divsd xmm3, xmm9 ; fti /= i
    
    movaps xmm8, xmm2 ; xmm8 = pw
    mulsd xmm8, xmm3 ; xmm8 = pw * fti
    mulsd xmm8, xmm5 ; xmm8 = pw * fti * sign
    addsd xmm4, xmm8 ; result += xmm8
    
    mulsd xmm2, xmm1 ; pw *= x^2
    addsd xmm9, qword[one]             ; xmm9 = (i + 1)
    divsd xmm3, xmm9             ; fti /= (i + 1)
    mulsd xmm5, qword [neg_one]   ; sign = -sign
    add rax, 2
    
    jmp .loop
    
.end:
    movaps xmm0, xmm4
    movsd qword[result], xmm0
    fld qword[result]
    ret