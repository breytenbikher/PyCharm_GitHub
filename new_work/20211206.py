N,K = 1,1
# N = int(input(''))
# K = int(input(''))
cluster = K // (2*N + 1)
clust_seat = K % (2*N + 1)
if clust_seat <= N:
    clust_row = 1
    seat = clust_seat
else:
    clust_row = 2
    seat = clust_seat - N
row = cluster * 2 + clust_row

print(row, seat)


