# Unity Weekly Exit Ticket

## Week 2 Part 1

This is part of the Medium Stake Assignments and **to Complete this Assignment** you need to follow the instructions listed below. I am using two paid assets that we shouldn't distribute and/or use outside of this classroom setting. They are both from the AK Studio Art group: [Art Gallery V2](https://assetstore.unity.com/packages/3d/environments/art-gallery-vol-2-230780) and [Art Gallery Museum VR](https://assetstore.unity.com/packages/3d/environments/art-gallery-museum-vr-230478). These have some larger files and thus I will be using [Git LFS](https://git-lfs.com/) for this project setup.

***

<div style="page-break-after: always;"></div>

### Assignment Instructions

By being part of the GitHub Team Under the Game Design Program you can directly access this various GitHub projects I'm going to be opening up for you all. For this weeks assignment we're going to utilize a single Unity project that is already 'ready' for you. You can find that project on our Game-Design-ODU organization [under the following repository: 'UG395_2024_Week2'](https://github.com/Game-Design-ODU/UG395_2024_Week2).

1. Using GitHub Desktop: Clone the repository on your computer.

<Image>
<a name=""></a>
<img src="OpenRepoViaGitHubDesktopLink.PNG" alt="" title="" class="centerlrg"/>
</Image>

***

<div style="page-break-after: always;"></div>

2. Using GitHub Desktop: Create a new branch from 'developer' and follow naming conventions for your name 'FirstCharacterFirstName'+'_'+'LastNameFull'. For example, mine would look like **'J_Shull'**

<Image>
<a name=""></a>
<img src="GitHubDesktopNewBranch.PNG" alt="" title="" class="centerlrg"/>
</Image>

>Make Sure It's from Developer
><Image>
<a name=""></a>
<img src="GitHubDesktopNewBranchFromDeveloper.PNG" alt="" title="" class="centerlrg"/>
</Image>

***

<div style="page-break-after: always;"></div>

3. Confirm that you have made a new branch and that you see it 'active' in GitHub Desktop. You can close GitHub desktop for the time being.

<Image>
<a name=""></a>
<img src="GitHubDesktopNewBranchName.PNG" alt="" title="" class="centerlrg"/>
</Image>

***

<div style="page-break-after: always;"></div>

4. Using Unity Hub: Locate the Unity project by adding it to the Hub.

>When you Open Unity Hub you will need to 'Add Project From Disk
><Image><img src="UnityHubAddProjectFromDisk.PNG" class="centerlrg"/></Image>
>Make sure you navigate to where you see the Assets folder
><Image><img src="UnityBrowseToProject.PNG" class="centerlrg"/></Image>
>It will now be available in the Hub, confirm the editor version, select, & open it!**
><Image><img src="UnityHubOpenProject.PNG" class="centerlrg"/></Image>
>This will take a few minutes to open for the first time (depends upon your machine-CPU & Ram). It will be significantly faster the next time you open it.
><Image><img src="OpeningProjectTime.PNG" class="centersml"/></Image>

***

<div style="page-break-after: always;"></div>

#### Make a Scene Copy

5. Once in the Editor: Open the project in Unity and navigate to the "G395/WK2_PrefabScene.unity" and open it up, make a copy and save it with the same naming conventions.

><Image><img src="UnityFileSaveAsName.PNG" class="centerlrg"/></Image>
>because Unity and managing scenes across a git repository can be a bit of a pain in Unity, you need to immediately save this scene with a different name, go to File --> Save As--> 'FirstCharacterFirstName+"_"+FullLastName and save it in the 'G395/StudentScenes/' folder, see mine above for an example.
***

<div style="page-break-after: always;"></div>

6. Confirm that you've saved your scene (look up in the top toolbar to make sure you are in fact in your scene name) and now explore the scene.

<Image><img src="UnityFileSaveConfirm.PNG" class="centerlrg"/></Image>

7. You should see a simple museum layout, find your name in the museum: there are two locations to find, you should have a display case and an image on the wall. Pay attention to the coordinate information in the Unity Component Menu. You're going to need these later. You will be modifying the item in the display case and the image on the wall.

***

<div style="page-break-after: always;"></div>

#### 3D Importing Instructions from Asset Store

8. Login to [Unity](https://unity.com) and navigate to the [Unity Asset Store](https://assetstore.unity.com/). Find a free asset. Go through the 'purchase' of that free asset and using the package manager import that asset into the project. If you have Unity open while you're online at the asset store you will see a prompt to import that into Unity, if not, you can come back to Unity and add the asset via the Package Manager.

<Image><img src="AssetStoreFree.PNG" class="centerlrg"/></Image>

>Now add it to your assets (you need to make sure you're logged in to Unity! upper right corner)
><Image><img src="AssetStore_Confirm_AddToAssets.PNG" class="centerlrg"/></Image>
>You should see an option pop up at the top to open in Unity
><Image><img src="AssetStoreOpenInUnity.PNG" class="centerlrg"/></Image>
>Download the assets
><Image><img src="AssetStore_PackageManager.PNG" class="centerlrg"/></Image>
>Import the assets
><Image><img src="AssetStore_Import.PNG" class="centerlrg"/></Image>

<div style="page-break-after: always;"></div>

>Unity Pop up for what you're about to Import
><Image><img src="ConfirmImport.PNG" class="centerlrg"/></Image>
>Locate it in the Project Hierarchy Tab
><Image><img src="AssetInProject.PNG" class="centerlrg"/></Image>

<div style="page-break-after: always;"></div>

> Test the assets drag one into the scene to confirm that it's "okay"
><Image><img src="PinkAsset.PNG" class="centerlrg"/></Image>
> Fixing Materials: if you need to fix your materials because things are pink, select your GameObject and look for the 'MeshRenderer' component. On this component you will find your 'Material' option, you may need to expand this arrow to see the materials. Once you see the materials, double click on the first one and will bring you to the actual material data in the Project Tab. With that material selected navigate to the 'Edit-->Rendering-->Materials-->'Convert selected for...' this should now take your old or standard rendering materials and convert them to URP and hopefully no longer be pink!
>
>Find the Material on the asset
><Image><img src="FindMaterial.PNG" class="centerlrg"/></Image>

<div style="page-break-after: always;"></div>

>Select the material and convert it to URP
><Image><img src="ConvertMaterials.PNG" class="centerlrg"/></Image>
>Fixed Asset?
><Image><img src="ConvertedMaterials.PNG" class="centerlrg"/></Image>

9. Make sure to stage your display case just how you want it - don't move the case, but add your item inside it, and make sure your 3D asset 'fits' *Adjust the scale uniformly!* when you're done with this make sure to save your scene!

***

<div style="page-break-after: always;"></div>

#### 2D Importing Instructions from Dalle/AI service

10. In similar fashion we need to get a 2D image into Unity but instead of using the asset store lets use an AI service to generate us an image. Lets use Dalle or any AI service (Stable Diffusion?) to create whatever image you want. Download the image and move the image into the Unity Project and save it under the "StudentImages" folder. Make sure you retain the text for the image prompt as we will need this later.

> StudentImages is located in the Assets/G395/StudentImages/ move your image in here just like you would any other file using the Windows file system. Make sure you use similar naming conventions with your name +"_" +last name+"Description": for example mine is 'J_Shull_SnailPower.PNG'. Come back into Unity and find the image.

11. You will need to make sure that the image is in the 'correct format' to be used in a material. We need our image to be what's called a 'Texture' or 'Texture2D'. We also might need to modify this image with other image software to correctly align our UVs (will talk more about this in class) so don't worry if it doesn't align exactly and for those who want to make sure it aligns the current image mesh UV setup has a large white space at the bottom, so as long as you put your image in the top 60% or so you should be good to get it to fit - you can also find the blank image template in the Unity folder as a guide or frame of reference. That item is located in the Assets/StudentImages/UV_Blank_ForImageProcessing-01.png

>My Example Replacement done in Illustrator
><Image><img src="ImageReplacementNormal.PNG" class="centerlrg"/></Image>

***

<div style="page-break-after: always;"></div>

12. Once you have your image in the Unity project you need to then update your material for your picture. Select the picture in the world that has your name on it, navigate down to the correct gameobject that represents the image, find the mesh renderer component, navigate to the material, and replace the texture part of the material with the texture you just created.

>Select the Material from the Mesh Renderer
><Image><img src="MaterialTextureUpdate_p1.PNG" class="centerlrg"/></Image>
>Click the Texture Icon Square**
><Image><img src="MaterialTextureUpdate_p2.PNG" class="centerlrg"/></Image>

<div style="page-break-after: always;"></div>

>Find your new image you brought in
><Image><img src="MaterialTextureUpdate_p3.PNG" class="centerlrg"/></Image>

***

<div style="page-break-after: always;"></div>

#### Documentation Instructions

13. Navigate the project repository and in the 'Documentation' Folder you will find a markdown file named "SceneSettings.md".

* Add a level 3 sub-header under the level 2 header named "Student Display Cases".
* Name is your header your name. Under this named level 3 sub-header there needs to be six pieces of information in a list form, please use the '*' for your list.
* the **first** item in the list: needs to be the 3D display case local coordinate in a Vector3 format using commas to separate. You can find this coordinate back on the parent item of your display case relative to the location.
* the **second** item in the list needs to be the Link to the Unity Asset you decided to use
* the **third** needs to be an explanation of what your grid represents and why you picked that asset. Keep it to under 2-3 sentences.
* the **fourth** item needs to be 2D image local coordinate in a Vector3 format using commas to separate. This is the coordinate of your 2D image location on the wall relative the location.
* the **fifth** item needs to contain the service you used, then a colon, and the text prompt you used to generate the image.
* the **sixth** item needs to be the image name including the type.
  * For example your list might look like this:
  * 0.01, 5.00, 0.05
  * [Animals](https://assetstore.unity.com/packages/3d/characters/animals/animals-free-260727)
  * I decided to place a penguin in my grid because growing up, for whatever reason, my mom just loved penguins. Sometime later she had the opportunity to go visit some in Antarctica and when she came back she told me she had never smelled anything like it, a million penguins all pooping in a relatively small area. I think that was the last time she really said she liked penguins.
  * 0.02, 3.00, 2.00
  * OpenAI DALLE: *"I need to create an image of a watercolor scene in the style of anime 2D illustration. The image needs to depict a post apocalyptical scene where all humans are gone and only the snails have survived. The snails are larger and are advanced, wearing armor and have communication devices attached to their helmets and shells. High Quality. Studio. Vibrant."*
  * 'J_Shull_SnailPower.PNG'

14. At this point save the markdown file, commit your changes, and push those changes to GitHub.
15. Make sure you have all changes pushed and synced before the next part! Navigate to the repository online: and open up a pull request. You want to make sure that you're requesting your branch to be pulled into 'developer'. While you're doing this, look for the reviewer category and **importantly** add me as a reviewer 'request a reviewer'. When you do this you should end up with a link for that pull request with review, please include that link in your submission for this assignment.
