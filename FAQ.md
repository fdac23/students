# FAQ:

Q1: I am finding some of the directions in class very confusing, and
I think it is because I do not understand the reasoning being some
of the steps. 

A: Please look at https://github.com/fdac22/lectures/blob/master/tools.pdf
Some rationale is provided there

Q2: Could you explain in more detail the overall objective of
Practice0? Is it just to help make sure we are using git correctly
from da0? I actually prefer default configs, but I may set my editor
to vim. 

A: To make sure everyone is able to run jupyter notebook, does a minimal task in python, and can go through 
fork/clone/commit/push/submit pull request cycle. The type of editor
for git commits is immaterial, but can be configured based on
individual preference. 


Q3: Though it is implicitly clear, you have never really specified
that you want us to work from your machine da2. Is this necessary
for certain software we will be using? Alternatively, could we work
from our own machines and share our local git config? 

A: da2 runs containers with the environment that has all the needed pieces. You
can run the same container (audris/jupyter-r) on your laptop/elswhere, or,
you can install the software (jupyter) directly on your laptop. 

Q4: Will we be cloning git into da2 from now on?

A: Unless you want to set up the environment elsewhere.

Q5: Why are we using git-request-pull? With naming conventions of UTKID there should be no accidental overwritting of assignments. Even if assignments were overwritten, version control is meant to recover work. Futhermore, malicious use of github is trackable so you would be able to find students abusing github.

A: Pull requests are a standard procedure to submit code from individual repo to team repo and is widely used in open source and closed source projects.

Q6: How do you run pull requests from command line? It doesn't feel
like best-practice to constantly have to log into github and
navigate the browser. I have looked at several instruction guides,
including github's page, and it is not very clear to me. I can keep
reading though if you are unsure. 

A: You don't want to run many pull requests, because I need to merge each one.
Please try to do only one for each assignment. It is easy to set up command line
script that triggers the pull request for you: please use github api for that.
