## Comp841 Practical AI
### Project Proposal 

**Teammates: Prudhvi & Vijay** 

**Platform - GitHub** 

**Opensource code for project:Open source**

### Project Name: Connect 4 AI bot

**1. What AI system are you interested in investigating further and why ?** 

The AI system that I am interested in is a game called Connect 4.It is sequential two player game in which the objective is to
create a line of four of your own discs that runs horizontally, vertically, or diagonally before your opponent.In General, all these
board games like Chess, Go, Checkers etc. use search algorithms and, in this case, it uses ‘minmax’ algorithm which is an
example for Depth-First search technique. I am interested in AI board games because they are easy to understand, take one step
at a time and can be easily implemented by AI modules. I can gain more hands-on experience on search algorithms by this
project.

**Lead Author:** Prudhvi, **Reviewer:** Vijay


**2. What content knowledge (theories and concepts) does the AI system use?**
The system uses Minmax algorithm which is recursive and used in decision-making in AI games. It performs a DFS (depth-first
search) algorithm for the exploration of the complete game tree so, proceeds all the way down to the terminal node of the tree,
then backtracks the tree as the recursion. Then we implement Alpha-beta pruning strategy to improve the computational speed
and save memory. The Alpha-beta pruning to a standard minimax algorithm yields the same move as the regular approach, but it
eliminates all the nodes that are slowing down the algorithm.

**Lead Author:** Prudhvi, **Reviewer:** Vijay

**3. What tools, platforms, and APIs are needed to develop the AI system?**

The tools that are needed to develop this system are
- Python IDE – PyCharm.
- For version control and collaboration – GitHub.
- Interpreter – python 3.10
- Modules – NumPy, pygame, sys, math and random.

**Lead Author:** Prudhvi, **Reviewer:** Vijay

**4.What example illustrates the basic "ingredients" of the AI system?**
A) This can be best explained by a decision tree. Connect 4 is a matrix of 6*7. When the game begins, the first player gets to
choose one column among seven to place the colored disc. There are 7 columns in total, so there are 7 branches of a decision
tree each time. After the first player makes a move, the second player could choose one column out of seven, continuing from
the first player’s choice of the decision tree. Finally, if any player makes 4 in a row, the decision tree stops, and the game ends.[2]

**Lead Author:** Prudhvi, **Reviewer:** Vijay

**5.What are the considerations for developing a safe and trustworthy AI system?**
A) AI system should be lawful, ethically adherent, and technically robust. It is based on the idea that AI will reach its full potential
when trust can be established in each stage of its lifecycle, from design to development, deployment, and use.[1]

**Lead Author:** Prudhvi, **Reviewer:** Vijay

**6.What are the ethical considerations in determining the legitimate use of the AI system?**
A) Four major ethical issues must be addressed: (1) informed consent to use data, (2) safety and transparency, (3) algorithmic
fairness and biases, and (4) data privacy are all crucial factors to consider.[3]

**Lead Author:** Prudhvi, **Reviewer:** Vijay

**References:**

[1].“Building trustworthy AI is key for enterprises” by Ronald Schmelzer
https://www.techtarget.com/searchenterpriseai/feature/Building-trustworthy-AI-is-key-for-enterprises.

[2]https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained3b5fc32e4a4f.

[3]Stahl, B.C. (2021). Ethical Issues of AI. In: Artificial Intelligence for a Better Future. SpringerBriefs in Research and
Innovation Governance. Springer, Cham. https://doi.org/10.1007/978-3-030-69978-9_4


