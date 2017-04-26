def read_conf(file_path = "E:\learning\python\BulkFileCopy\configuration.txt"):
	dict1={}
	fp1 = open(file_path,"r")
	for i in fp1.readlines():
		dict1[i.split(':')[0]]=i.split(':')[1].strip('\n')
	return dict1


source_file = "E:\learning\python\BulkFileCopy\SourceFolder\PFnotice.txt"
dest_file = "E:\learning\python\BulkFileCopy\Dest\dest.txt"
try:
	fp1 = open(source_file,"r")
except Exception as err:
	if err[1] == "No such file or directory":
		dict2 = read_conf()
		if dict2["Source not found"] == "Skip the copy":
			print "Source file not find and skipping the copy according to configuration"
		#print "not found"
else:
	try:
		fp2 = open(dest_file,"r")
	except Exception as err1:
		if err1[1] == "No such file or directory":
			print "Destination file not found"
	else:
		print "Destination file exists checking the configuration file"
		dict2 = read_conf()
		if dict2["destination found"] == "skip":
			print "Configuration file says to skip the copy, skipping"
		elif dict2["destination found"] == "replace":
			print "Configuration file says to replace the data, replacing"
			data1 = fp1.read()
			fp2 = open(dest_file,"w")
			fp2.write(data1)
			print "Replaced"
			fp2.close()


	