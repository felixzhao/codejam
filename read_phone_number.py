
def splitphonenum(num, order):
  chunk = [int(n) for n in order.split('-')]
  return [num[sum(chunk[0:i]):sum(chunk[0:i])+chunk[i]] for i in range(len(chunk))]

def getchunkvoice(num_chunk):
  result = []
  times = {2:'double',3:'triple',4:'quadruple',5:'quintuple',6:'sextuple',7:'septuple',8:'octuple',9:'nonuple',10:'decuple'}
  words = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
  
  count = 0
  cur_word = ''
  if len(num_chunk) == 1:
    result.append(words[num_chunk[0]])
    return result
    
  for i in xrange(len(num_chunk)):
    if count == 0:
      cur_word = words[num_chunk[i]]
      count += 1
    elif words[num_chunk[i]] != cur_word:
      if count > 1 and count <= 10:
        result.append(times[count])
      result.append(cur_word)
      cur_word = words[num_chunk[i]]
      count = 1
      if i == len(num_chunk) - 1:
        result.append(words[num_chunk[i]])
    elif words[num_chunk[i]] == cur_word:
      count += 1
      if i == len(num_chunk) - 1:
        if count > 1 and count <= 10:
          result.append(times[count])
        result.append(cur_word)
  return result

def getvoice(num):
  result = []
  for n in num:
    result += getchunkvoice(n)
  return result
  
if __name__ == '__main__':
  lines = open('A-small-attempt0.in','r').readlines()
  outfile = open('small.out','w')
  count = int(lines[0])
  for i in xrange(1,count+1):
    line = lines[i].split()
    numlist = splitphonenum(line[0],line[1])
    print numlist
    voice = getvoice(numlist)
    voicestring = ' '.join(voice)
    print voicestring
    outfile.write('Case #' + str(i) + ': ' + voicestring + '\n')
  outfile.close()