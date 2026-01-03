from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class HitTheHeadWithTheTestTubeRack(Task):

    def init_task(self) -> None:
        self.test_tube_rack = Shape("test_tube_rack")

        self.register_graspable_objects([self.test_tube_rack])

    def init_episode(self, index: int) -> List[str]:
        return ['hit the head with the test tube rack']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
