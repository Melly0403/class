scores = [85, 4, 77, 90, 58, 66]
def average(scores):
    return round(sum(scores)/len(scores),1)
def count_pass(scores, cut=60):
    cnt=0
    for s in scores:
        if s>=cut:
            cnt +=1
    return cnt
print(f"평균:{average(scores)}")
print(f"60점 이상:{count_pass(scores)}명")
print(f"70점 이상: {count_pass(scores, 70)}명")
