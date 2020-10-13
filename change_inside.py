import glob, os
os.chdir("/home/plase1/Documents/yolo_data/data/training_jpeg")
for file in glob.glob("*.txt"):
    handle = open(file)
    st = handle.readline()
    print("1" + st[2:])
    with open(file, "w") as f:
    	f.writelines("1" + st[2:])
    	
