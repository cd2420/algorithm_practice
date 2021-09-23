n, m = map(int, input().split())

girl_group = dict()
group_girl = dict()

for i in range(n):

    team_name = input()
    member = int(input())
    girl_group[team_name] = list()

    for j in range(member):
        girl_name = input()
        girl_group[team_name].append(girl_name)
        group_girl[girl_name] = team_name

for _ in range(m):
    name = input()
    check_type = int(input())
    if check_type == 1:
        print(group_girl[name])
    else:
        for n in sorted(girl_group[name]):
            print(n)
