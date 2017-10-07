import dropbox, sys, os

dbx = dropbox.Dropbox('PQP4kBo8X-AAAAAAAAABCru0hFHK9T4rnvf72tVl7u4zN3TfduXgtu7Eg5PJecHd')
rootdir = '/home/xilinx/jupyter_notebooks/common/data'

print('Attempting to upload...')

counter = 0
for dir, dirs, files in os.walk(rootdir):
	for file in files:
		try:
			file_path = os.path.join(dir,file)
			dest_path = os.path.join('/SnapBack',file)
			print 'Uploading %s to %s' % (file_path, dest_path)
			with open(file_path) as f:
				dbx.files_upload(f.read(), dest_path, mute = True)
		except Exception as err:
			print("Failed to upload %s\n%s" % (file, err))
			counter += 1

print("Finished with %i errors" % (counter))
