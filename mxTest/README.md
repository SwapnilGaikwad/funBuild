This repo is created to experiment and learn mx build system.

Unorganized information learned so far is mentioned here. This shall be updated with my understanding of mx.

mx build
- Primary suite requires a directory starting with name mx.<name> .
	After executing 'mx build' command following error could be seen
	"no primary suite found"

- This error goes after creating a primary suite by creating a suite.py file in the mx.<name> directory
  Now on executing 'mx build' command following error is shown.
  "cannot determine VC for ~/sandbox/freshTruffle/delme/TestJoda"

- This error occurrs because mx cannot find any repository/version control system in the given directory.
  It looks like mx requires to have one of the know version control system which includes 'git', 'hg' or 'binaryVC'

  To overcome this error, git repository created and all the necessary files pushed into the repository.

- After doing 'mx build' following error occurrs,
  '/home/sgaikwad/sandbox/freshTruffle/delme/TestJoda/mx.sample/suite.py must define a variable named "suite"'

- 'mx build' command becomes successful after adding the following content
	suite = {
	  "mxversion" : "5.19.6",
	  "name" : "sample"
	}

Create a custom target e.g. 'fun' which could be invoked using 'mx fun'
- Custom targets are allows user to create specific targets to be invoked with mx command and specify a corresponding action.
- Need to add mx_<suiteName>.py file in the directory mx.<suiteName>. Here mx.sample/mx_sample.py file is added.
- This file is executed when mx command is called in a particular suite.
- To add 'fun' target following piece of code has to be added
	import mx

	def function(args=None):
   	  print "###### In function() for target 'fun'"

	_suite = mx.suite('sample')
	mx.update_commands(_suite,{
  	  'fun' : [function,'']}
	)
- Few important points to note,
	- import the mx module
	- '_suite' is the name of the current suite for which we are adding a new target. If incorrect suite name is given then following error is shown. Here incorrect suite name 'incorrectSuiteName' is given
	'suite named incorrectSuiteName not found'
	- 'fun' target is made available by adding into the mx commands for a given suite. If this name is incorrect then mx would print help message with list of possible commands.
	- Add a dictionary entry with a target name for key ('fun') and value as an array of 2 elements [<function_name>, '']. 2nd element I'm not sure at this point but it is not an argument to function. However if the 2nd argument is not given in the array then following error comes,
	'ValueError: need more than 1 value to unpack'
	- Arguments to function shall be marked as 'args=None' else following error is shown.
	'TypeError: function() takes no arguments (1 given)'
