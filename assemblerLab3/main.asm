section .rodata 
    message: db "Hello world!", 0
 
section .text
extern printf
 
global main
main:
    sub rsp, 32+8
    lea rcx, [message]
    call printf
    add rsp, 32+8
    xor rax, rax
    ret