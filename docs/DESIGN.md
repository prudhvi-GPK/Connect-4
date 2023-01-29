## Comp841 Practical AI

### Project DESIGN

**Teammates: Prudhvi & Vijay** 

**Platform - GitHub** 

### Project Name: Connect 4 AI bot

## Introduction

**What AI system are you interested in investigating further and why?**

A) The AI system that I am interested in is a game called Connect 4. It is sequential two player game in which the objective is to
create a line of four of your own discs that runs horizontally, vertically, or diagonally before your opponent. In General, all these
board games like Chess, Go, Checkers etc.

**Why is it of interest to you?**

A) I am interested in AI board games because they are easy to understand, take one step
at a time and can be easily implemented by AI modules. I can gain more hands-on experience on search algorithms by this
project.

**What specifically you'll focus on? What's the overall guiding question your study will pursue?**

A) We are focusing on building an AI that can beat humans in Connect 4 game.The overall guiding question is how to find the best possible move to complete the game.

**Lead Author:** Vijay, **Reviewer:** Prudhvi

## Theoretical Background

**What areas or fields of AI provide the theoretical framework of the AI system?**

A) This Connect-4 board game uses Search algorithm (Depth first Search) to find the best possible node in a decision tree.

**What are the key concepts and techniques that the AI system is based on?**

A) The system uses Minmax algorithm which is recursive and used for decision-making in AI games. It performs a DFS (depth-first search) algorithm for the exploration of the complete game tree so, proceeds all the way down to the terminal node of the tree, then backtracks the tree as the recursion. Then we implement Alpha-beta pruning strategy to improve the computational speed and save memory. The Alpha-beta pruning to a standard minimax algorithm yields the same move as the regular approach, but it eliminates all the nodes that are slowing down the algorithm.

**Include appropriate references that describe the field, key concepts, and technique**

- https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f
- https://www.educative.io/answers/the-minimax-algorithm

**Lead Author:** Vijay, **Reviewer:** Prudhvi

## Development Approach

**What tools, platforms, APIs, libraries?**

- Python IDE – PyCharm.
- For version control and collaboration – GitHub.
- Interpreter – python 3.10
- Libraries – NumPy, pygame, sys, math and random.
- Reasoning - Minmax Algorithm, Alpha-beta pruning.

**Lead Author:** Prudhvi, **Reviewer:** Vijay

## Working Example

**What example is a technically sound illustration of the AI system?**

A) This can be best explained by a decision tree. Connect 4 is a matrix of 6*7. When the game begins, the first player gets to choose one column among seven to place the colored disc. There are 7 columns in total, so there are 7 branches of a decisiontree each time. After the first player makes a move, the second player could choose one column out of seven, continuing from the first player’s choice of the decision tree. Finally, if any player makes 4 in a row, the decision tree stops, and the game ends.

**Lead Author:** Prudhvi, **Reviewer:** Vijay

## Discussion and Evaluation

**What are the considerations for developing a safe and trustworthy AI system?**

A) AI system should be lawful, ethically adherent, and technically robust. It is based on the idea that AI will reach its full potential
when trust can be established in each stage of its lifecycle, from design to development, deployment, and use.

**What are the ethical considerations in determining the legitimate use of the AI system?**

A) Four major ethical issues must be addressed: (1) informed consent to use data, (2) safety and transparency, (3) algorithmic
fairness and biases, and (4) data privacy are all crucial factors to consider.

**Lead Author:** Prudhvi, **Reviewer:** Vijay
