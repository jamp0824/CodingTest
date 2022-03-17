from xmlrpc.client import MAXINT

drinkList = {
    '0':[100,320], '1':[232,720],  '2':[600,103],     '3':[100,124],     '4':[730,1076],    '5':[185,125],     '6':[104,600], 
    '7':[392,705],     '8':[33,265],     '9':[89,421],}

def answer(drinkData, fixNum):
    startIdx = 0
    recordIdx = 0
    total = 0 - MAXINT
    while(startIdx <= len(drinkData) - fixNum):
        curCal = 0
        for i in range(startIdx, startIdx + fixNum):
            curCal += drinkData[f'{i}'][1] - drinkData[f'{i}'][0]
        if total < curCal:
            total = curCal
            recordIdx = startIdx
        startIdx += 1
    tau = 0
    cafe = 0
    for i in range(recordIdx, recordIdx + fixNum):
        print(i, end=' ')
        tau += drinkData[f'{i}'][1]
        cafe += drinkData[f'{i}'][0]
    print(f'의 타우린 합은 {tau}, 카페인 합은 {cafe}로 가장 효과가 좋습니다.')

answer(drinkList, 3)