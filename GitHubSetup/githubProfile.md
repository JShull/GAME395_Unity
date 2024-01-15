# Instructions on Setting up your GitHub Profile

There are a lot of ways you can do this! Conceptually it's just the following:

> 1.) Create New Repository
>
> 2.) Include a 'readme.md' file in the root of this repository
>
> 3.) Sync with GitHub and name the repository to match your user handle
>
> *thats it!*

Now how you do that above is really up to you. 

## The GitHub Way

If you follow the online [GitHub documentation](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme), they have 7 steps, and it's all done online via GitHub.com through their interface and is the easiest way to do this without needing to have any software installed as it's all 'on the web'. 

## How we did this in class

In class we started from the local machine, created a local repository, added a local 'readme.md' file, opened up GitHub client, added that repository to our GitHub client, then published it and upon publishing it we named the repository our user handle.

- 1.) Navigate on your computer to a folder where you want to save your repository, in class I made a new folder on my main drive, named it GitHub, then made another folder inside it and named it after my handle - 'JShull' with the directory now looking like this--> C:\GitHub\JShull 
- 2.) While in this folder I then right clicked, and looked for 'Open Git Bash Here'
  - If this isn't an option, you can navigate to the folder using the command line tool, in my case I would open up command prompt and type;

```bash
        #type
        cd C:\GitHub\JShull
        #hit enter
```

- 3.) Assuming we are in Git Bash: In Git Bash: I typed 'git init'
  - If you're using the command prompt as mentioned above, you can do the same thing 'git init' and hit enter.
  - No matter which way we got to git, we have now initialized the repository in my C:\GitHub\JShull folder

```bash
        #type
        git init
        #hit enter
```

- 4.) I opened up VSCode and then File-->"Open Folder..." and selected my C:\GitHub\JShull folder.
  - At this point it's pretty empty so lets create our readme.md file
- 5.) In VSCode I clicked the 'New File Icon' and named it 'readme.md'
  - ![new file Icon](newFileVSCode.png)
  - In this new file I put a few things following the [markdown guide](https://www.markdownguide.org/) and saved it.
- 6.) I then opened up GitHub Desktop on my computer and now want to reference the work we just did by 'adding an existing repository' because up until this point GitHub desktop doesn't *know* about this local repository (yet)
  - ![GitHub Add Local Repository](githubDesktopAddLocal.png)
  - Click the up/down arrow as outlined in red above
  - ![GitHub Add Local Repository 2nd Step](githubDesktopAddLocalStepTwo.png)
  - Click the 'Add' button as outlined in red above
- 7.) At this point GitHub now should be showing you your repository and you might have some changes that still need to be 'committed' go ahead and do that now and then publish it.
  - ![GitHub Commit](gitHubCommit.png)
  - When you publish it, make sure you select where you want to publish it - in our case we want it to be public and this is where **very importantly** you name the repository your handle name.
  - ![GitHub Publish](gitHubPublish.png)

***
<div style="page-break-after: always;"></div>

## Git to GitHub

A quick video after I've already 'git init' via the git bash tool. I'm going to now open that folder in VSCode and create a readme.md file, save it, and then open/add the repository to GitHub. From here I will make a commit and push/publish this. Same as before **very importantly** make sure to name it with GitHub your handle name.
<video src="vsCode_GitHub.mp4" controls="controls" style="max-width: 1920px;"></video>

***
<div style="page-break-after: always;"></div>

## Exporting to PDF

If you wanted to export a markdown file to a PDF file you can utilize the VSCode plugin feature to do this. You're going to want to find a [Markdown to pdf plugin like this one.](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

- Make sure you're able to install it and confirm that's installed before proceeding - you might need to restart VSCode
- You then can access the plugin's settings via the plugin icon, and navigate to the 'Markdown to PDF' Plugin
- ![VSCode Plugin Step 1 after install](./VSCodePluginStep1.PNG)
- From here you can now view the settings for the plugin and/or other options like how to 'export'
- ![VSCode Plugin Step 2 after you've clicked usage](./VSCodePluginStep2.PNG)
- Now that you know what the hot keys are 'CTRL+SHIFT+P' you can go back to your markdown document, open the document in VSCode and use the hot key to bring up the plugin options!
- ![VSCode Plugin Step 3 export!](./VSCodePluginStep3.PNG)
