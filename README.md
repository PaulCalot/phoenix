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
