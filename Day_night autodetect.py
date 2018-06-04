st = raw_input().split(" ")
sm =0.0
for i in range(len(st)):
    temp = st[i].split(",")#Values of R,G,B stored in array temp where split(",") signifies that values are seperated by comma
    sm += (int(temp[0])+int(temp[1])+int(temp[2]))/3
sm = sm/len(st)
if sm < 80:
    print "night"
else:
    print "day"
