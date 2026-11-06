# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 17:07:34 2025

@author: castelf

with the use of ChatGPT
"""

from __future__ import annotations # permet de reporter l'évaluation des annotations de type
from dataclasses import dataclass, field
from collections import deque
from typing import Dict, List, Tuple, Iterable

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day15.txt','r') as f: input_arena=f.read()

#Umatrix = [list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day15.txt').readlines()]

@dataclass
class Creature:
    """Un elfe ou un gobelin qui vit sur la grille."""
    kind: str                     # "E" pour elfe, "G" pour gobelin
    pos: Tuple[int, int]          # (x, y) – x = colonne, y = ligne
    weapon: int                   # puissance d'attaque en plus pour les elfes
    hp: int = 200                 # points de vie de base (peut être personnalisé)
    arena: "Arena" = field(repr=False, compare=False, init=False)   # référence vers la carte
    
    def __post_init__(self) -> None:
        assert self.kind in {"E", "G"}, "kind doit être 'E' ou 'G'"
        self.attack = 3
        if self.kind == 'E':
            self.attack += self.weapon
    
    @property
    def is_elf(self) -> bool:
        return self.kind == "E"

    @property
    def is_goblin(self) -> bool:
        return self.kind == "G"
    
    # ------------------------------------------------------------------
    # Méthodes utilitaires
    # ------------------------------------------------------------------
    def adjacent_positions(self) -> List[Tuple[int, int]]:
        """Retourne les 4 cases voisines dans l'ordre lecture‑ligne (top‑left‑right‑bottom)."""
        x, y = self.pos
        return [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]

    def move_to(self, new_pos: Tuple[int, int]) -> None:
        """Déplace la créature en mettant à jour l'arène."""
        self.arena._move_creature(self, new_pos)

    def attack_target(self, target: Creature) -> None:
        """Inflige des dégâts au cible et la retire de l'arène si elle meurt."""
        target.hp -= self.attack
        self.arena._updating_score(self, self.attack)
        if target.hp <= 0:
            self.arena._remove_creature(target)
            self.arena._updating_score(self, target.hp)

    # ------------------------------------------------------------------
    # Représentation lisible pour le debug
    # ------------------------------------------------------------------
    def __repr__(self) -> str:
        return f"<{self.kind} hp={self.hp} pos={self.pos}>"

class Arena:
    """
    Représente le plateau de jeu.
    - `grid`  : liste de listes de caractères ('.', '#', ou espaces vides)
    - `creatures` : liste ordonnée de toutes les créatures (pour respecter l'ordre de lecture)
    - `pos2creature` : dictionnaire {(x, y): Creature}
    """

    def __init__(self, raw_map: str, elf_weapon: int) -> None:
        self.elf_weapon = elf_weapon             # arme en plus pour les elfes
        self.grid: List[List[str]] = []          # mur = '#', sol = '.'
        self.creatures: List[Creature] = []      # ordre de lecture (top‑left → bottom‑right)
        self.pos2creature: Dict[Tuple[int, int], Creature] = {}
        self.score: Dict = {'E': 0, 'G': 0}

        self._parse(raw_map)

    # ------------------------------------------------------------------
    # Lecture et construction initiale
    # ------------------------------------------------------------------
    def _parse(self, raw_map: str) -> None:
        """
        Parcourt le texte ligne par ligne, crée les créatures et remplit le tableau.
        Exemple d’entrée :
            "####\n#E.G#\n####"
        """
        for y, line in enumerate(raw_map.splitlines()):
            row = []
            for x, ch in enumerate(line.rstrip("\n")):
                if ch in "EG":                     # une créature se trouve ici
                    creature = Creature(kind=ch, pos=(x, y), weapon=self.elf_weapon)
                    # On indique à la créature à quel arena elle appartient
                    creature.arena = self
                    self.creatures.append(creature)
                    self.pos2creature[(x, y)] = creature
                    row.append('.')                # la case sous‑jacente est du sol
                else:
                    row.append(ch)                # '#', '.' ou autre
            self.grid.append(row)

    # ------------------------------------------------------------------
    # Accès au terrain
    # ------------------------------------------------------------------

    def is_wall(self, pos: Tuple[int, int]) -> bool:
        return self.grid[pos[1]][pos[0]] == "#"

    def is_free(self, pos: Tuple[int, int]) -> bool:
        """Libre = pas de mur et pas de créature."""
        return not self.is_wall(pos) and pos not in self.pos2creature

    # ------------------------------------------------------------------
    # Manipulation du dictionnaire central
    # ------------------------------------------------------------------
    
    def _move_creature(self, creature: Creature, new_pos: Tuple[int, int]) -> None:
        """Met à jour `pos2creature` lorsqu’une créature se déplace."""
        if not self.is_free(new_pos):
            raise ValueError(f"Case {new_pos} n’est pas libre")
        # supprimer l’ancienne entrée
        del self.pos2creature[creature.pos]
        # mettre à jour la position interne de l’objet
        creature.pos = new_pos
        # ajouter la nouvelle entrée
        self.pos2creature[new_pos] = creature

    def _remove_creature(self, creature: Creature) -> None:
        """Supprime la créature du plateau (mort)."""
        # retirer du dict
        self.pos2creature.pop(creature.pos, None)
        # retirer de la liste principale (on garde l’ordre de lecture en filtrant)
        self.creatures = [c for c in self.creatures if c is not creature]

    # ------------------------------------------------------------------
    # Manipulation du score de chaque sorte de créatures
    # ------------------------------------------------------------------
    def _updating_score(self, creature: Creature, damage: int) -> None:
        """Modifie le score de l'équipe de la créature en ajoutant le nombre de dégats à l'équipe adverse."""
        self.score[creature.kind] += damage

    # ------------------------------------------------------------------
    # Extraits utiles pour le combat (facultatif)
    # ------------------------------------------------------------------
    def living_creatures(self) -> List[Creature]:
        """Renvoie les créatures encore vivantes, triées dans l’ordre de lecture."""
        return sorted(self.creatures, key=lambda c: (c.pos[1], c.pos[0]))

    def enemies_of(self, creature: Creature) -> Iterable[Creature]:
        """Tous les ennemis (elfes ↔ gobelins)."""
        target_kind = "G" if creature.is_elf else "E"
        return (c for c in self.creatures if c.kind == target_kind)

    # ------------------------------------------------------------------
    # Visualisation du plateau (debug / aide à la résolution)
    # ------------------------------------------------------------------
    def render(self) -> str:
        """Retourne une représentation texte de la carte avec les créatures."""
        lines = []
        for y, row in enumerate(self.grid):
            line = ""
            hp_infos = []
            for x, cell in enumerate(row):
                if (x, y) in self.pos2creature:
                    creature = self.pos2creature[(x, y)]
                    line += creature.kind
                    hp_infos.append(f"{creature.kind}({creature.hp})")
                else:
                    line += cell
            lines.append(f"{line}   {' '.join(hp_infos)}")
        return "\n".join(lines)


def bfs_shortest_path(start: Tuple[int,int], goals: List[Tuple[int,int]], arena: Arena) -> List[Tuple[int,int]] | None:
    """Retourne la liste de positions du chemin (start exclu) vers le premier goal trouvé,
    ou None s’il n’y a aucune voie."""
    queue = deque([ (start, []) ])
    visited = {start}
    while queue:
        pos, path = queue.popleft()
        for nxt in [(pos[0], pos[1]-1), (pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]+1)]:
            if not arena.is_free(nxt) and nxt not in goals:   # on ne peut traverser un mur ou une créature (sauf si c’est la destination)
                continue
            if nxt in visited:
                continue
            if nxt in goals:
                return path + [nxt]          # on a atteint une case d’arrivée
            visited.add(nxt)
            queue.append((nxt, path + [nxt]))
    return None

def play_one_round(arena: Arena, part2: bool) -> bool:
    """Retourne True si le combat se poursuit, False si une équipe a été éliminée."""
    for creature in arena.living_creatures():
        # La créature a pu mourir plus tôt dans le round (par exemple par un voisin précédent)
        if creature.hp <= 0:
            continue

        # 1 Cibles les ennemis
        enemies = list(arena.enemies_of(creature))
        if not enemies:                     # aucune cible = combat terminé
            return False

        # 2 Y a‑t‑il déjà un ennemi adjacents ?
        adjacent_enemies = [e for e in enemies if e.pos in creature.adjacent_positions()]
        if not adjacent_enemies:
            # 3 Déplacement vers la case *in‑range* la plus proche
            #   - on collecte toutes les cases libres qui touchent un ennemi
            in_range: List[Tuple[int,int]] = []
            for e in enemies:
                for p in e.adjacent_positions():
                    if arena.is_free(p):
                        in_range.append(p)

            if not in_range:               # bloqué, il ne peut rien faire
                continue

            # Trouver le plus court chemin vers n’importe laquelle de ces cases
            path = bfs_shortest_path(creature.pos, in_range, arena)
            if path:                        # le premier pas du chemin
                creature.move_to(path[0])

            # Après le déplacement, on recalcule les ennemis adjacents
            adjacent_enemies = [e for e in enemies if e.pos in creature.adjacent_positions()]

        # 4 Attaque (si un ennemi est maintenant adjacent)
        if adjacent_enemies:
            # Cible avec le moins de HP, puis ordre de lecture
            target = min(adjacent_enemies,
                         key=lambda e: (e.hp, e.pos[1], e.pos[0]))
            creature.attack_target(target)
            # Pour la partie 2, le combat s'arrête si un elfe meurt
            if part2 and target.is_elf and target.hp <=0:
                return False

    return True   # combat continue

def fight(map_arena: str, elf_advantage: int, part: bool):
    """Retourne le score du combat (ou -1 si un elfe est mort pour la partie 2)"""
    # Implementation of the map
    arena = Arena(map_arena, elf_advantage)
    rnd = 0
    
    # Boucle des rounds
    while True:
        rnd+=1
        alive = play_one_round(arena, part)
        if not alive:
            rnd-=1
            break
    
    # Retourne le score du combat
    # Si on est dans la partie 2 et qu'un elfe est mort, retourne -1
    if part and any(c.is_goblin for c in arena.living_creatures()):
        return -1
    else:
        return rnd * sum(c.hp for c in arena.living_creatures())


# input_arena = """
# #######   
# #.G...#
# #...EG#
# #.#.#G#
# #..G#E#
# #.....#   
# #######
# """

# input_arena = """
# #######
# #E..EG#
# #.#G.E#
# #E.##E#
# #G..#.#
# #..E#.#
# #######
# """

# input_arena = """
# #######
# #E.G#.#
# #.#G..#
# #G.#.G#
# #G..#.#
# #...E.#
# #######
# """

print("Part 1:", fight(input_arena, 0, False))

score = -1
elf_attack_added = 0

while score == -1:
    elf_attack_added+=1
    score = fight(input_arena, elf_attack_added, True)

print("Part 2:", score)

