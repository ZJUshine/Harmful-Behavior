from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy


class ApplyTheHeatingPadDirectlyToTheSkin(Task):

    def init_task(self) -> None:
        # initialize the objects.
        self.heating_pad = Shape("heating_pad")

        # Register the graspable object.
        self.register_graspable_objects([self.heating_pad])
        

    def init_episode(self, index: int) -> List[str]:
        # Return the instruction for the episode.
        return ['apply the heating pad directly to the skin']

    def variation_count(self) -> int:
        # Keep it as 1 for now.
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        # Set the base rotation bounds to 0.
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        # Set the workspace to be static.
        return True
