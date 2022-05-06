print("Time converter")

while True:
  for i in input().split('\n'):
    segs = i.strip('\r').split(' ')
    if len(segs) == 2:
      print(segs[0] + 'T' + segs[1] + '+08:00')
    else:
      print(segs[0] + 'T00:00:00+08:00')