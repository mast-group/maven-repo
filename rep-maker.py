#!/usr/bin/python
import sys
import os.path

if len(sys.argv) < 2:
    sys.stderr.write('Usage: full_path_to_jars_dir jars_ver\n')
    sys.exit(1)

folder = sys.argv[1]
rm_ver = sys.argv[2]
groupID = 'codemining.deps'

f = open('dependencies.xml', 'w')
f_commands = open('mvn_commands', 'w')

print 'processing: \n'
for root, dirs, files in os.walk (folder):
    for filename in files:
	if filename.endswith('.jar') == True:
		print filename + '\n'
        # create dependencies for pom.xml
        f.writelines('<dependency>\n')
        f.writelines('<groupId>' + groupID + '</groupId>\n')
        f.writelines('<artifactId>' + filename[:-4] + '</artifactId>\n')
        f.writelines('<version>' + rm_ver + '</version>\n')
        f.writelines('</dependency>\n\n')

        # create dependencies for pom.xml
        command = 'mvn install:install-file -DgroupId=' + groupID + ' -DartifactId='+ filename[:-4] + ' -Dversion=' + rm_ver + ' -Dfile=' + os.path.join(root,filename) + ' -Dpackaging=jar -DgeneratePom=true -DlocalRepositoryPath=./repository  -DcreateChecksum=true'
        f_commands.write(command + '\n')


f.close()
f_commands.close()

print 'TODO: \n'
print f_commands.name + ' containts mvn commands that need to be executed; may need to do chmod + x'
print f.name + ' containts dependencies that need to be added to pom.xml'
print 'Dont forget to commit to git/maven repository'