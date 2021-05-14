import csv

datal = []

with open("data\\tabel.csv","r") as f:
    reader  = csv.reader(f)
    # val = reader[88:]
    for i in reader:
        datal.append(i)
headers = datal[0]
other_planets = datal[1:]
to_lower_case=[]

#lower case
for i in other_planets:
    t =[]
    j:str
    for j in i:
        if i[0]==j:
            t.append(j.lower())
        else:
            t.append(j)
    to_lower_case.append(t)
to_lower_case.sort()
listwithinlist=[[]]
sorted_list:listwithinlist=sorted(to_lower_case,key=lambda x:x[0])

#merging

with open("data\\scraped.csv","r") as f:
    reader  = csv.reader(f)
    i=[]
    n,m=1,0
    # print(reader,len(sorted_list))
    for i in reader:
        if n==1:
            for j in i:
                headers.append(j)
        for j in i:
            sorted_list[n].append(j)
        # print(i[0])
        n+=1
    print(len(sorted_list[0]))
with open("data\\final.csv","w",newline='') as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(sorted_list)
    
