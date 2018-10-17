
with open("s_box_raw.txt", 'r') as raw:
    results = []
    for lines in raw:
        if "||" in lines:
            lines = lines.strip()
            lines = lines.strip("|")
            raw_num = lines.split("||")
            raw_num = [int(num) for num in raw_num]

            results.append(raw_num)

for i in range(0, len(results), 4):
    print(results[i:i+4])
        

