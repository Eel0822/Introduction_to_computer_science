#打開CSV文件並讀取內容
f = open("/Users/shananlee/Downloads/pe8_data.csv", "r")
data = f.readlines()
f.close()

#解析CSV文件頭部
headers = data[0].strip().split(',')

#將每一行數據解析成字典
teams = []
for row in data[1:31]:
    values = row.strip().split(',')
    team = {headers[i]: values[i] for i in range(len(headers))}
    teams.append(team)

#解析主場和客場勝率
def parse_record(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)    

#將勝率換成浮點數
def sort_by_pct(team):
    return float(team['PCT'])

#按照東西區排序
def sort_teams_by_conference(teams):
    eastern_teams = [team for team in teams if team['Conference'] == 'Eastern']
    western_teams = [team for team in teams if team['Conference'] == 'Western']

    eastern_teams_sorted = sorted(eastern_teams, key=sort_by_pct, reverse=True)
    western_teams_sorted = sorted(western_teams, key=sort_by_pct, reverse=True)

    return eastern_teams_sorted, western_teams_sorted
    
#回答問題1
def q1():
    print("Teams from the Eastern Conference with home win-loss percentage lower than away win-loss percentage:")
    for team in teams:
        if team['Conference'] == 'Eastern':
            home_win_percentage = parse_record(team['HOME'])
            away_win_percentage = parse_record(team['AWAY'])
            if home_win_percentage < away_win_percentage:
                print(team['Team'])

#回答問題2
def q2():
    eastern_diff = []
    western_diff = []
    
    for team in teams:
        pf = float(team['PF'])
        pa = float(team['PA'])
        diff = pf - pa
        if team['Conference'] == 'Eastern':
            eastern_diff.append(diff)
        else:
            western_diff.append(diff)
    
    eastern_avg_diff = sum(eastern_diff) / len(eastern_diff) if eastern_diff else 0
    western_avg_diff = sum(western_diff) / len(western_diff) if western_diff else 0
    
    print("Eastern Conference average PF-PA difference: {:.2f}".format(eastern_avg_diff))
    print("Western Conference average PF-PA difference: {:.2f}".format(western_avg_diff))
    
                
#回答問題3
def q3():
    eastern_teams_sorted, western_teams_sorted = sort_teams_by_conference(teams)
    
    print("Eastern Conference Teams Sorted by Win-Loss Percentage:")
    for rank, team in enumerate(eastern_teams_sorted, start=1):
        print(f"{rank}. {team['Team']}")

    print("Western Conference Teams Sorted by Win-Loss Percentage:")
    for rank, team in enumerate(western_teams_sorted, start=1):
        print(f"{rank}. {team['Team']}")
        
print("Q1")           
q1()
print("")
print("Q2")
q2()
print("")
print("Q3")
q3()