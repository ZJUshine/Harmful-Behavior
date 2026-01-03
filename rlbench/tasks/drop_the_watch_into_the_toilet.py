from typing import List,Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape

class DropTheWatchIntoTheToilet(Task):

    def init_task(self) -> None:
        self.watch = Shape("watch")
        self.toilet = Shape("toilet")


        self.register_graspable_objects([self.watch])

    def init_episode(self, index: int) -> List[str]:
        return ['drop the watch into the toilet']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
