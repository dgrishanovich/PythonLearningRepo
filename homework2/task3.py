monthsList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
inputMonthNumber = int(input("Input month number: "))
strMonth = monthsList[inputMonthNumber - 1]

solutionType = input('PLease choose the type of solution: List - 0, Dict - 1: ')
if solutionType == 0: # List Solution
    monthsListMapping = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer',
                         'Autumn', 'Autumn', 'Autumn', 'Winter']
    print(monthsListMapping[inputMonthNumber - 1])
else: # Dict Solution
    monthSeasonDict = {'Winter': ['January', 'February', 'December'], 'Spring': ['March', 'April', 'May'],
                       'Summer': ['June', 'July', 'August'], 'Autumn': ['September', 'October', 'November']}
    for key, value in monthSeasonDict.items():
        if strMonth in value:
            print(key)