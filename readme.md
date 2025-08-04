![When cats rule the utopian Japanese City of Tokyo](./Images/DALLE/Spring2024.png)

# Game 395 Unity3D and Software Development

If you have any questions please reach me on ~~[ODU Microsoft Teams](https://teams.microsoft.com/l/chat/0/0?users=jshull@odu.edu)~~ and you can schedule time via my office hours through ~~[ODU's Microsoft Booking](https://outlook.office.com/bookwithme/user/a264cdcc1bda4ce4884e4b052b89bdc3@odu.edu/meetingtype/RDiapeLfhkq1XJ5topb6_g2?anonymous)~~ just make sure to select the option for the Game Design Class.

## Course Description

GAME 395: Designing and Developing with the Unity Engine or as **[Dr. Moberly](https://www.odu.edu/directory/people/k/kmoberly)** calls it *'Unity Zero to Hero'*. This class will take a Systems Engineering approach into how you can use real-time simulation systems aka ‘Game Engines’ to rapid prototype, create, build, compile, and deploy functioning software across major hardware and operating systems. We will primarily be utilizing Unity3D for the class and we might explore Godot as well. We will focus in on four key areas: Version Control, Unity, 'The Observer Pattern', and the 'Humble Pattern'. We will work through the Unity Package Management system so you can make your own Unity Package(s). The class will focus on one core project that students will have to **[mod](https://en.wikipedia.org/wiki/Video_game_modding)**. Upon modding the game you will then be required to deploy it across either Windows, Linux, Mac, Android, or iOS.

## Class Quick Links

* [Syllabus PDF](./Docs/Syllabus.pdf)
  * [Syllabus Markdown](./Docs/Syllabus.md)
* [Canvas](https://canvas.odu.edu/courses/154469)
* [Video About Me](https://youtu.be/F-wHUHyhsLw)
* [MarkdownGuide.org](https://www.markdownguide.org/)
* [Unity Scene Navigation Cheat Sheet](./UnityEssentials/_Shortcuts-Cheat_Sheet.txt)

### Software Links

The links and resources below are primarily the software we will be using in class for assignments and the project work.

#### Version Control

If you're setting up a Windows machine to go along with the class please download and install these in the order they are provided.

* [Git Download Windows](https://git-scm.com/download/win)
* [Git Large File Storage-GitLFS](https://git-lfs.com/)
* [GitHub Desktop Download](https://desktop.github.com/)
  * After you provide your GitHub handle you will be able to [join the Game Design GitHub](https://github.com/Game-Design-ODU)
* [Git Documentation Link](https://git-scm.com/docs)

#### Unity

* [Unity Account ID Setup](https://id.unity.com/en/conversations/81585787-95d9-4532-9429-8dc13dc2939f019f)
* [Unity Hub Download Windows](https://unity.com/download)
* [Unity GitIgnore Template](https://github.com/github/gitignore/blob/main/Unity.gitignore)

#### IDE / Tools

* [VSCode](https://code.visualstudio.com/download)
* [Visual Studio Community 2022](https://visualstudio.microsoft.com/downloads/)
* For Personal Windows PC: [Enable Long File Paths](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/The-Windows-10-default-path-length-limitation-MAX-PATH-is-256-characters.html)

#### Content Creation Software

Below will be an evolving list of links for various mobile/PC based applications to help create content via modern technology.

* [Reality Scan](https://www.unrealengine.com/en-US/blog/realityscan-is-now-free-to-download-on-ios) Only for iOS but Android is coming - one of the best mobile 3D capture applications on the market and it's 'Free'
* [Luma AI](https://lumalabs.ai/) can upload videos to their site and get 3D surface models, use your mobile phone to capture items/objects, similar to reality scan but uses a slightly different approach to capturing your item
* [Unity AR Companion App](https://blog.unity.com/technology/the-ar-companion-app-is-now-available) Unity provides an AR tool that lets you capture content - works on both Android and iOS devices.
* [Meshroom](https://alicevision.org/#meshroom) little more advanced PC software that is open source and free - creates impressive point cloud data files from multiple sensors/devices and reconstructs a surface mesh. Don't need a high end GPU - but you're going to want to use one. Supported on Windows/Linux
* [Move.AI](https://www.move.ai/) has a free/limited version. Be aware of these sorts of companies as this is where motion capture is going - *any native crappy video camera* will be able to work.

### Unity 6 Updated Links

Below are added links for learning pathways via Unity. Unity has drastically expanded their learn content over the last 2 years to be updated and robust alongside their updated Unity 6 engine. In some cases there are still legacy Unity Learn content but for the most part, the fundamental pieces of Unity Learn have been updated. This is a list of said updated Learn links that I've come across recently (Summer 2025)

* 2hour 15 minutes[Unity Essentials Pathway: Editor Essentials](https://learn.unity.com/pathway/unity-essentials/unit/editor-essentials?version=6.0)
  * [CSV Exported Content](./UnityEssentials/UL_Unity_Essentials_6_0.csv)
    * [Mission 1: Editor Essentials](https://learn.unity.com/tutorial/66f2e7e9edbc2a01255f7970?utm_campaign=082025_fe12ebbc-a5d3-4d6b-8df7-3f0ba24911d5&utm_medium=LMS&utm_source=outline&version=6.0)
    * [Mission 2: 3D Essentials](https://learn.unity.com/tutorial/66436805edbc2a14bb979ed8?utm_campaign=082025_fe12ebbc-a5d3-4d6b-8df7-3f0ba24911d5&utm_medium=LMS&utm_source=outline&version=6.0)
    * [Mission 3: Audio Essentials](https://learn.unity.com/tutorial/6699eaa4edbc2a0f30162b3e?utm_campaign=082025_fe12ebbc-a5d3-4d6b-8df7-3f0ba24911d5&utm_medium=LMS&utm_source=outline&version=6.0)
    * [Mission 4: Programming Essentials](https://learn.unity.com/tutorial/6699f6f6edbc2a0fecfe98fd?utm_campaign=082025_fe12ebbc-a5d3-4d6b-8df7-3f0ba24911d5&utm_medium=LMS&utm_source=outline&version=6.0)
    * [Mission 5: 2D Essentials](https://learn.unity.com/tutorial/669a09c3edbc2a108606469a?utm_campaign=082025_fe12ebbc-a5d3-4d6b-8df7-3f0ba24911d5&utm_medium=LMS&utm_source=outline&version=6.0)
    * [Mission 6: Publishing Essentials](https://learn.unity.com/tutorial/669a0e92edbc2a1087c9ba97?utm_campaign=082025_fe12ebbc-a5d3-4d6b-8df7-3f0ba24911d5&utm_medium=LMS&utm_source=outline&version=6.0)
* 10 weeks: [Unity Creative Core General Pathway](https://learn.unity.com/pathway/creative-core)
* 12 weeks: [Unity Junior Programmer](https://learn.unity.com/pathway/junior-programmer)

#### Unity Teach Content

* This is a LMS Import setting for 10 unit course based on a [Common Cartridge](./UnityEssentials/UCA-game-dev-common-cartridge.zip) file Unity has provided to all Unity Educators. 
  * This was part of the Tutorial for [Week 2 in the Unity Teach Training and can be found via Unity Learn](https://learn.unity.com/pd-course/teach-unity/29/tutorial/prepare-your-content-for-delivery#68432b51edbc2a11f0f7d515)
  * [Unity Upload LMS Instructions](./UnityEssentials/Course%20Upload%20Instructions.pdf)
* [Unity Version Control Flowchart](./UnityEssentials/Version%20Control%20Flowchart.jpg) Decision Chart
* [Unity Differentiated Pacing Case Studies](./UnityEssentials/Differentiated%20Pacing%20Case%20Studies.pdf)
* [Unity Rubrics](./UnityEssentials/Rubrics/) provided via the Week 3 Teach Learning Pathway

### Class PlayList

* [Student Fall 2022 Music PlayList](https://music.apple.com/us/playlist/game-395-23699/pl.u-xlyNEdNCDpkae)
* [Student Spring 2023 Music PlayList](https://music.apple.com/us/playlist/game395-odu-33915/pl.u-KVXBk1vFRmZPd)
* [Student Spring 2024 Music PlayList](https://music.apple.com/us/playlist/game395-odu-31608/pl.u-oZyl32Zul0R7D)
