# Connect-4 AI bot.

## PROJECT REPORT.

## Team: Prudhvi and Vijay.

### Introduction: 

* 1.1	What AI system are you interested in investigating further? 

The AI system that I am interested in is a game called Connect 4. It is sequential two player game in which the objective is to create a line of four of your own discs that runs horizontally, vertically, or diagonally before your opponent. In General, all these board games like Chess, Go, Checkers etc. use search algorithms and, in this case, it uses Minmax algorithm which is an example for Depth-First search technique. We have also implemented Reinforcement Learning and Alpha – Beta pruning for solving this game. With the help of a system of observations, actions, and rewards, an agent can repeatedly "play" an environment using this reinforcement learning technique, which also integrates deep neural networks
* 1.2	Why is it of interest to you?
I am interested in AI board games because they are easy to understand, take one step at a time and can be easily implemented by AI modules. These board games are incorporated with search algorithms. I can gain more hands-on experience on search algorithms by this project.	
* 1.3	What specifically your project will focus on? What's the focus of your investigation?
We planned on implementing Alpha- Beta pruning and Minmax algorithm which are classic examples of Symbolic AI and along with them we have also tried the Machine Learning part by implementing the Reinforcement learning by using agents to train a model. By using Alpha - Beta pruning we designed an AI system that plays the game as opponent tries to make a move that will eventually results in a win to the system and coming to the Reinforcement Learning using the Q-learner agents(Q-Learning) we are training a model by observations, actions, and rewards. for finding optimal results in future.
Lead Author: Prudhvi, Reviewer: Vijay 

### Theoretical Background:

* What area or field of AI provides the theoretical framework for the chosen AI system?
We mainly concentrated on Alpha-Beta Pruning (Symbolic AI) and Q-Learning which is an algorithm of Reinforcement Learning. Symbolic AI tries to solve the problem in the same way humans thinks to solve it. The approach would very similar. Where as Machine Learning is more of training a model to solve the problem by considering all the observations, actions, and rewards by which it has trained. It may not replicate human analysis. 
* What are the key concepts and techniques that the AI application is based on?
`Minmax Algorithm`: A backtracking algorithm is used to find a solution to computational problems in such a way that a candidate is incrementally built towards a solution, one step at a time. And the candidate that fails to complete a solution is immediately abandoned. It is implemented like a search tree simultaneous levels of min(Tries to minimize outcome of opponent) and max(Tries to minimize outcome of opponent).
`Alpha – Beta Pruning`: Alpha beta pruning is an optimization technique for the minimax algorithm. The model becomes more complex as a result of unnecessary branches. In order to prevent this, Alpha-Beta pruning is used, which spares the computer from having to examine the entire tree. The process is slowed down by these peculiar nodes. Therefore, the algorithm becomes efficient by deleting these nodes.
`Deep-Q-Learning`: This method of Reinforcement Learning incorporates deep neural networks in a way that allows an agent to ‘play’ an environment repeatedly and learn the environment over time through a system of observations, actions, and rewards. This structure has obvious benefits over a standard deep neural network implementation as it allows the agent to interact with its surroundings, receive feedback from its surroundings, and then optimize for desirable (highly rewarded) future actions.[1]

Lead Author: Prudhvi, Reviewer: Vijay

### Development Approach

* HOW did you carry out the plan? This is where you describe the HOW of your project, guided by the WHAT.
The first thing we have done is find an idea for the project that uses both symbolic AI and Machine Learning part. After some research we got the idea of our project which is Connet4-AI bot.
We have prepared proposal and Design for the project followed by the codebase. Through out the development process we have used below tools.

1.Python IDE – PyCharm.

2.For version control and collaboration – GitHub.

We have tried various features of GitHub like project board to document the progress. As this is a collaborative project GitHub is best suitable tool for reviewing the team members work and we have used git branches to individually works on our part the project. 

3.Interpreter – python 3.10

4.Modules – NumPy, pygame, sys, math and random. 

* HOW did the team divided the work? 

I(Prudhvi) acted as developer of the project and my teammate(Vijay) is the team lead. Project Proposal, Design and Readme part is distributed equally. And coming to codebase we have three modules Minmax, Alpha-Beta Pruning and Q-Learning. I worked on Minmax, and Q-Learning part and Vijay acted as the reviewer, whereas coming to Alpha-Beta Pruning Vijay worked on it and I acted as the reviewer.
Lead Author: Prudhvi, Reviewer: Vijay

### Working Example

* Describe the working example?
Our working example is the actual game of connect-.  It is sequential two player game in which the objective is to create a line of four of your own discs that runs horizontally, vertically, or diagonally before your opponent. We have created three scenarios. Player vs Player, Player vs AI and Training the system. Player vs Player part is implemented by using min-max algorithm. In this module both the players in the game are humans. Player vs AI is implemented using Alpha-Beta Pruning, which is an enhanced version of minmax algorithm. In this part human can play with the AI system which tries to beat him in every possible move and the last part is training the module with Reinforcement Learning.
For this we have used Deep-Q-Learning, which incorporates deep neural networks in a way that allows an agent to ‘play’ an environment repeatedly and learn the environment over time through a system of observations, actions, and rewards.
* Describe the data the AI application example uses. 

The first two parts (min-max and Alpha-Beta pruning) takes response from the players and act accordingly whereas the final part take date of every observations, actions, and rewards and train the model to act optimally in every possible situation in the future.
Lead Author: Vijay, Reviewer: Prudhvi

### Evaluation

* What are the safety and trustworthy considerations for developing your project's AI application example?
Below are the safety and trustworthy considerations for developing my AI project Application

Maintain data privacy and security: Look across the AI system lifecycle and make sure that portions that interact with data, metadata and models are secured and maintain data privacy as required.
Reduce the bias of data sets to train AI models: Examine training data sets for sources of potential bias and make sure that communities are represented in a fair and equitable way.
Provide transparency into AI and data usage: Organizations should let AI system users know how their data is being used to train or power AI systems and provide visibility into aspects of data selection, usage and even the business model that the AI system supports. 
Keep the human in the loop: Even when AI systems are operating in an autonomous fashion, there should always be a person keeping an eye on system performance. 
Limit the impact of AI systems on critical decision-making: If the AI system is being used for critical life-or-death or high-impact decisions, there should always be an identified failover process or human oversight to make sure that no harm is done.[2]

* What are the ethical considerations for developing your project's AI application example?
Four major ethical issues must be addressed: (1) informed consent to use data, (2) safety and transparency, (3) algorithmic fairness and biases, and (4) data privacy are all crucial factors to consider.[3]

Lead Author: Vijay, Reviewer: Prudhvi


References: 
1.	 https://towardsdatascience.com/playing-connect-4-with-deep-q-learning-76271ed663ca.
2.	 https://www.techtarget.com/searchenterpriseai/feature/Building-trustworthy-AI-is-key-for-enterprises.
3.	Stahl, B.C. (2021). Ethical Issues of AI. In: Artificial Intelligence for a Better Future. Springer Briefs in Research and Innovation Governance. Springer, Cham. https://doi.org/10.1007/978-3-030-69978-9_4
