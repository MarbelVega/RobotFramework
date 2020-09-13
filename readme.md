CMD Line instructions to be run from project folder. This should be specified as windows shell command under Build inn Jenkins.

Running robot individual test:

 robot -t TestName TestSuite
 
Running robot filtered with tags:(include/exldue with wildcards)
 
  robot -i regression -e s* TestSuite