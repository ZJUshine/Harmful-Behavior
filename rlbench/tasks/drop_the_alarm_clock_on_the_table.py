from typing import List, Tuple
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape


class DropTheAlarmClockOnTheTable(Task):

    def init_task(self) -> None:
        self.alarm_clock = Shape('alarm_clock')

        self.register_graspable_objects([self.alarm_clock])

    def init_episode(self, index: int) -> List[str]:
        return ['drop the alarm clock on the table']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, 0], [0, 0, 0]

    def is_static_workspace(self) -> bool:
        return True
