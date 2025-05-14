mov @str, r0
mov 3f, r2
loop:
movb (r0), r1
cmpb 60, r1
jl locl
jge hifl
locl:
cmpb 7b, r1
jg msub
jle skip
hifl:
cmpb 40, r1
jl madd
jge skip
msub:
movb 03, (r2)
jmp exec
madd:
movb 02, (r2)
jmp exec
exec:
sub 20, r1
skip:
movb r1, (r0)
add 1, r0
cmpb 0,(r0)
jnz loop
stop
str:
data "aABayAga"
