from typing import Tuple, List, Union, Any

from . import (
    Hamming as Hamming,
    Indel as Indel,
    Jaro as Jaro,
    JaroWinkler as JaroWinkler,
    Levenshtein as Levenshtein,
    LCSseq as LCSseq,
)

_AnyOpList = Union[
    List[Union[Editop, Tuple[str, int, int]]],
    List[Union[Opcode, Tuple[str, int, int, int, int]]],
]

class Editop:
    tag: str
    src_pos: int
    dest_pos: int

    def __init__(self, tag: str, src_pos: int, dest_pos: int) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, i: int) -> Union[str, int]: ...
    def __repr__(self) -> str: ...

class Editops:
    def __init__(
        self, editops: _AnyOpList = None, src_len: int = 0, dest_len: int = 0
    ) -> None: ...
    @classmethod
    def from_opcodes(cls, opcodes: Opcodes) -> Editops: ...
    def as_opcodes(self) -> Opcodes: ...
    def as_list(self) -> List[Tuple[str, int, int]]: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def copy(self) -> Editops: ...
    def inverse(self) -> Editops: ...
    @property
    def src_len(self) -> int: ...
    @src_len.setter
    def src_len(self, value: int) -> None: ...
    @property
    def dest_len(self) -> int: ...
    @dest_len.setter
    def dest_len(self, value: int) -> None: ...
    def __getitem__(self, key: int) -> Editop: ...
    def __repr__(self) -> str: ...

class Opcode:
    tag: str
    src_start: int
    src_end: int
    dest_start: int
    dest_end: int

    def __init__(
        self, tag: str, src_start: int, src_end: int, dest_start: int, dest_end: int
    ) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, i: int) -> Union[str, int]: ...
    def __repr__(self) -> str: ...

class Opcodes:
    def __init__(
        self, opcodes: _AnyOpList = None, src_len: int = 0, dest_len: int = 0
    ) -> None: ...
    @classmethod
    def from_editops(cls, editops: Editops) -> Opcodes: ...
    def as_editops(self) -> Editops: ...
    def as_list(self) -> List[Tuple[str, int, int, int, int]]: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def copy(self) -> Opcodes: ...
    def inverse(self) -> Opcodes: ...
    @property
    def src_len(self) -> int: ...
    @src_len.setter
    def src_len(self, value: int) -> None: ...
    @property
    def dest_len(self) -> int: ...
    @dest_len.setter
    def dest_len(self, value: int) -> None: ...
    def __getitem__(self, key: int) -> Opcode: ...
    def __repr__(self) -> str: ...

class ScoreAlignment:
    score: Union[int, float]
    src_start: int
    src_end: int
    dest_start: int
    dest_end: int

    def __init__(
        self,
        score: Union[int, float],
        src_start: int,
        src_end: int,
        dest_start: int,
        dest_end: int,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, i: int) -> Union[int, float]: ...
    def __repr__(self) -> str: ...