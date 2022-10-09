import requests
import time

class Pokemon:

    def __init__(self, pk_name: str) -> None:
        self.name = pk_name
        PokemonObject = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pk_name.lower()}')
        self.PokemonJson = PokemonObject.json()

    def moves(self, index: int):
        # for MoveObject in self.PokemonJson['moves']:
        MoveObject = self.PokemonJson['moves'][index]
        move_url = MoveObject['move']['url']
        # Data about a specific move
        move_data = requests.get(move_url).json()
        time.sleep(0.2)
        for data in move_data["flavor_text_entries"]:
            if data["language"]["name"] == "en":
                desc = data["flavor_text"]
                break
        return {  # return dictionary of name,description,accuracy,demg_stats
            'name': MoveObject['move']['name'],
            'description': str(desc).replace("\n", " ").capitalize(),
            'accuracy': move_data['accuracy'],
            'dmg_type': move_data['damage_class']['name'],

        }

    def len_moves(self):
        no_moves = len(self.PokemonJson['moves'])
        return no_moves

    def types(self):
        type = []
        for slot in self.PokemonJson['types']:
            type.append(slot["type"]["name"].title())
        time.sleep(0.2)
        return type  # return types in that pokemon

    def stats(self):
        stat = []
        for statis in self.PokemonJson['stats']:
            stat.append((statis['stat']['name'], statis['base_stat']))
        # return dictionary of stats namne and it s statistics
        time.sleep(0.2)
        return(dict(stat))

    def ability(self):
        abilities = []
        for abi in self.PokemonJson['abilities']:
            abilities.append(abi["ability"]["name"].title())
        time.sleep(0.2)
        return abilities  # return the abilities of pokemon

    def game_version(self):
        for version in self.PokemonJson['game_indices']:
            if(version['version']['name'] == "diamond" or version['version']['name'] == 'black'):
                index = version["game_index"]
        return index


x = Pokemon('pikachu')
print(type(x.game_version()))
