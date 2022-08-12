# How it works

Well, this is simple.

Aiogram_declarative provides 3 objects:
1) Custom Router - inherited from basic aiogram Router, 
but able to "delay" initial operations
2) The Joint - class which groups handlers and other stuff
3) The Registry - main class in the scheme.
This is a builder of Joints.

Refer to the documentation files