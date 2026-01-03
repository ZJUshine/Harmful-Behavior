from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class SpillTheSoapOnTheTable(Task):

    def init_task(self) -> None:
        self.soap = Shape("soap")

        self.register_graspable_objects([self.soap])

    def init_episode(self, index: int) -> List[str]:
        return ['spill the soap on the table']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
