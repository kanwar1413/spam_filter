[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15963158&assignment_repo_type=AssignmentRepo)
# Activity 1 - (5%)
## Due Date - Friday September 27, 2024 (Late Policy: 10% per day)
## Questions


1. Spam Filter Email Agent (50%)

Create an agent (in C++ or Python) which filters email classifying it as either spam or not.

Email is typically stored in [.eml format](https://docs.fileformat.com/email/eml/#brief-history-of-eml) composed of headers and a body.  The file is stored in text format with the header in plain text.  The body contents can be encrypted or encoded in arbitrary formats .  In this case we assume attachments of type “text” are readable by the agent

The system has access to 
-	an _allow list_, which lists safe domains…emails coming from that domain are classified as non-spam regardless of its contents 
-	an _restrict list_, which lists safe domains…emails coming from that domain are classified as spam regardless of its contents 
-	a _bad word list_, which list words that are likely to be in spam emails. If more than 5 words within the body of the email are found on this list and it is not coming from a domain on the allow list, then it should be considered spam 

Spam email should be placed in a spam directory.  Others should be a placed in an email directory 


a) Specify the *task environment* for this problem using PEAS.

b)	List the properties of the task environment.

c)	What type of agent is most appropriate for this problem?  Justify your answer.

d)	Implement an agent that acts rationally in this environment.  Use the structure/form for the agent types selected in the book.


 
2. Search Problem (50%)

You have three jugs, measuring 12 gallons, 8 gallons, and 3 gallons, and a water faucet. You can fill the jugs up or empty them out from one to another or onto the ground. You need to measure out exactly one gallon.

a) Define your _states_ (initial, goal(s)), _action(s)_, _transition model_

b) Does a heuristic function makes sense for this problem?  If so, informally define what it would be. (A description as oppose to a precise mathematical function is sufficent.) 

c) Is _any_ search algorthims guarenteed to reach a goal state?  Explain your answer.

d)	Implement the breadth first search algorithm as described in Figure 3.9 in order to search your defined state space.


 ## Submission Notes

 - 40% of the grade will be the presentation of your work
 - Presentations will take place on **Friday September 27** during lab time either in the lab or via our Zoom link
 - Implementations must include runnable tests along with test data.  Instructions for running these tests must be provided.  Preferably GitActions are used to have the tests run automatically.
 - Implementations can be done in a language of your choice but must use the code snippets provided in the text to guide your design.
 
