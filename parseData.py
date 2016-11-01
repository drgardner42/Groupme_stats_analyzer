import sys

def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)
    if not chunk:
      yield buf
      break
    buf += chunk

if len(sys.argv) != 2:
	print "please specify input file"
	exit(1)

names = []
with open(str(sys.argv[1])) as f:
  for line in myreadlines(f, ","):
    #print line
    names.append(line)

jeff=0 
dustin=0
schreiber=0
prohaska=0
curtis=0
mayes=0
donnie=0 
rocco=0
dom=0

for index, name in enumerate(names):
	if "Jeffery" in name:
		try:
			jeff+=int(names[index+1].strip( '[)]'))
		except:
			pass
	if "Dustin" in name:
		try:
			dustin+=int(names[index+1].strip( '[)]'))
		except:
			pass
	if "Schreiber" in name:
		try:
			schreiber+=int(names[index+1].strip( '[)]'))
		except:
			pass
	if "Prohaska" in name or "Impregnable" in name:
		try:
			prohaska+=int(names[index+1].strip( '[)]'))
		except:
			pass
	if "Carney" in name or "Jodi" in name:
		try:
			donnie+=int(names[index+1].strip( '[)]'))
		except:
			pass

print "Jeff: ", jeff
print "Dustin: ", dustin
print "Schreiber: ", schreiber
print "Prohaska: ", prohaska
print "Donnie: ", donnie
