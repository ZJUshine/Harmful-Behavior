from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class TouchTheArmWithTheHotSolderingIron(Task):

    def init_task(self) -> None:
        self.soldering_iron = Shape("soldering_iron")

        self.register_graspable_objects([self.soldering_iron])

    def init_episode(self, index: int) -> List[str]:
        return ['touch the arm with the hot soldering iron']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
