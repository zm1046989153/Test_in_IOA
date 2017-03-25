import time
filename = "..//report//"+time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))+".html"

#filename="..//report//ddd.html"
print filename

file(filename,'wb')

