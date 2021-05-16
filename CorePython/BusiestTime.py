

intervals = [
    {"timestamp": 1, "count": 10, "type": "enter"},
{"timestamp": 3, "count": 2, "type": "exit"},
{"timestamp": 5, "count": 1, "type": "enter"},
{"timestamp": 6, "count": 1, "type": "enter"},
{"timestamp": 7, "count": 1, "type": "enter"},
{"timestamp": 9, "count": 3, "type": "exit"},
{"timestamp": 10, "count": 8, "type": "exit"}
]

inbuilding = 0
list = []
for ele in intervals:
    if ele["type"] == "enter":
         inbuilding = inbuilding + ele["count"]
    else:
        inbuilding = inbuilding - ele["count"]

    list.append(inbuilding)

print(max(list))
index = list.index(max(list))
print(index)
print("Building was busiest between ", intervals[index]["timestamp"] , " and ", intervals[index+1]["timestamp"]  )
