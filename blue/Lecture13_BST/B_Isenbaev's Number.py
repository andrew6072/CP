'''

7
Isenbaev Oparin1 Toropov1
Ayzenshteyn2 Oparin1 Samsonov2
Ayzenshteyn2 Chevdar3 Samsonov2
Fominykh1 Isenbaev Oparin1
Dublennykh2 Fominykh1 Ivankov2
Burmistrov3 Dublennykh2 Kurpilyanskiy3
Cormen Leiserson Rivest

'''

INF = 10**5

def UpdateTeam(name_level, team):
    min_level = INF
    for member in team:
        min_level = min(min_level, name_level[member])
    for member in team:
        if name_level[member] != min_level:
            name_level[member] = min_level + 1


n = int(input())
teams = []
for _ in range(n):
    a = list(input().split())
    teams.append(a)

name_level = {}
name_pos = {}

# O(3n)
for i, team in enumerate(teams):
    for j, member in enumerate(team):
        if member == 'Isenbaev':
            name_level[member] = 0
        else:
            name_level[member] = INF
        name_pos[member] = []

# O(3n)
for i, team in enumerate(teams):
    for j, member in enumerate(team):
        name_pos[member].append((i, j))
    UpdateTeam(name_level, team)

#O(3*n^2)
for team in teams:
    for member in team:
        min_level_member_teams = INF # try to find the minimum level of this member in all teams
        for tuple in name_pos[member]:
            min_level_member_teams = min(min_level_member_teams, name_level[member])
        name_level[member] = min_level_member_teams
        for tuple in name_pos[member]: # after updating true level for this member, update teams that have this member
            UpdateTeam(name_level, teams[tuple[0]])

for team in reversed(teams):
    for member in team:
        min_level_member_teams = INF # try to find the minimum level of this member in all teams
        for tuple in name_pos[member]:
            min_level_member_teams = min(min_level_member_teams, name_level[member])
        name_level[member] = min_level_member_teams
        for tuple in name_pos[member]: # after updating true level for this member, update teams that have this member
            UpdateTeam(name_level, teams[tuple[0]])


sorted_dict = dict(sorted(name_level.items(), key=lambda item: item[0])) # O(3nlog(3n))

for key in sorted_dict.keys():
    value = sorted_dict[key]
    if value != INF:
        print(key, value)
    else:
        print(key, 'undefined')
