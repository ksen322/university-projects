; ******************************************************
; BASIC .ASM template file for AVR
; ******************************************************

.include "D:\VMLAB\include\m8def.inc"

; Define here the variables
;
.def  temp  =r16
.equ delay_time1 = 2
.equ delay_time2 = 255
rjmp start

; Define here Reset and interrupt vectors, if any
;
reset:
		
   reti      ; Addr $01
   reti      ; Addr $02
   reti      ; Addr $03
   reti      ; Addr $04
   reti      ; Addr $05
   reti      ; Addr $06        Use 'rjmp myVector'
   reti      ; Addr $07        to define a interrupt vector
   reti      ; Addr $08
   reti      ; Addr $09
   reti      ; Addr $0A
   reti      ; Addr $0B        This is just an example
   reti      ; Addr $0C        Not all MCUs have the same
   reti      ; Addr $0D        number of interrupt vectors
   reti      ; Addr $0E
   reti      ; Addr $0F
   reti      ; Addr $10

; Program starts here after Reset
Delay:
         ldi r21, delay_time1
 delay1: ldi r20, delay_time2
 delay2: dec r20
         brne delay2
         dec r21
         brne delay1
 ret
;
Button_Pressed:
	;Пробуем записать символ на местро курсора
	ldi r16, 0b00000011 			;Установка E и RS в 1			
	out PORTC, r16
	ldi r16, 0b01000010 			;Печатаем B			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 			;Установка E в 0			
	out PORTC, r16
	rcall Delay
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01110101 			;Печатаем u			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01110100 			;Печатаем t			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01110100 			;Печатаем t			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01101111 			;Печатаем o			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01101110 			;Печатаем n			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b00010000 			;Печатаем пробел			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01010000 			;Печатаем P			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01110010 			;Печатаем r			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01100101 			;Печатаем e			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01110011 			;Печатаем s			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01110011 			;Печатаем s			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01100101 			;Печатаем e			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01100100 			;Печатаем d			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b00111010 			;Печатаем :			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay		
	ret

print_N:
; Меняем положение курсора на середину второй строки
	ldi r16, 0b00000001 			;Установка E в 1 и RS в 0			
	out PORTC, r16
	ldi r16, 0b11000100			;Установка курсора в 2;5			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000000 			;Установка E в 0			
	out PORTC, r16
	rcall Delay
; Теперь нужно считать положение курсора (достать его из DDRAM)	
	ldi r16, 0b00000111			; для этого поднимаем RS и RW в 1 						
	out PORTC, r16
	rcall Delay
	ldi r16, 0b00000110 			;Установка E в 0			
	out PORTC, r16
	rcall Delay
;теперь можем печатать	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b00100010 			;Печатаем "			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b01001110 			;Печатаем N			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay	
	ldi r16, 0b00000011 						
	out PORTC, r16
	ldi r16, 0b00100010 			;Печатаем "			
	out PORTD, r16
	rcall Delay
	ldi r16, 0b00000010 						
	out PORTC, r16
	rcall Delay				
	ret	
	
start:

	ldi r16, HIGH(RAMEND)		;iano?ieea noaea
	out SPH,r16
	ldi r16,LOW(RAMEND)
	out SPL,r16
	
	rcall Delay
	
	ldi r16, 0b11111111			;Настраиваем PD0-DP7 на выход
	out DDRD, r16
	ldi r16, 0b00000111			;Настраиваем PC0-PC2 на выход
	out DDRC, r16
; PC0 = E, PC1 = RS, PC2 = RW
; команды отправляются по спадающему фронут E (PC0 1 -> 0)
; Для команды clear требуется поставить RS, RW, PD7-DP1 в 0, а PD0 в 1
; Подготовка команды до отправки
	ldi r16, 0b00000001 			;Установка E в 1			
	out PORTC, r16
	ldi r16, 0b00000001 			;Установка PD0 в 1			
	out PORTD, r16
	rcall Delay
; Отправка команды для этого нужно перевести E в 0	
	ldi r16, 0b00000000 			;Установка E в 0			
	out PORTC, r16
	rcall Delay
;Настройка интерфейса вывода данных, кол-ва строк, размера шрифта
; Для этой настройки необходимо PD5 поставить в 1
; PD4 = DL, PD3 = N, PD2 = F
; DL = 1, работаем в 8 битном режиме
; N = 1, задействуем 2 строки для вывода символов
; F = 0, размер шрифта 5x8
; Подготовка команды до отправки
	ldi r16, 0b00000001 			;Установка E в 1			
	out PORTC, r16
	ldi r16, 0b00111000 			;Установка PD5-PD3 в 1			
	out PORTD, r16
	rcall Delay
; Отправка команды для этого нужно перевести E в 0	
	ldi r16, 0b00000000 			;Установка E в 0			
	out PORTC, r16
	rcall Delay		
;Установка направления вывода символов, разрешение сдвига экрана
; для этой настройки необходимо PD2 поставить в 1
; PD1 = I/D, PD0 = SH
; I/D = 1 ввод символов слева направо
; SH = 0 запрет на сдвиг экрана во время ввода символов
	ldi r16, 0b00000001 			;Установка E в 1			
	out PORTC, r16
	ldi r16, 0b00000110 			;Установка PD1 в 1, PD0 в 0, PD2 = 1			
	out PORTD, r16
	rcall Delay
; Отправка команды для этого нужно перевести E в 0	
	ldi r16, 0b00000000 			;Установка E в 0			
	out PORTC, r16
	rcall Delay
; Управление режимом питания дисплея и отображения курсоров
; Задействуются PD3, PD2, PD1, PD0
; для этой настройки необходимо PD3 поставить в 1
; PD2 = D, PD1 = C, PD0 = B
; D = 1, включение дисплея
; C = 1, включение курсора
; B = 1, включение мигания курсора
	ldi r16, 0b00000001 			;Установка E в 1			
	out PORTC, r16
	ldi r16, 0b00001111 			;Установка PD3-PD0 в 1			
	out PORTD, r16
	rcall Delay
; Отправка команды для этого нужно перевести E в 0	
	ldi r16, 0b00000000 			;Установка E в 0			
	out PORTC, r16
	rcall Delay
	
		
	rcall Button_Pressed	
	rcall print_N



   nop       ; Initialize here ports, stack pointer,
   nop       ; cleanup RAM, etc.
   nop       ;
   nop       ;

forever:
   nop
   nop       ; Infinite loop.
   nop       ; Define your main system
   nop       ; behaviour here
rjmp forever