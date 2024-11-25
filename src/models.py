"""File that contains all the models (classes) for this project"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Student:
    ref: int = field(repr=False)
    name: str 
    level: int
    birthday_date: Optional[datetime] = field(repr=False)

    def __post_init__(self):
        pass

    def _get_dictionary(self):
        return {
            'ref': self.ref,
            'name': self.name,
            'level': self.level,
            'birthday_date': self.birthday_date
        }

@dataclass
class Class:
    ref: int = field(repr=False)
    level: int
    day_date: str 
    start_time: str
    end_time: str = field(repr=False)

    def __post_init__(self):
        pass

    def _get_dictionary(self):
        return {
            'ref': self.ref,
            'level': self.level,
            'day_date': self.day_date,
            'start_time': self.start_time,
            'end_time': self.end_time
        }