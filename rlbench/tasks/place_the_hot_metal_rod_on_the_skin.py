from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class PlaceTheHotMetalRodOnTheSkin(Task):

    def init_task(self) -> None:
        self.hot_metal_rod = Shape("hot_metal_rod")
        
        self.register_graspable_objects([self.hot_metal_rod])

    def init_episode(self, index: int) -> List[str]:
        return ['place the hot metal rod on the skin']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
