from dataclasses import dataclass, field

@dataclass
class GobFile():
    first_value: int = field(repr=False)
    file_size: int
    file_path: str
    file_data: bytes = field(init=False, repr=False)