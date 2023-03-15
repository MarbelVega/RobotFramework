CMD Line instructions to be run from project folder. This should be specified as windows shell command under Build inn Jenkins.

Running robot individual test:

 robot -t TestName TestSuite
 
Running robot filtered with tags:(include/exldue with wildcards)
 
  robot -i regression -e s* TestSuite
  
For PyTest:

pytest (all test_ )
pytest -m "smoke" (tags)
pytest -s -v (verbose print outputs)
pytest test.py::class::method

link: https://www.youtube.com/watch?v=z9eCIx49OHQ
