#### GAME 395 Topics Class

# Game 395 Topics Class: Unity3D Game Engine

**Overall TL;DR:** Design, Development, Deployment, & Software Patterns that will help you understand Unity3d and other game engines.*We all have different starting points and we all have different paces. Success in this class: show up, participate, keep on iterating, keep creating, keep trying, and you will do fine* Last Updated 1-7-2024.

<Image>
<a name="Dalle GenerationCat"></a>
<img src="Images\CatLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A cat wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

| | |
|---|---|
| **Instructor:** John Shull | **Semester:** Spring 2024 |
| **Email:** [JShull@odu.edu](mailto:jshull@odu.edu) | **Class Meeting Times:** Mon & Wed, 3:00-4:15pm |
| **ODU Office:** Dragas 1108D | **Class Location:** Monarch Hall 2116 |

## Course Description

GAME 395: Designing and Developing with the Unity Engine. This class will focus on core software programming patterns that can be used in all major game engines. We will primarily be utilizing Unity3D for the class and we might get to explore Godot as well. This class will break down Unity into its core systems and we will explore how said systems can be found in most game engines. We will focus in on four key areas: Version Control, Unity, 'The Observer Pattern', and the 'Humble Pattern'. We will work through the Unity Package Management system so you can make your own Unity Package(s). I will encourage the use of new machine learning tools like [ChatGPT](https://openai.com/) but you will still have to explain the entire software architecture and the choices you made utilizing services like ChatGPT, Copilot, etc. The class will focus on one core project that students will have to **[mod](https://en.wikipedia.org/wiki/Video_game_modding)**. Upon modding the game you will then be required to deploy it across either Windows, Linux, Mac, Android, or iOS. The class is designed around one day being dedicated to learning/teaching with the second day used in the software. Whether you’re an expert in Unity or brand new to Unity, this class will help build confidence, make you familiar with the entire Unity environment, immediately help build content for your portfolio, and will provide information that directly helps towards you building confidence in general software practices. This class will involve programming.

## Required & Suggested Materials

There is no official book for this class - most of the information will be provided via the instructor and made accessible within a GitHub repository that will be provided and updated throughout the class. I will provide some free material and will be in the books folder. If you wanted to purchase a book, I would suggest [**'Choose your Wow!'** by Scott W.Ambler and Mark Lines](https://www.amazon.com/Choose-your-WoW-Disciplined-Optimizing/dp/1628257547/) and look into [**Game Programming Patterns** by Robert Nystrom](https://gameprogrammingpatterns.com/).

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationDog"></a>
<img src="Images\DogLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A dog wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

## Office Hours & Contacting Me

The best way to reach me is through [Microsoft Teams](https://teams.microsoft.com/l/chat/0/0?users=jshull@odu.edu). You can also reach me at [JShull@odu.edu](mailto:jshull@odu.edu). You can check my [Office Hours Booking page](https://outlook.office.com/bookwithme/user/a264cdcc1bda4ce4884e4b052b89bdc3@odu.edu/meetingtype/RDiapeLfhkq1XJ5topb6_g2?anonymous) to request a MS Teams 15 minute time to meet with me. I am on [campus](https://goo.gl/maps/ebtAi9WVRHqaKUgP9) Mondays & Wednesdays. The rest of the time I could be at [VMASC](https://goo.gl/maps/o2nEecGLXEQnmMw28) and/or working remote. If you ever need to meet outside of those times just ask me via email/Teams if there's another time. I try to restrict my meeting times to keep me honest and on task as I tend to ramble and put others needs over my own which is a blessing and a curse!

## Student Learning Outcomes

My intention on teaching this class is to build confidence within a game engine - currently this is Unity and we might explore GoDot. I hope that this class empowers you to explore other real-time simulation tools! :rocket: I feel confident that by the end of the class you should be stronger in understanding general software development processes. You will build experience towards understanding general software design patterns and current technologies that industry is using to collaborate and share work. I also believe that you will feel more confident in deploying from Unity to a wide range of other operating systems, including Apple and Android. Below are the high level outcomes I expect you to walk away from immersing yourself within this class.

* Understand the basics of Version Control Systems
* Understand the basics of tasking/issue based work systems like [Microsoft Planner](https://tasks.office.com/olddominion.onmicrosoft.com/en-US/Home/Planner/), [Jira](https://www.atlassian.com/software/jira), [Trello](https://trello.com/), and [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
* Understanding the basics of software package management systems like [Unity Package Manager](https://www.youtube.com/watch?v=mgsLb3TKljk)
* Understand deployment models, versioning, and documentation standards
* Understanding of basic Production Models
* Increased Confidence within Unity3D and increased confidence in deployment in Unity
* Understanding the [Observer Software Pattern](https://learn.microsoft.com/en-us/dotnet/standard/events/observer-design-pattern)
* Understanding the [Humble Software Pattern](https://www.youtube.com/watch?v=3O_rpTWdGps)
* Be aware of [Data Oriented Design](https://github.com/dbartolini/data-oriented-design) and [Unity Entity Component System ECS](https://unity.com/ecs)

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationBadger"></a>
<img src="Images\BadgerLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A badger wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

### Action Items

These are items you will have the choice to complete. These items are broken up in a system that builds towards how I evaluate you and ultimately provide you the end game score. These are going to be explained more later on a different section of the document associated with the [grading agreements](#grading-agreement-check-ins).

* Action Items  
  * [High Stake Item](#high-stake)
  * [Medium Stake Item](#medium-stake)
  * [Low Stake Item](#low-stake)

### Live Demonstrations & Industry Professionals

Every month I might  show-off one personal/work project(s), maybe some new software, and/or some VMASC projects, and update some of my own public GitHub repositories that might be helpful for the class. I am working on finalizing the partial guest lectures that are from the game industry and/or technology experts ranging from Valve, Sharkmob, Ubisoft, and maybe some hardware companies like TiltFive and/or developers from the HoloLens team. In the past I've had people drop in that worked on Dota, Star Wars Battlefront and Jedi Survivor, BioShock Infinite, Assassins Creed, Ghost of Tsushima, Far Cry, The Division, and others!

***
<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationHawk"></a>
<img src="Images\RedTailLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A red tail hawk wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

## Accessibility and Inclusion

Most of the indented statement below was originally written by [Ann Kumm](https://www.odu.edu/directory/people/a/akumm001) - my significant other and the main reason this class was able to happen. Without her input, guidance, and support I would not have been able to make this class possible. We stand on the shoulders of giants, my *giant* happens to be about foot shorter than me!
>Your success in this class is important to me. We all need accommodations because we all learn differently. **Everyone** has the right to the full experience of the university education you have earned by admission. If there are aspects of this course that prevent you from learning or exclude you, please let me know as soon as possible and whenever needed. It is never too late to request accommodations—our bodies, minds, and circumstances are in constant states of change. Together we’ll develop strategies to meet both your needs and the requirements of the course.

**Mental Health & Stress Management**: As a student, you may experience a range of issues that can affect your learning (for example, increased anxiety, strained relationships, decreased motivation, feeling down). These concerns or stressors can affect your academic performance and reduce your ability to participate in class. Old Dominion University services are available to assist you with addressing these concerns and others you may be experiencing. Please see the [*Campus Resources* section below](#campus-resources).
I will try my best to accommodate everyone in this class to the best of my ability- at anytime if something I'm doing doesn't feel accessible please let me know. I have been in your place at this University and I understand that in a lot of situations you feel there isn't a way forward... if I made it this far... I can guarantee you there is always a path forward and in most cases it just requires you to ask.

### Campus Resources

|  | |
|---|---|
|[Office of Education Accessibility](https://www.odu.edu/accessibility) 1021 Student Success Center [757.683.4655](tel:+7576834655)|[Women & Gender Equity Center](https://www.odu.edu/life/support/wgec) 1000 Webb Center [757.683.4109](tel:7576834109)|
|[FeedODU Monarch Pantry](https://odu.edu/sees/feedodu) Suffolk Room in Webb Center [757.683.4325](tel:7576834325)|[Counseling Services](https://www.odu.edu/counselingservices) 1526 Webb Center, North Wing [757.683.4401](tel:7576834401)|
|[The Writing Center](https://www.odu.edu/al/centers/writing-center) 1208 Perry Library [757.683.4013](tel:7576834013)|[Student Outreach and Support-SOS](https://www.odu.edu/life/dean-students/student-outreach) 2008 Webb Center [757.683.3442](tel:7576833442)|

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationShark"></a>
<img src="Images\SquirrelLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A squirrel wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

## Assignments, Un-Grading, and Specification Grading

Grading Agreements! What? *Ungrading* wtf is that?! That's right, *zero* grades. But *how?!* Below I'm going to take a concept called *ungrading* and another concept called *specifications grading* and break out a "Choose your own Adventure" pathway towards the 'grade' agreement that you want to take on. I will lay this out for how this class will work. Yes you will have work to do, yes I will provide feedback, and yes because the university still requires me to submit a grade you will get a *grade*. If you're here to game the grade system, drop the class and please save us the time and energy as it won't work in this class. This class is structured based around building experience and alining your realistic time commitment towards this class. I get it. Trust me - there are classes that take a lot of time and there are classes that don't. This class can be thought of as a flex. If you've got the time to give and you want to aim high - do it. If you're working two jobs and can only come in and meet the general requirements - do it. I'm not here to judge your individual experiences and where you are within your own journey - this concept hopefully meets you where you are and helps maintain that to where you want to go. I'm going to approach this from a sort of bundled perspective, you can think of this as a mini-degree in which there are core stake requirements and 'gen-eds' that you can pick from to make up your own pathway. Given that this is the first time I'm doing this - I might be making some adjustments to how we transfer between content and the work you do and that's just to help eliminate *OP* strategies that I'm sure will emerge. To keep it simple, everything you do in this class will either be a Low-stake, Medium-stake, or High-stake assignment. You are then committing to what you want to do via a process of periodic check-ins with me, just like if you were working a contract, and ultimately working towards delivering on that agreement and commitment. Think of me as a customer waiting to pay you for what you deliver, or not pay you for what you don't deliver. I will provide feedback at multiple intervals throughout the class, allow ample time for you to schedule one-on-one time with me, and will provide feedback on all **medium & high state** assignments. In the long run - my plan is to use this class and the next few times of teaching this class to provide a set of more defined pathways tied to industry specifications to allow a wider range of individuals who are entering this class with a various levels of different technical and non-technical skills pathways to become even stronger within their area. To get there I first, I need to get a better idea of where everyone is and watch what emerges through some of these first few classes I teach - so again, thank you!

### Evaluation of Learning

In our class, your work will be evaluated using a form of ungrading called grading agreements. A grading agreement is a more authentic means of assessment in a technical course because it models workplace practices (e.g., the concept of adding/removing features towards a game by the next big update/event) While you will receive a final grade at the end of the semester, I will not be grading each individual assignment or task. Instead, I will provide feedback by asking questions and making comments that engage your work. The purpose of this is for you to learn and be able to use feedback to improve and/or reflect. This is important because I believe that grades should tell a story of progress and achievement. This is why in our class, your final grade will be an iterative reflection of performance, progress, and process.
The underlying premise of a grading agreement is that if you do the work required and meet all expectations, you will see enormous gains in your learning and pass the course. This shifts the focus from points and percentages to a focus on learning. The hope is that this frees you up to focus more on learning and taking risks instead of zeroing in on a particular grade. I want you to strive to hit that extra feature or game mechanic because it pushes you want to aim high, even if the mechanic doesn't work out entirely or is over-powered as all get out.
Therefore, if you simply complete all of the work for this class and engage with me throughout the session, prepare for your semester project, provide periodic feedback to me, utilize the class lab time, participate in the class discussion, and are prepared and professional, which includes bringing in functioning games when assigned to do so, and staying on task, you will earn a B. There’s **no catch**. As *Inoue* states:
>In a nutshell, if you do all that is asked of you in the manner and spirit it is asked, if you work through the processes we establish and the work we assign ourselves in the labor instructions during the quarter, if you do all the labor asked of you, then you’ll get a “B”. This grade and labor effort is not based on artistic/creativity and will not be based off what I or your colleagues think of your 'work', it only assumes that you are listening to our feedback compassionately. We may disagree or misunderstand your intent, but if you put in the labor, you are guaranteed a B course grade. If you miss class (do not participate fully), turn in assignments late, forget to do assignments, or do not follow the labor instructions precisely, you will get a lower course grade.

### Item Assignment

This is getting broken down in the lower sections in [low](#low-stake), [medium](#medium-stake), and [high](#high-stake) stakes and will be broken down in those sections. Below is just general information about what the definition of an assignment is.

**Time Allotment requirements** For most of the assignments I have setup a window of time that's suggested to put aside for it, this doesn't mean it will take you the full time, it's more an allotment for you to understand if you're constantly brushing up against it that maybe you should reach out and talk with me. By design these items shouldn't exceed the time windows I've put in. I will be providing feedback throughout the assignment submission timeline, you can expect feedback on all required medium and high stake assignments. Low stake assignments are there to help scaffold and build towards the class and by definition already include a lot of contact points with me and other students.

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationDolphin"></a>
<img src="Images\DolphinLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A dolphin wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

### Low-Stake

There are **20** required low-stake items that everyone will be doing. For the most part a chunk of these are all taken care of the first 2-4 weeks of class and can be thought of as roughly 30-40% of your effort towards the class.

#### Required Low Stake Assignments (RLSA)

**Everyone has to do these four required assignments listed**

* 9 [Weekly Exit Tickets](https://forms.gle/cg9z5PgytyDKXeSh9): Expected Time 5-10 minutes per survey per week. Generally there are 10-14 of them throughout the semester.
  * These are to help you understand your own progress and are analytical reference markers for me to make sure that I'm presenting material that aligns with your needs and that I'm able to be agile enough to make adjustments at a weekly level as needed for your best interest. They also help you reflect on what you're learning to keep you engaged and provide you input into my adjustments.
* 1 [GitHub Profile Setup](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme): Expected Time 45-90 minutes
  * We will be learning the basics of git and general version control practices within the first two weeks. This Low-Stake assignment is for you to setup an outward facing GitHub profile page. I've included mine as a reference as well as others that you can look at. [John GitHub Profile Page](https://github.com/jshull)
* 1 [UnityID Account Setup](https://id.unity.com/en/conversations/252364a8-cfe1-4a46-8c8d-a3e1f2a7f452019f): Expected Time 10 minutes
  * This is self-explanatory as this is a [Unity](https://id.unity.com/en/conversations/6a0b1b07-7146-4c05-92f2-ed88433c6afc002f) class!
* 1 [Initial Student Questionnaire](https://forms.gle/Er1HDHR6AyGPc8qP8): Expected Time 15-25 minutes.
  * This is a questionnaire that will be one of the first items you have to complete.
* 8 weekly Canvas assignments
  * If you fail to do the 8, you will be forfeiting the ungraded agreement that turns into the A-B option. They will always be due the week after they are issued. They are released each week upon the conclusion of the second class and have to be finalized by the following weeks second class.

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationOtter"></a>
<img src="Images\OtterLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A otter wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

### Medium-Stake

There are **4** required medium-stake items that everyone will be doing. They are outlined below. There are then some additional medium-stake items that you can choose from to complete towards your grading agreement.

#### Required Medium Stake Assignments (RMSA)

* 2 [Grading Agreement Check-Ins](#grading-agreement-check-ins): Expected Time 15 minutes, we will do one at the beginning of the semester and one towards the middle-end of the semester
  * You will be required to meet with me one-on-one to discuss your progress and your grading agreement.  I will be accommodating to schedules as needed. These meetings are designed to make sure to address any questions you have and to make sure you're on-path to deliver your working project.
* 1 GitHub Project Generation and Management: Expected Time 7-14 hours over the course of the semester
  * Using GitHub project to help manage your Kanban board, expect to spend roughly 15-30 minutes on average a week managing your project board over the course of the semester. You will share your project repository with from the first initial [grading agreement](#grading-agreement-check-ins). Which means you should anticipate to have this setup and 'ready' by week 3.
* 1-2 Project Final GitHub Pull Request: Expected Time 30-60 minutes towards the end of the class
  * Completion of a Required Repository Project format which will be given to you all well in advance and all project content that you work on across the entire semester will always be 'ready' for submission as it's part of the iterative design process: aka always be ready to deploy and deliver!

#### Optional Medium Stake Assignments (OMSA)

* 1 Publicly hosted Unity Git Package: Expected time 2-8 hours over the semester
  * This can be a set of 2D/3D models you've created.
  * This can be audio files that you've created
  * This can be a custom section of code that you've created.
  * The content = I will be flexible on but the package requirements all have to be met, include samples, and documentation to support it. See me for more details.
* 1 Project Changelog that has been managed throughout every pull request to your project Expected time 4-8 hours over the semester
  * Keep a running changelog with your semester project following the [Change Log Standards](https://keepachangelog.com/en/1.0.0/)
  * Hook project commits with tags back to project tasking and showcase synchronization of issue tracking with commits, milestones, and versions.
* 8 Unity Learn Modules: Expected time 4-16 hours over the semester
  * Completion of 8 Unity Learn Modules that are part of your project plan and are outlined in the first 1 on 1 meeting.
    * Unity Learn is amazing and I'd be a complete idiot for not taking advantage of it in this class. **Unity** runs a few different ways of learning. You will have a lot of control here to go through the various pathways and/or kits. Unity Learn is also sometimes out dated so to help with some of the more dated content you're free to supplement that material with curated YouTube videos by seasoned Unity developers.

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationPenguin"></a>
<img src="Images\PenguinLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A penguin wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

### High-Stake

There are **2** required high-stake items that everyone will be doing. They are outlined below. High-stake items are slightly different, as they are fundamental to the class, and there is no such thing as an *optional* high-stake item. Within the high-stake assignments you will see variations of requirements that aline to your grading agreement pathway. This class is based around the end deliverable and these high-stake assignments support that ultimate deliverable.

* 1 'mod' Submission Plan
  * Somewhere before Spring Break you will submit your project mod plan.
    * Includes GitHub Issues and task management
    * Includes connections towards personal goals and how you plan on 'modding' pieces of the game you're working with
* 1 Final 'mod' Submission & Final Project GitHub Portfolio
  * Demo a mod of a working deployed experience via Unity3D on device and show it off during our exam time in class
  * Showcase your burn-down GitHub project plan as well as explain your project tasking breakdown
  * GitHub project synchronization and successful pull request for submissions

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationKillerWhale"></a>
<img src="Images\KillerWhaleLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A killer whale wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

### Grading Agreement Details

In order to be eligible to pass this course with a **'C'** you *must* complete all required stake assignments - I've based these requirements on the expected minimum amount of time spent outside of class. If this is your *goal* I suggest you drop the class and rethink your major (especially those in Game Design). I will be making some changes to these agreements within the first week and they are not initially due to me until we have our first one-on-one as this is the main reason: to address the grading agreement.

#### The Advanced Agreement

An **A** in this class requires you to go beyond the normal expected allotment of time for this class. The typical rule is 2-3 hours per 1 hour of in class time. A 3 credit class then would require about 5-6 hours of additional weekly time spent on a single class. Given that this class is software intensive and we are all coming at it with different backgrounds this is going to range wildly across each individual. To maintain that this class is accessible, but also realistic in your expectations, expect to use my office hours a lot, use me to help with your projects when you're stuck (that's the point of me teaching the class!!), be ready to put additional time after class to fully grasp all that you could do within Unity, expect lots of failures and through those failures I promise you will be rewarded. My main job for you within this advanced agreement is to help limit your focus so you set a good cadence and still maintain realistic hours within the time frame alloted for this class: no one wants to overwork and my theory is overworking is a derivative of bad planning.

* Complete all assignments on your plan
* Submit 12 Weekly Exit Tickets
* Complete 8 Weekly Unity Assignments
* Submit 'mod' Plan
* Turn in your Final Mod Project Pull Request
* Your experience compiles and runs on device with no major issues.
  * This software aligns to your GDD and your Unity Learn Plan
* Show up to the Final Exam
* Show up prepared for both conferences with me
* Contribute to the local community in a way that you define

#### The Basic Agreement

A **B** in this class is easy to get. Show up, use the lab time wisely, make sure to hit all of the low-stake assignments, the Experience Design Document & Project Plan, and most of you should be okay. I hope that this also then encourages you to push for that next level contract as a 'B' in this class is BASIC AF and you all are better than that!

* Complete all assignments on your plan
* Submit 8 Weekly Exit Tickets
* Complete 6 Weekly Unity Assignments
* Submit 'mod' Plan
* Turn in your Final Project Pull Request
* Your experience compiles and runs on device
  * This software aligns to your Unity Learn Plan
* Show up to the Final Exam
* Show up prepared for one conference with me

#### The Rubbish-CRUD Agreement

A **C** in this class requires you to plan, use Unity Learn, and layout your plan and then failing on your plan, dropping off the face of the earth and/or just ghosting all of us. Is this an ideal way of taking any class you're paying for? **NOPE**. This is here as a catch-all that I wish I had as I was figuring out my life 20 years ago. I will not allow anyone to actually agree to this agreement, but it's here for those 'life happens' moments. The entire class is designed around you wanting to learn and putting in the time. You are "buying your time" is the best way to think of this class and this agreement is for when *'Sh$$' happens'* and you make some attempt to communicate that with me so I can help you prepare for the *crud*.

* Complete a majority of required stake assignments
  * Complete the Initial Project Design Document & Project Plan
* Submit 5 Weekly Exit Tickets
* Complete 4 Weekly Unity Assignments
* Turn in your Final Project Pull Request
* Show up to the Final Exam and provide a presentation on failures and lessons learned
* Show up prepared for one conference with me
* Notify me of said *'Sh$$ happens'* event(s) and keep an open communication line with me
  * If you manage to do this while also trying to balance out your life other options like [Incomplete's](https://ww1.odu.edu/academics/academic-records/grades/incompletes-withdraws-zgrades) become available. My policy on an incomplete is based on open lines of communication and when the CRUD literally hits the fan and time isn't an option. I hope that this doesn't happen - but if it does - I hope you've gotten past the midpoint in the semester and have managed to have been on track.

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationIguana"></a>
<img src="Images\IguanaLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'An Iguana wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

## Grading Agreement Check-Ins

Through periodic grading agreement check-ins with students we will work together to make sure you stay on track and get adequate feedback from myself. We are doing this by setting goals and documenting your progress with me. This helps maintain that you've finished the required assignments and are still on track for your grade completion (we want to ensure you meet **ALL** requirements). This is very similar to how you make sure you're on track to graduate - we just go down the list of assignments you've agreed upon and do a quick status check of them and course correct as needed. I generally set this up with everyone and try to meet everyone one-on-one before the end of September, we then meet again one-on-one sometime after fall-break, and then we meet again right at the end of the class.

* I hope you feel encourages to take added risks and pursue projects you are passionate about.
* Your classmates and I will be able to respond to your work as colleagues and readers, rather than judges and critics.
* You should always have a sense of what your grade is. That being said, if at any point you have any doubts or want additional guidance, just let me know.

We will talk more about what this means and you will be given the opportunity to consider what this looks like for you over the course of the semester.

***

<div style="page-break-after: always;"></div>

### Late Work & Grace Period

My late work policy includes a Grace Period that should cover most of the problems that arise (e.g., academic conflicts, illness,
religious holidays, personal issues). It only applies to medium and high stake assignments and can be used multiple times throughout the semester. There is **no** grace period for weekly low stake assignments.
You do not need to ask in advance or explain why your work is late. Instead, just use the Grace Period explained below:

>1. The Due Date is the day your work is due.
>
>2. The Grace Period occurs between the Due Date and the Deadline. Every student has a 3-day Grace Period after the Due Date during which an assignment or project can still be submitted. Work submitted during the Grace Period will be marked as late; however there is no grade penalty during the Grace Period.
>
>3. The Deadline comes 3 days after the Due Date. There are no extensions on the Deadline date. If you do not turn in your work by the end of the Grace Period, you will receive a “Not Submitted” for that assignment and may not receive feedback for revisions after that.

**Extenuating Circumstances**: In the case of extenuating circumstances, contact me as soon as possible. As long as you are honest and timely in letting me know what’s going on, we will most likely be able to work something out as that's how the rest of the world works and I don't care about my ego ;)

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle GenerationShark"></a>
<img src="Images\SharkLoot-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the lower portions of the image. The bottom says 'A shark wearing a backpack and a hardhat with a light looking for the loot, digital art'" title="SyllabusHeader" class="centerheader"/>
</Image>

### Time & Money

**A big piece of this class is your time with me in the lab.** I believe that a *topics* class like this one are best designed to be places to work through material and learn from your instructors. I believe in opening up my time to all of you to utilize it as you all need it. I am making myself available roughly 50% of the in class instructor time; instead of lecturing at you - I want to help you become the best you within software & Unity. I want to break some things down for you to explain how this works from a cost benefits analysis perspective. This is a 3 credit class, [current odu in-state undergraduate rates](https://www.odu.edu/tuition-aid/tuition/rates/archived/2021-2022) places this class at approximately *3x$374 =* **$1122**.
>If we break down the time we meet: 75 minutes per class, accounting for holidays in the Spring semester of 2024 you get me for 28 classes, or 2100 minutes. My plan right now is to use approximately 975 minutes towards lecture, leaving you roughly 1125 minutes for in-class software use towards your project and *consultant time* with me. This means overall the class is costing you $32 a hour (ballpark). If you were to contract me as a private consultant, my rate is roughly $150-$200 an hour depending upon what the level of need is. If you take the time leftover to utilize me as a consultant in this class (1125 minutes or roughly 18.75 hours) my cost to you is roughly $3,750 and that's just for about half of the time mentioned, so for the full time you're getting me at a 85% discount. *This doesn't even include the additional hours weekly I hold for office hours*. I point this out because I believe in transparency and I want you to know how the rest of the world operates. This is not a way to boost my own ego, but hopefully for you all to fully understand and appreciate the cost of scale when taking these classes and to get the best bang for your :dollar: I would like to utilize every minute you have within this class with your fellow classmates and with my time and experience to help you escalate your capabilities and build that confidence! If you strive for the highest [grading agreement](#a-b-contract) offered and hit it; I will personally write you a letter of recommendation as needed, when needed, as long as you notify me with at least two weeks notice. This offer will be good the moment your grades post and is good until May 1, 2026 (two years post the end of this class).

***

<div style="page-break-after: always;"></div>

<Image>
<a name="Dalle Corn Generation"></a>
<img src="Images\CornItHasTheJuice-01.png" alt="Image of artificial intelligence generated images using Dalle setup in a horizontal array. The prompts used for the Dalle generation are in the upper and lower portions of the image. The top says 'a video game character based on the expression: 'Its Corn, a big lump with knobs, it has the juice, I cant imagine a more beautiful thing, digital art' and the bottom says 'a video game where you are a large piece of corn that has to jump over rivers of butter, digital art'" title="WeeklyStructureHeader" class="centerheader"/>
</Image>

## University Policy

You should be aware of University policy towards student conduct & academic integrity. I do not set these policies but as students at ODU you are required to adhere to them and equally I am here to make sure that we stay transparent to what is prohibited. Please make sure you review this information as there are a lot of cases in which you might not think you're violating a policy but in actuality you are. Please see the [ODU Office of Student Conduct & Academic Integrity for additional information](https://www.odu.edu/oscai).
<!--
<Image>
<a name="Full Model View"></a>
<img src="Images\A2M_FullModelView.png" alt="" title="" class="centerlrg"/>
<p>&nbsp;</p>
<figcaption class="centersml">Image 1: What the user sees when the load the alp file</figcaption>
</Image>
-->