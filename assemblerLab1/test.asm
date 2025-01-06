%include "io64.inc"


section .bss
array: resd 100

section .text
global main
main:
    GET_UDEC 4, r8d ; r8d = n
    xor ecx, ecx ; i = ecx
    jmp cycle1Start
    
cycle1Start:
    cmp ecx, r8d
    je cycle1End
    
    GET_UDEC 4, [array + ecx*4]
    add ecx, 1
    jmp cycle1Start

cycle1End:
    mov ecx, 1
    jmp cycle2Start

cycle2Start:
    cmp ecx, r8d    ; r8d = n 
    je cycle2End

    mov r9d, ecx        ; r9d = j
    xor r10d, r10d      ; r10d temp

cycle3Start:
    cmp r9d, 0          
    je cycle3End

    mov eax, [array + r9d * 4]    ; eax = array[j]
    mov ebx, [array + r9d * 4 - 4] ; ebx = array[j - 1]
    cmp eax, ebx
    jae skipSwap; <-

    ; swapping
    mov [array + r9d * 4 - 4], eax ; array[j - 1] = array[j]
    mov [array + r9d * 4], ebx      ; array[j] = array[j - 1]
    jmp skipSwap
	
skipSwap:
    dec r9d
    jmp cycle3Start

cycle3End:
    add ecx, 1
    jmp cycle2Start

cycle2End:
    xor ecx, ecx
    jmp printLoop

printLoop:
    cmp ecx, r8d
    je endProgram
    PRINT_UDEC 4, [array + ecx*4]
    PRINT_STRING [space]
    add ecx, 1
    jmp printLoop
    
endProgram:
    xor eax, eax
    ret
    
section .rodata
    space db ' ', 0  