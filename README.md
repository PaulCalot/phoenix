# Introduction
Build game Shoot 'em up-like where your spacecraft is controlled by an AI that you trained yourself.

## Stack
- Python for MVP
- C later on
- C++ later on

## Architecture
- AI Engine : handles the agent
- Simulation Engine : handles mobs and game logic
- Rendering Engine : visualisation, for playing (when I play the agent) and debugging
In addition, I should need a human-player engine, that does the tricks between the command I input and the simulation engine.

### Simulation Engine
Keep it simple and efficient.

Responsibilities :
- Keep state of the simulation
- Handle agent input
- Handle mobs generation and logic
- Keep thing physical

Implementation :
* For performance reason, I will go with the "object of arrays" representation.
* Physics is implemented here (projectiles have a speed for instance)

The visualisation will handle the realistic display such that it does not depend on the framerate.

The simulation is developped as a package.

## Communication
RTS : real time system
GO server, nvim client
no websocket, no http => tcp connection entre les 2
Partial frame ? (update uniquement)
=> je me dois de faire les tests aussi que ce soit propre ! 

Intéressant pour comprendre les sockets : [ici, python](https://docs.python.org/2/howto/sockets.html)
Ce que je souhaite en réalité :
IPC socket (inter-process communication socket)

Question : comment faire cela au mieux ? 2 choix.
- soit je le fais en local, avec mémoire partagée, mais plus compliqué, moins intéressant
- soit je le fais via socket en bindant sur localhost dans un premier temps au moins => avec des sockets, c'est ce que je vais faire.

A voir comment je peux faire pour assurer que c'est bien le même processus qui reçoit et plot tout ce qu'il faut.
