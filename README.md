maven-repo
==========

Maven repository for jars not on maven central 

To add a new jar:

 1. Place jar in jars subfolder
 
 2. Add jar to maven repo:
 
 mvn install:install-file -DgroupId=codemining.deps -DartifactId=$depname -Dversion=$version -Dfile=$path -Dpackaging=jar -DgeneratePom=true -DlocalRepositoryPath=./repository  -DcreateChecksum=true
 
 (optionally add -Dsources=$sourcepath to include sources) 
 
 Note that the default $version for all packages except spmf is 1.0

 3. Update relevant pom.xml:
 
 &lt;dependency&gt; <br/>
 &lt;groupId&gt;codemining.deps&lt;groupId&gt; <br/>
 &lt;artifactId>$depname&lt;artifactId&gt; <br/>
 &lt;version&gt;$version&lt;version&gt; <br/>
 &lt;/dependency&gt; <br/>
 
 That's all!
 
More info
---------
http://riaconnection.wordpress.com/2012/08/01/create-your-own-github-maven-repository/
https://bitbucket.org/neil_rubens/rapidminer_maven-repo/wiki/Home
http://maven.apache.org/plugins/maven-install-plugin/install-file-mojo.html
