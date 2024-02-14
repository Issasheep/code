from string import ascii_letters,digits, punctuation
import time 
start = time.time() 
for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print (i,j,k,l)
 #               for h in ascii_letters + digits + punctuation:
  #                  for u in ascii_letters + digits + punctuation:
  #                      for z in ascii_letters + digits + punctuation:
  #                          for s in ascii_letters + digits + punctuation:
                                
end = time.time()
print (start-end)
