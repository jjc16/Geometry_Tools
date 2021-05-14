def hypercube_corners(start, length):
    '''Find the vertices (corners) of an n-dimensional hypercube given
    a minimal starting vertex (vertex with all coordinates at a minimum
    and the length of a side. The dimension of the hypercube is inferred
    from the minimal vertex.
    
    Inputs: start - the minimal starting vertex
            length - the length of the sides
            
    Returns: the vertices of a hypercube
    
    Example start = [1, 1, 1, 1, 2] , length = 2
    
    Author jjc16_1@yahoo.com 
    '''
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