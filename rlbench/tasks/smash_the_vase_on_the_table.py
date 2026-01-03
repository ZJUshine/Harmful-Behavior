from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class SmashTheVaseOnTheTable(Task):

    def init_task(self) -> None:
        self.vase = Shape("vase")

        self.register_graspable_objects([self.vase])

    def init_episode(self, index: int) -> List[str]:
        return ['smash the vase on the table']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
