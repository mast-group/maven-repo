maven-repo
==========

Maven repository for jars not on maven central 

To add a new jar:

 1. Place jar in jars subfolder
 
 2. Add jar to maven repo:
 
 mvn install:install-file -DgroupId=codemining.deps -DartifactId=$depname -Dversion=1.0 -Dfile=$path -Dpackaging=jar -DgeneratePom=true -DlocalRepositoryPath=./repository  -DcreateChecksum=true
 
 3. Update relevant pom.xml:
 
 &lt;dependency&gt; <br/>
 &lt;groupId&gt;codemining.deps&lt;groupId&gt; <br/>
 &lt;artifactId>$depname&lt;artifactId&gt; <br/>
 &lt;version&gt;1.0&lt;version&gt; <br/>
 &lt;/dependency&gt; <br/>
 
 That's all!
 
