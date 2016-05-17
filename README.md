This repo is created to experiment and learn mx build system.

Unorganized information learned so far is mentioned here -

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
