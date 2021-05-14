def min_all_dims(list_):
  out = []
  for ii in range(len(list_[0])):
    tmp = [pt[ii] for pt in list_]
    t2 = max(tmp)
    t1 = min(tmp)
    out.append(t2 - t1)
  return min(out)

def find_coord(point1, point2):
  for ii in range(len(point1)):
    if point1[ii] != point2[ii]:
      return ii
  return []

def gen_tst_pts(start, end, coord):
    tst_pts=[]
    for ii in range(start[coord], end[coord]+1):
      tmp = start.copy()
      tmp[coord] = ii
      tst_pts.append(tmp)
    return tst_pts

def test_pts(list_, tst_pts):
  return [pt in list_ for pt in tst_pts]

def line_in_list(list_, start, end, coord):
  tst_pts = gen_tst_pts(start, end, coord)
  out = test_pts(list_, tst_pts)

  return all(out)

def hyper_cube_corners(start, length):
  if len(start) == 1:
    tmp = start.copy()
    out = []
    out.append(tmp)
    tmp2 = list(map(lambda x:x+length, tmp))
    out.append(tmp2) 
    return out
  else:
    tmp = hyper_cube_corners(start[:-1], length)
    out = []
    for item in tmp:
      item1 = item.copy()
      item1.append(start[-1])
      item2 = item.copy()
      tmp = start[-1] + length
      item2.append(tmp)
      out.append(item1)
      out.append(item2)
    return out


def find_lines(corners):
  lines = []
  for ii in range(len(corners)):
    for jj in range(ii, len(corners)):
      tmp = [int(not(corners[ii][kk] == corners[jj][kk])) for kk in range(len(corners[ii]))]
      # print(tmp)
      if sum(tmp) == 1:
        lines.append(tuple((corners[ii], corners[jj])))

  return lines


def find_all_cube_one_size(list_, sz):
  list_.sort()
  count = 0
  for l in list_:
      corners = hyper_cube_corners(l, sz)
      lines = find_lines(corners)
      ln_lst = []
      for ln in lines:
      coord = find_coord(ln[0], ln[1])
      pts = gen_tst_pts(ln[0], ln[1], coord)
      tmp = test_pts(list_, pts)
      tmp = all(tmp)
      ln_lst.append(tmp)
      if all(ln_lst):
      count += 1

  return count

def find_all_hypercubes(list_):
  count = 0
  out_dict = {}
  sz = min_all_dims(list_)
  for ii in range(1,sz+1):
    tmp = find_all_cube_one_size(list_, ii)
    out_dict[ii] = tmp
    count += tmp

  return count, out_dict