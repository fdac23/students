# FAQ:

Q1: I am finding some of the directions in class very confusing, and
I think it is because I do not understand the reasoning being some
of the steps. 

A: Please look at https://github.com/fdac23/lectures/blob/master/tools.pdf
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

# Common Problems

## **Forward your local port to the machine's notebook port:**
`-L 8000:localhost:8888` forwards port 8000 on your machine to the jupyter notebook already running in your container on port 8888  
you can also add this to your config:
`LocalForward 8000 localhost:8888`

## **Enable SSH Agent Forwarding to use your local SSH keys in your container:**
add option `-o ForwardAgent=yes` and this will allow you to use your local SSH keys to authenticate for cloning git repos to your container  
`ForwardAgent yes` option in the ssh config

You can check what keys your SSH agent has registered with `ssh-add -l`

Here's an example: (replace my values with yours)

```ssh
Host fdac23
  hostname da2.eecs.utk.edu
  Port 7701
  user bklein3
  LocalForward 8000 localhost:8888
  ForwardAgent yes
```
Then you can simply type `ssh fdac23`, no extra options needed

## **MacOS: No SSH keys are being forwarded?**
You need to make sure you have an SSH agent running: <https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent>
If you're not a homebrew user, you might need the `-K` flag to `ssh-add` when you add your keys/identities to your SSH agent.

## **ZSH: New user / first time shell setup**
If you're prompted when logging in for how you want your shell to be set up, you'll probably want to copy the default from the system (recommended, #2)
You can re-run the first time setup with `autoload -U zsh-newuser-install && zsh-newuser-install -f`

## **Local VSCode connection to your remote Jupyter notebook**
[https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_connect-to-a-remote-jupyter-server](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_connect-to-a-remote-jupyter-server)

## **"Connection refused" trying to open the notebook after logging in**
Check that you're using the right local and remote port syntax for the `LocalForward`
Check that your notebook server is still running: `ps aux | grep 'notebook' | grep 'python3'`: if this shows nothing, then restart your notebook
