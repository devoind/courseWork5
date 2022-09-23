from dataclasses import dataclass
from skills import *


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=100,
    max_stamina=30,
    attack=1,
    stamina=1,
    armor=3,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1,
    skill=HardShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
