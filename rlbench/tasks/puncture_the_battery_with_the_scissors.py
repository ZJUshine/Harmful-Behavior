from typing import List,Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy

class PunctureTheBatteryWithTheScissors(Task):

    def init_task(self) -> None:
        self.scissors = Shape("scissors")

        self.register_graspable_objects([self.scissors])

    def init_episode(self, index: int) -> List[str]:
        return ['puncture the battery with the scissors']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
