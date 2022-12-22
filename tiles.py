import items, enemies, actions, world
import sounds
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Status())
        moves.append(actions.Equip())
        moves.append(actions.Heal())
 
        return moves


class EnterHogwarts(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        Welcome to Hogwarts School of Witchcraft and Wizardry.
        The school is fairly straightforward in layout, 
        with large rooms of regular size connected by wide corridors 
        but there are death eaters hiding around the corners!!!.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class Corridor(MapTile):
    def intro_text(self):
        return """
        Another wide corridor. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass


class Passage(MapTile):
    def intro_text(self):
        return """
        Crawl through the passage
        """

    def modify_player(self, player):
        # Room has no action on player
        pass
 
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            sounds.spider()
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.wolf()
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class NaginiRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Nagini())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.monster()
            return """
            Nagini the snake has appeared
            """
        else:
            return"""
        Nagini is dead
        """

class VoldemortRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Voldemort())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.zombie()
            return """
                Lord Voldemort is coming for you
            """
        else:
            return """
        Voldemort was exterminated!
        """
class ReaperRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Reaper())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.reaper()
            return """
                The murderous reaper is here!
            """
        else:
            return """
        Reaper was killed
        """

class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a sword of Gryffindor! You pick it up.
        """

class SmallPotionRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.SmallPotion())

    def intro_text(self):
        return """
        You have a found a small healing potion.
        """
    def modify_player(self, player):
        player.inventory.append(self.item)

class LeaveHogwarts(MapTile):
    def intro_text(self):
        return """
        A huge door welcomes you...
        Yes you have made it to the end
        Congratulations ...
        """
 
    def modify_player(self, player):
        player.victory = True


class EnterForbiddenForest(MapTile):
    def intro_text(self):
        return """
       This area is more difficult than Hogwarts.
        The Forbidden Forest are very dark, and the room layout is convoluted and confusing
        """

    def modify_player(self, player):
        player.victory = True

class LeaveForbiddenForest(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True

