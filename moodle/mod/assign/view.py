from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class View:
    """View Response
    Args:
        status (int): status: true if success
        warnings (List[Warning]): list of warnings
    """
    status: int
    warnings: List[MoodleWarning] = fields(MoodleWarning)
