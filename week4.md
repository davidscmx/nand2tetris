

# Unit 4.2: Machine Language: Elements

- Machine language is the most important interface in the world.
- Machine language specifies exactly what the hardware can do for us. 

Cost-performane tradeoff
- The more sophisticated operations and types the more expensive the
hardware get.

## Machine Operations

- Flow control operation: when to jump inside a program
- Different machine langugages differ on what they offer.
- What data types can our hardware access? 8-bit vs. 64-bit numbers.
- Some machine languages can also support floating point operations.

## Addressing

How do we decide what data to work on? How does the hardware allows us
to do this?

- Accessing memory is an expensive operations in two ways:
  - Need to specify a long address
  - Gettings memory contents into the CPU takes a long time compares to the CPU
    operations

Solution: Memory Hierarchy.
Insert drawing

Memory Hierachy
- Registers
- Cache
- Main memory
- Disk

1. Registers
- All CPU contains few registers inside
- Getting information from them is extremely quickly
- Quick to address
- Central part of the machine language

Example:
Add R1, R2

Address register:
Store R1, @A

Addressing Modes: How dow we decide which data to work upon? How to tell
the CPU on which data to apply an operation say the add operation?

- Register
Add R1,R2

- Direct
Add R1, M[200]

- Indirect
Add R1, index

- Immediate
Add 73, R1

## Input/Output

- Many types of input and output
  Keyboard, mouse, camera, sensors...

CPU needs some protocol to talk to them -> drivers knows this protocols

One general methods to do this: memory mapping
Connect the registers that control the devices as a part of the memory.
Gives us access to input/output as if we were accesing the memory itself.

## Flow control
How can we tell the hardware which instrution to execute next.
Unconditional jumps: for loop
Conditional jumps: if statement
