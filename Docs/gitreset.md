# QUICK TUTORIAL ON MANUAL RESET / NEW REPOSITORY

* Let's say you messed up something and/or you've been tracking the wrong files for a *while*
* There are lots of way's to fix this, but sometimes it's easier just to do a hard reset
* These steps below will help you do a hard reset and rehost your repository with your current work and remove all of the previous history (basically this is a new repository with nothing connecting it back to the old one)

## MAKE SURE YOU'RE ON THE CORRECT BRANCH

* Whatever you do - make sure you're on the branch you want to KEEP!
* Navigate to GitHub Desktop and confirm you're on the right branch!

## STEPS TO RESET

* For example purposes we are going to use Ryan F. project, thanks Ryan F!

### STEP 1 DELETE OLD REPOSITORY

* Go to your Root repository Windows folder
* ![Root Windows](./Images/gitReset/MicrosoftTeams-image%20(6).png)
* Do you see this .git folder?
  * Yes = proceed
  * No? = Go to View-->Show-->Hidden Items needs to be checked
* Delete this .git folder
* ![Delete GIT](./Images/gitReset/MicrosoftTeams-image%20(7).png)

### STEP 2 CLEAR GITHUB HISTORY, GIT & GIT LFS SETUP

* Now go to GitHub Desktop and it's going to prompt you about this work you just deleted - BE CAREFUL HERE
* ![Reset GitHub Desktop](./Images/gitReset/MicrosoftTeams-image%20(8).png)
* HIT REMOVE!
* Let's make sure our GIT LFS .gitattributes file is correct!
  * In your root folder look for a file named '.gitattributes' or 'gitattributes.md' if you see it as the '*.md' format we need to change it.
    * ![LFS Attributes not right](./Images/gitReset/gitlfsSetup_00.png)
    * Remove the .md at the end and type '.gitattributes' this should change your file format to be something that Git LFS now understands.
    * ![LFS Attributes is now right](./Images/gitReset/gitlfsSetup_01.png)
* Now while we are here, in your Windows Folder where your work is at, right click and look for 'Git Bash Here' you might have it under more options and/or you might not have it.
* IF YOU DON'T SEE GIT BASH in your right click menu follow these steps, if you do **ignore these steps**.
  * If you don't have it there, hit the windows button and type 'git bash', then open it up.
    * You need to manually navigate to your folder.
    * Depending upon where you're saving your projects, if you set up your GitHub folder like I suggest (in your C: drive), you can just type 'ls' in this Git Bash terminal to see all of the current folders
    * ![Reset GitHub Desktop P2](./Images/gitReset/gitCommand_00.png)
    * For me, my root GitHub is under my C drive so I just type 'cd c:/GitHub' without the ''
    * Now you can type ls to see all the folders/files here
    * ![Reset GitHub Desktop P2](./Images/gitReset/gitCommand_01.png)
    * I have my current project folder under Spring2023/_RFeldman_33915 so I'm going to navigate to there via the command line
    * ![Reset GitHub Desktop P2](./Images/gitReset/gitCommand_02.png)
* You Had Get Bash Here or you followed along.
  * Command Terminal pops up and we need to type a couple things in but lets make sure we have our LFS setup
* ![ready to Init git](./Images/gitReset/MicrosoftTeams-image%20(9).png)
* type 'git init'
  * This will now setup this folder to be 'git tracked'
  * ![Git Init](./Images/gitReset/MicrosoftTeams-image%20(10).png)
* now LFS Setup
  * type 'git lfs install'
    * ![Git lfs install](./Images/gitReset/MicrosoftTeams-image%20(12).png)
* You are now ready locally with git and git lfs so we need to head back to GitHub Desktop.

### STEP 3 GITHUB DESKTOP PUBLISH

* Now in GitHub Desktop we need to tell GitHub desktop that we have a new local repository
* ![GitHub Desktop Setup 0](./Images/gitReset/MicrosoftTeams-image%20(13).png)
  * Navigate to where you have your current folder setup at
* ![GitHub Desktop Setup 1](./Images/gitReset/MicrosoftTeams-image%20(14).png)
  * When you select this it should pop up with an option for Git LFS initialization - do this!
  * ![GitHub Desktop Setup 2](./Images/gitReset/MicrosoftTeams-image%20(15).png)
* Go ahead and do your local commit in the bottom left of GitHub Desktop
* Upon that finishing (might take a few minutes) you're ready to publish to GitHub Desktop. Depending upon where you're hosting if under our game organization or your own private setup you can select that information now when you tell GitHub Desktop to Publish
* ![GitHub Desktop Setup 3](./Images/gitReset/MicrosoftTeams-image%20(16).png)
* ![GitHub Desktop Setup 4](./Images/gitReset/MicrosoftTeams-image%20(17).png)
* Just make sure you don't name it the same exact name as your other repository - that way you have a backup of your old work that you're resetting and this new repository of those fixes. In the example I just removed the underscore from _RFeldman_33915 and now its named 'RFeldman_33915'
* ![GitHub Desktop Setup 5](./Images/gitReset/MicrosoftTeams-image%20(18).png)
* Hit Publish!
