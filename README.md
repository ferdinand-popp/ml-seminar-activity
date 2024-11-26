# Machine Learning Seminar Activity
### Introduction: 
For the Machine Learning Seminar, we will provide an optional activity for you to complete while the course is ongoing. This activity could theoretically be completed by those of all coding backgrounds and will be available in both Python and R. Within this activity, we will provide 3 real-life bioinformatics-based datasets (1 for classification and 2 for regression) where you will be able to learn how to go through the entire machine learning pipeline of cleaning/preprocessing your data, performing exploratory data analysis, splitting your data into training/testing sets, choosing your model(s),  training your model(s), predicting on the test set, choosing the correct metric to use, and, most importantly, explaining what your results mean. 

As a guide, there will be short coding snippets and guided questions to help push you in the right direction if you’re stuck along with links to online resources if you are in need of more assistance. Additionally, we plan to have discussions on Discord and short discussion after the lectures on wednesdays, where students can meet/discuss in person and where members of the Division of Applied Bioinformatics will be available for individual help.

At the end of the Machine Learning Seminar, we are also planning a final meeting (date, location and time TBA)  where those students who have participated will come to talk about their results, what they liked, what they found difficult, and most importantly discuss with their classmates why certain methods worked/did not work. No presentation will be required and we envision this to be a more open discussion rather than an actual presentation. We highly encourage all participants to come to this!

### Goal:
With this activity, our goals are the following:
- Implement the machine learning algorithms (i.e. linear regression, logistic regression, neural networks, etc.) that you have learned throughout the seminar using either Python and/or R
- Use real bioinformatics-based datasets to perform your analysis
- Perform an entire machine learning analysis starting from having only data available all the way to presenting your results in a clear and concise manner
- Collaborate with other students to see what works and/or does not work

### Contact person on Discord :
- Ferdinand Popp (PhD Student): Python
- Julia Münch (PhD Student): R
- Dr. Lars Feuerbach (Group Leader): Organizational

# Getting Started
Before doing any work, it's extremely common for machine learning engineers, data scientists, and bioinformaticians to use some type of version control. Without getting into too much details, it's a way for users to "load in" someone's previous coding repository so that they can make changes or use it as a default starting point. In our case, we will be using GitHub but there are other alternatives such as GitLab, Bitbucket, Google Cloud Source Repositories, and AWS CodeCommit but thankfully, they all work the same way. If you are unaware of what version control does, feel free to watch this video: https://www.youtube.com/watch?v=USjZcfj8yxE&ab_channel=ColtSteele

### Downloading Git
If you do not yet have Git installed, follow the directions to do so here: https://git-scm.com/downloads

### Cloning the Repository
Now, open your terminal in your respective operating system and ensure that git is properly installed by typing:

`git --help`

Different git options should be displayed such as `clone`, `init`, `add`, `merge`, etc.

Now, navigate to the proper location in your computer that you want to save your work in (i.e. /Desktop/) and clone (or load in/copy) this current repository that we have by inputting the following command:

`git clone https://github.com/ferdinand-popp/ml-seminar-activity.git`

If everything works properly, a new folder should be created in the location where you want to save your work and this folder should be called `ml-seminar-activity`. Ensure that this is the case before proceeding!

### Option 1: Using Python / Jupyter Notebooks
If you'd like to continue doing this activity using Python, ensure that you have both Python 3.xx, pip and Jupyter Notebook installed. Before starting the installation process, `pip` is a way to programatically download the different ML libraries that we'll be using using such as Pandas, NumPy, SciKit Learn and Keras/Tensorflow. On the other hand, `Jupyter Notebooks` are a common way to run Python commands in a code-block fashion. Luckily, `Jupyter Notebook` can be installed via `pip`.

`pip` is by default installed next to python for most versions. If not: To download `pip`, follow the directions here: https://www.geeksforgeeks.org/download-and-install-pip-latest-version/

Once this is downloaded properly, install `Jupyter Notebooks` by inputting the following command into your terminal/command line:

`pip install notebook`

After this step is complete and within your terminal/command line, navigate to where this repository is saved and type in `jupyter notebook`. If all things work out properly, a new window will pop up. Within this window, click and open the file that ends in the common jupyter notebook file ending `.ipynb` and follow the directions.


### Option 2: Using R / R Markdown Files
On the other hand, if you'd like to continue doing this activity using R, ensure that you have R installed first: https://cran.r-project.org
and foremost and an IDE such as R-Studio: https://www.rstudio.com/products/rstudio/download. 
First create a new project. When using R, to download different packages, you could download them using the command `install.packages()`. Rather than having an R script, a more interactive way to display your code along with comments/images is through the use of R Markdown files. If using R-Studio, R Markdown files can be loaded in directly or if you'd like to create your own, you can go to `New File > R Markdown`. In order to properly view your document in a common form such as HTML or PDF, you can knit your Markdown file to html or PDF, which creates the file in the chosen format and saves this to your local machine.


# Datasets
In order to download the datasets, unfortunately GitHub is not the greatest way to store data and therefore we have data for you to play around with in a Google Drive. The access link is shared via Discord.


