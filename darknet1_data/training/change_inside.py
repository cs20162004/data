import glob, os
os.chdir("/home/plase1/Documents/yolo_data/darknet/training/dataset")
for file in glob.glob("*.txt"):
    handle = open(file)
    st = handle.readline()
    print("0" + st[1:])
    with open(file, "w") as f:
    	f.writelines("0" + st[1:])
    	
