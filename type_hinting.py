# Type hinting is a feature in Python that help to write clean code.

def greeting(name: str) -> str:
    return 'Hello ' + name

from typing import List
x : List[List[int]] = [[23,53], [18, 62]]

from typing import Dict
y : Dict[str, str] = {"a": "b"}

# Creating Custom Types:
OurCustomType_1 = List[float]
OurCustomType_2 = List[OurCustomType_1]

# Type Alieasing:
Float64 = float
