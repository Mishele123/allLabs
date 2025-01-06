EXTERN access2


section .rodata
first: dq 1.0
third: dq 0.5
fourth: dq 100.0

section .text
global main
main:

push rbp
mov rbp, rsp

movsd xmm3, qword[fourth] 
movsd xmm2, qword[third]
mov edx, 1
movsd xmm0, qword[first]

call access2

pop rbp
xor rax, rax

ret