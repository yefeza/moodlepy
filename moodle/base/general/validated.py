from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class GeneralValidated:
    """GeneralValidated
    Args:
        validated (int): True or False, nor 1 or 0
        warnings (List[Warning]): list of warnings
    """
    validated: int
    warnings: List[MoodleWarning] = fields(MoodleWarning)

    def __bool__(self) -> bool:
        if isinstance(self.validated, int):
            return self.validated == 1
        elif isinstance(self.validated, str):
            return self.validated == '1' or self.validated == 'true'
        return bool(self.validated)
