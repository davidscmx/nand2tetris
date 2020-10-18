// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// screen: 16384 + 8191
// Listening to keyboard input
(LOOP)
@i
M=0
@24576
D = M
@BLACKLOOP
D;JNE
@BLANKLOOP
D;JEQ

(BLACKLOOP)
@i
D=M
@8191
D=D-A
@LOOP
D;JGT // If (i-8191)=0 goto END
@SCREEN
D = A
@i
A = D+M
M = -1
@i
M = M+1
@BLACKLOOP
0;JMP

(BLANKLOOP)
@i
D=M
@8191
D=D-A
@LOOP
D;JGT // If (i-8191)=0 goto END
@SCREEN
D = A
@i
A = D+M
M = 0
@i
M = M+1
@BLANKLOOP
0;JMP

@24576 // Reset keyboard value
M = 0

@LOOP
0;JMP
