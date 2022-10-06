import csv
import os
import math

# team A all shots
three_point_corner_teamA = 0
three_point_corner_made_teamA = 0
three_point_corner_efg_teamA = 0

three_point_not_corner_shots_teamA = 0
three_point_not_corner_made_teamA = 0
three_point_not_corner_efg_teamA = 0

two_point_shots_teamA = 0
two_point_shots_made_teamA = 0
two_point_shots_efg_teamA = 0

total_shots_teamA = 0


# team b all shots
three_point_corner_teamB = 0
three_point_corner_made_teamB = 0
three_point_corner_efg_teamB = 0

three_point_not_corner_shots_teamB = 0
three_point_not_corner_made_teamB = 0
three_point_not_corner_efg_teamB = 0

two_point_shots_teamB = 0
two_point_shots_made_teamB = 0
two_point_shots_efg_teamB = 0

total_shots_teamB = 0


def effecient_fg(fgm, tpm, fga):
    efficient_field_goal = (fgm + (0.5*tpm))/fga
    return(efficient_field_goal)


with open('shots_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            x = float(row[1])
            y = float(row[2])
            if_made = int(row[3])

            if row[0] == 'Team A':
                if x > 22.0 and y < 7.8:
                    three_point_corner_teamA += 1
                    total_shots_teamA += 1
                    if if_made == 1:
                        three_point_corner_made_teamA += 1
                elif x < -22.0 and y < 7.8:
                    three_point_corner_teamA += 1
                    total_shots_teamA += 1
                    if if_made == 1:
                        three_point_corner_made_teamA += 1
                elif (pow(x, 2) + pow(y, 2)) > pow(23.75, 2):
                    three_point_not_corner_shots_teamA += 1
                    total_shots_teamA += 1
                    if if_made == 1:
                        three_point_not_corner_made_teamA += 1
                elif (pow(x, 2) + pow(y, 2)) < pow(23.75, 2):
                    two_point_shots_teamA += 1
                    total_shots_teamA += 1
                    if if_made == 1:
                        two_point_shots_made_teamA += 1
                else:
                    total_shots_teamA += 1


            if row[0] == 'Team B':
                if x > 22.0 and y < 7.8:
                    three_point_corner_teamB += 1
                    total_shots_teamB += 1
                    if if_made == 1:
                        three_point_corner_made_teamB += 1
                elif x < -22.0 and y < 7.8:
                    three_point_corner_teamB += 1
                    total_shots_teamB += 1
                    if if_made == 1:
                        three_point_corner_made_teamB += 1
                elif (pow(x, 2) + pow(y, 2)) > pow(23.75, 2):
                    three_point_not_corner_shots_teamB += 1
                    total_shots_teamB += 1
                    if if_made == 1:
                        three_point_not_corner_made_teamB += 1
                elif (pow(x, 2) + pow(y, 2)) < pow(23.75, 2):
                    two_point_shots_teamB += 1
                    total_shots_teamB += 1
                    if if_made == 1:
                        two_point_shots_made_teamB += 1
                else:
                    total_shots_teamB += 1

            line_count += 1


    # team a efficiencies
    three_point_corner_efg_teamA = effecient_fg(three_point_corner_made_teamA, three_point_corner_made_teamA, three_point_corner_teamA)
    two_point_shots_efg_teamA = effecient_fg(two_point_shots_made_teamA, 0, two_point_shots_teamA)
    three_point_not_corner_efg_teamA = effecient_fg(three_point_not_corner_made_teamA, three_point_not_corner_made_teamA, three_point_not_corner_shots_teamA)

    # team b efficiencies
    three_point_corner_efg_teamB = effecient_fg(three_point_corner_made_teamB, three_point_corner_made_teamB, three_point_corner_teamB)
    two_point_shots_efg_teamB = effecient_fg(two_point_shots_made_teamB, 0, two_point_shots_teamB)
    three_point_not_corner_efg_teamB = effecient_fg(three_point_not_corner_made_teamB, three_point_not_corner_made_teamB, three_point_not_corner_shots_teamB)

    print('\nTEAM A')
    print(f'Total Shots Taken: {total_shots_teamA}')
    print('\nCorner 3s Data:')
    print(f'Total Corner 3s Taken: {three_point_corner_teamA}\nTotal Corner 3s Made: {three_point_corner_made_teamA}')
    print(f'Percentage of shots that are Corner 3s: %{(100 *(three_point_corner_teamA/total_shots_teamA)):.3f}')
    print(f'Corner 3s Efficient Field Goal Percentage: %{100 *(three_point_corner_efg_teamA):.3f}')
    print('\n2 Point Shots Data:')
    print(f'Total 2 Point shots taken: {two_point_shots_teamA}\nTotal 2 Point Shots Made: {two_point_shots_made_teamA}')
    print(f'Percentage of shots that are 2 Points: %{(100*(two_point_shots_teamA/total_shots_teamA)):.3f}')
    print(f'2 Point Shots Efficient Field Goal Percentage: %{100 *(two_point_shots_efg_teamA):.3f}')
    print(f'\nRegular 3s Data: ')
    print(f'Total Regular 3s Taken: {three_point_not_corner_shots_teamA}\nTotal Corner 3s Made: {three_point_not_corner_made_teamA}')
    print(f'Percentage of shots that are regular 3s: %{(100 * (three_point_not_corner_shots_teamA / total_shots_teamA)):.3f}')
    print(f'Corner 3s Efficient Field Goal Percentage: %{100 * (three_point_not_corner_efg_teamA):.3f}')

    print('\n\nTEAM B')
    print(f'Total Shots Taken: {total_shots_teamB}')
    print('\nCorner 3s Data:')
    print(f'Total Corner 3s Taken: {three_point_corner_teamB}\nTotal Corner 3s Made: {three_point_corner_made_teamB}')
    print(f'Percentage of shots that are Corner 3s: %{(100 * (three_point_corner_teamB/total_shots_teamB)):.3f}')
    print(f'Corner 3s Efficient Field Goal Percentage: %{100 * (three_point_corner_efg_teamB):.3f}')
    print('\n2 Point Shots Data:')
    print(f'Total 2 Point shots taken: {two_point_shots_teamB}\nTotal 2 Point Shots Made: {two_point_shots_made_teamB}')
    print(f'Percentage of shots that are 2 Points: %{(100 * (two_point_shots_teamB / total_shots_teamB)):.3f}')
    print(f'2 Point Shots Efficient Field Goal Percentage: %{100 * (two_point_shots_efg_teamB):.3f}')
    print(f'\nRegular 3s Data: ')
    print(f'Total Regular 3s Taken: {three_point_not_corner_shots_teamB}\nTotal Corner 3s Made: {three_point_not_corner_made_teamB}')
    print(f'Percentage of shots that are regular 3s: %{(100 * (three_point_not_corner_shots_teamB / total_shots_teamB)):.3f}')
    print(f'Corner 3s Efficient Field Goal Percentage: %{100 * (three_point_not_corner_efg_teamB):.3f}')