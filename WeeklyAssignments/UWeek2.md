# Unity Weekly Exit Ticket

## Week 2 Part 1

This is part of the Medium Stake Assignments and **to Complete this Assignment** you need to follow the instructions listed below.

### Assignment Instructions

By being part of the GitHub Team Under the Game Design Program you can directly access this various GitHub projects I'm going to be opening up for you all. For this weeks assignment we're going to utilize a single Unity project that is already 'ready' for you. You can find that project here.

1. Using GitHub Desktop: Clone the repository on your computer.
2. Using GitHub Desktop: Create a new branch from 'developer' and follow naming conventions for your name 'FirstCharacterFirstName'+'_'+'LastNameFull'. For example, mine would look like **'J_Shull'**
3. Confirm that you have made a new branch and that you see it 'active' in GitHub Desktop. You can close GitHub desktop for the time being.
4. Using Unity Hub: Locate the Unity project by adding it to the Hub. Open the project in Unity and navigate to the "scene named" and open it up, make a copy and save it.

    > because Unity and managing scenes across a git repository can be a bit of a pain in Unity, you need to immediately save this scene with a different name, go to File --> Save As--> 'FirstCharacterFirstName+"_"+FullLastName and save it in the 'Scenes' folder.

5. Confirm that you've saved your scene (look up in the top toolbar to make sure you are in fact in your scene name) and now explore the scene.
6. You should see a sort of grid layout, find your name in the grid and pay attention to the coordinate information next to your name - you're going to need this later. In this region is where you're going to perform the next set of steps.
7. Login to [Unity](https://unity.com) and navigate to the [Unity Asset Store](https://assetstore.unity.com/). Find a free asset. Go through the 'purchase' of that free asset and using the package manager import that asset into the project. If you have Unity open while you're online at the asset store you will see a prompt to import that into Unity, if not, you can come back to Unity and add the asset via the Package Manager.
8. Use the area defined for you to your advantage and make sure to import and display whatever asset you found. Note: if you're asset is bright pink it's probably because you found an asset that wasn't **URP** as the project is using the URP graphics pipeline. Please follow these instructions to fix your materials.

    > Fixing Materials: if you need to fix your materials because things are pink, select your GameObject and look for the 'MeshRenderer' component. On this component you will find your 'Material' option, you may need to expand this arrow to see the materials. Once you see the materials, double click on the first one and will bring you to the actual material data in the Project Tab. With that material selected navigate to the 'Edit-->Rendering-->Materials-->'Convert selected for...' this should now take your old or standard rendering materials and convert them to URP and hopefully no longer be pink!

9. (Optional) If you have other content that you want to contribute that is your own, feel free to add custom pieces but the assignment requires at least one free asset to be added to the project. No code. Just 2D or 3D in world assets.
10. Make sure to stage your grid area just how you want it, save your scene and put Unity aside (don't close it)
11. Navigate the project repository and in the 'Documentation' Folder you will find a markdown file named "SceneSettings.md".
  
    * Add a level 3 sub-header under the level 2 header named "Student Grid".
    * Name your header your name. Under this named level 3 sub-header there needs to be three pieces of information in a list form, please use the '*' for your list.
    * The **first** item in the list: need the coordinate space of your grid in a Vector3 format using commas to separate. You can find this coordinate back in the scene where you found your name.
    * The **second** item in the list needs to be the Link to the Unity Asset you decided to use
    * the **third** needs to be an explanation of what your grid represents and why you picked that asset. Keep it to under 2-3 sentences. For example your list might look like this:
      * 0.01, 5.00, 0.05
      * [Animals](https://assetstore.unity.com/packages/3d/characters/animals/animals-free-260727)
      * I decided to place a penguin in my grid because growing up, for whatever reason, my mom just loved penguins. Sometime later she had the opportunity to go visit some in Antarctica and when she came back she told me she had never smelled anything like it, a million penguins all pooping in a relatively small area. I think that was the last time she really said she liked penguins.

12. At this point save the markdown file, commit your changes, and push those changes to GitHub.
13. Make sure you have all changes pushed and synced before the next part! Navigate to the repository online: and open up a pull request. You want to make sure that you're requesting your branch to be pulled into 'developer'. While you're doing this, look for the reviewer category and **importantly** add me as a reviewer 'request a reviewer'. When you do this you should end up with a link for that pull request with review, please include that link in your submission for this assignment.
