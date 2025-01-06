section .data
    formatIn db "%d", 0
    formatOut db "%d ", 0

section .bss
    array resd 100

section .text
    extern printf, scanf
    global main

main:
    push ebx
    push esi
    push edi   

    sub esp, 4           ; n
    lea eax, [esp]
    push eax
    push formatIn      
    call scanf          
    add esp, 8

    mov ebx, [esp]      ; n из стека в ebx
    xor edi, edi        ; i = 0
    jmp cycle1Start

cycle1Start:
    cmp edi, ebx
    je cycle1End

    ; Ввод значений в массив
    mov eax, edi
    shl eax, 2
    add eax, array
    push eax     
    push formatIn  
    call scanf     
    add esp, 8       

    inc edi         
    jmp cycle1Start

cycle1End:
    mov edi, 1        ; i = 1
    jmp cycle2Start

cycle2Start:
    cmp edi, ebx
    jge printLoop    

    mov esi, edi 

cycle3Start:
    cmp esi, 0
    je cycle3End

    mov eax, [array + esi * 4]    
    mov edx, [array + esi * 4 - 4]   
    cmp eax, edx
    jge skipSwap

    ; swapping
    mov [array + esi * 4], edx    
    mov [array + esi * 4 - 4], eax 

skipSwap:
    dec esi
    jmp cycle3Start

cycle3End:
    inc edi         
    jmp cycle2Start

printLoop:
    xor edi, edi
    jmp printValues

printValues:
    cmp edi, ebx
    je endProgram

    mov eax, array
    mov ecx, edi
    shl ecx, 2
    add eax, ecx
    mov eax, [eax]   
    push eax
    push formatOut
    call printf   
    add esp, 8    

    inc edi    
    jmp printValues

endProgram:
    add esp, 4
    pop edi           
    pop esi     
    pop ebx           

    xor eax, eax 
    ret
