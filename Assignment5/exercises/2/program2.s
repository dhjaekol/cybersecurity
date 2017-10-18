	.file	"2.c"
	.section	.rodata
.LC0:
	.string	"record: %s\n"
	.text
	.globl	default_print_record
	.type	default_print_record, @function
default_print_record:
.LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$24, %esp
	movl	8(%ebp), %eax
	leal	32(%eax), %edx
	movl	$.LC0, %eax
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	printf
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	default_print_record, .-default_print_record
	.globl	newRecord
	.type	newRecord, @function
newRecord:
.LFB1:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%edi
	subl	$52, %esp
	movl	$0, -12(%ebp)
	movl	$168, (%esp)
	.cfi_offset 7, -12
	call	malloc
	movl	%eax, -12(%ebp)
	cmpl	$0, -12(%ebp)
	jne	.L3
	movl	$0, %eax
	jmp	.L4
.L3:
	movl	8(%ebp), %eax
	movl	$-1, -28(%ebp)
	movl	%eax, %edx
	movl	$0, %eax
	movl	-28(%ebp), %ecx
	movl	%edx, %edi
	repnz scasb
	movl	%ecx, %eax
	notl	%eax
	subl	$1, %eax
	cmpl	$31, %eax
	jbe	.L5
	movl	-12(%ebp), %eax
	movl	%eax, (%esp)
	call	free
	movl	$0, %eax
	jmp	.L4
.L5:
	movl	8(%ebp), %edx
	movl	-12(%ebp), %eax
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	strcpy
	movl	12(%ebp), %eax
	movl	$-1, -28(%ebp)
	movl	%eax, %edx
	movl	$0, %eax
	movl	-28(%ebp), %ecx
	movl	%edx, %edi
	repnz scasb
	movl	%ecx, %eax
	notl	%eax
	subl	$1, %eax
	movl	%eax, %edx
	movl	-12(%ebp), %eax
	movw	%dx, 164(%eax)
	movl	-12(%ebp), %eax
	movzwl	164(%eax), %eax
	cmpw	$127, %ax
	jbe	.L6
	movl	-12(%ebp), %eax
	movl	%eax, (%esp)
	call	free
	movl	$0, %eax
	jmp	.L4
.L6:
	movl	-12(%ebp), %eax
	movl	$default_print_record, 160(%eax)
	movl	12(%ebp), %eax
	movl	$-1, -28(%ebp)
	movl	%eax, %edx
	movl	$0, %eax
	movl	-28(%ebp), %ecx
	movl	%edx, %edi
	repnz scasb
	movl	%ecx, %eax
	notl	%eax
	leal	-1(%eax), %ecx
	movl	12(%ebp), %eax
	movl	-12(%ebp), %edx
	addl	$32, %edx
	movl	%ecx, 8(%esp)
	movl	%eax, 4(%esp)
	movl	%edx, (%esp)
	call	strncpy
	movl	-12(%ebp), %eax
.L4:
	addl	$52, %esp
	popl	%edi
	.cfi_restore 7
	popl	%ebp
	.cfi_def_cfa 4, 4
	.cfi_restore 5
	ret
	.cfi_endproc
.LFE1:
	.size	newRecord, .-newRecord
	.section	.rodata
.LC1:
	.string	"/bin/date"
.LC2:
	.string	"Program started at:"
	.text
	.globl	printDay
	.type	printDay, @function
printDay:
.LFB2:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	movl	$.LC1, -12(%ebp)
	movl	$.LC2, (%esp)
	call	puts
	movl	-12(%ebp), %eax
	movl	%eax, (%esp)
	call	system
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE2:
	.size	printDay, .-printDay
	.globl	main
	.type	main, @function
main:
.LFB3:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$32, %esp
	cmpl	$2, 8(%ebp)
	jg	.L9
	movl	$-1, %eax
	jmp	.L10
.L9:
	call	printDay
	movl	12(%ebp), %eax
	addl	$8, %eax
	movl	(%eax), %edx
	movl	12(%ebp), %eax
	addl	$4, %eax
	movl	(%eax), %eax
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	newRecord
	movl	%eax, 28(%esp)
	cmpl	$0, 28(%esp)
	je	.L11
	movl	28(%esp), %eax
	movl	160(%eax), %edx
	movl	28(%esp), %eax
	movl	%eax, (%esp)
	call	*%edx
.L11:
	movl	$0, %eax
.L10:
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE3:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits
