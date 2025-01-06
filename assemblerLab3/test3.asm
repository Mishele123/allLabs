section .data
    formatIn db "%d", 0
    formatOut db "%d ", 0

section .bss
    array resq 100
section .text
    extern printf, scanf
    global main

main: ; 8
    push r13 ; 0
    push rbx ; 8
    push r14 ; 0
    push r15 ; 8

    push rbp ; 0
    mov rbp, rsp
    sub rsp, 32

    lea rdx, [rsp] ; для хранения n
    lea rcx, [formatIn]
    call scanf

    mov rbx, [rsp]  ; n в rbx
    xor r13, r13
    jmp cycle1Start

cycle1Start:
    cmp r13, rbx
    je cycle1End

    lea rdx, [array + r13*8]
    lea rcx, [formatIn]
    call scanf
    add r13, 1
    jmp cycle1Start

cycle1End:
    mov r13, 1
    jmp cycle2Start

cycle2Start:
    cmp r13, rbx
    je cycle2End

    mov r14, r13

cycle3Start:
    cmp r14, 0
    je cycle3End

    mov rdx, [array + r14 * 8]
    mov r15, [array + r14 * 8 - 8]
    cmp rdx, r15
    jae skipSwap

    ; swapping
    mov [array + r14 * 8], r15
    mov [array + r14 * 8 - 8], rdx
    
skipSwap:
    dec r14
    jmp cycle3Start

cycle3End:
    add r13, 1
    jmp cycle2Start

cycle2End:
    xor r13, r13
    jmp printLoop

printLoop:
    cmp r13, rbx
    je endProgram
    
    lea rcx, [formatOut]
    mov rdx, [array + r13*8]
    call printf

    add r13, 1
    jmp printLoop
    
endProgram:
    mov rsp, rbp
    pop rbp
    pop r15
    pop r14
    pop rbx
    pop r13
    
    xor rax, rax
    ret
