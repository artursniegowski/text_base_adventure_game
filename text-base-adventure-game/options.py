from objects import ObjectBase
from objects import Goblin

def say(action : str) -> str:
    """defining first posible action"""
    return 'You said {}'.format(action)

def inspect(object : str) -> str:
    """looking if the object was defined"""
    if object in ObjectBase.objects:
        return ObjectBase.objects[object].get_description()
    else:
        return "{} dosent exists in this game".format(object)

def hit(object : str) -> str:
    """method used for atacking creatures"""
    if object in ObjectBase.objects:
        creature = ObjectBase.objects[object]
        if creature.class_name == "goblin":
            creature.health -= 1
            if creature.health == 0:
                msg = "You killed the goblin !"
            elif creature.health < 0:
                msg = "It is long dead !!"
            else:
                msg = "You hit the {}".format(creature.class_name)
    else:
        msg = "There is no {} here".format(object)
    return msg

action_dictionary = {
    'say':say,
    'inspect':inspect,
    'hit':hit,
}