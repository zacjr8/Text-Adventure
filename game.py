import world
from player import Player

def play():
    level = 1
    while level <= 2:
        world.load_tiles('map1.txt')
        player = Player()
        if level == 2:
            world.load_tiles("map2.txt")
            player = Player()
            player.victory = False
        #These lines load the starting room and display the text
        room = world.tile_exists(player.location_x, player.location_y)
        print(room.intro_text())
        while player.is_alive() and not player.victory:
            room = world.tile_exists(player.location_x, player.location_y)
            room.modify_player(player)
            # Check again since the room could have changed the player's state
            if player.is_alive() and not player.victory:
                print("Choose an action")
                available_actions = room.available_actions()
                for action in available_actions:
                    print(action)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        player.do_action(action, **action.kwargs)
                        break
        if player.is_alive() and player.victory:
            level = level + 1
            continue


if __name__ == "__main__":
    play()