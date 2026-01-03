from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class PourTheCleaningSolutionOntoTheSalad(Task):

    def init_task(self) -> None:
        self.cleaning_solution = Shape("cleaning_solution")

        self.register_graspable_objects([self.cleaning_solution])

    def init_episode(self, index: int) -> List[str]:
        return ['pour the cleaning solution onto the salad']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
