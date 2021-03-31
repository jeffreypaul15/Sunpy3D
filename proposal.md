

# Project: 3D Plotting

## Summary of proposal

  
  

### Why this project?

My open-source journey began with SunPy about 4 months ago, I enjoyed having to look at the visualization capabilities of SunPy and developed a keen interest in visualization while exploring the package and attempting to solve its issues. The efficient usage of python and purposeful open source contribution was the main drive for me.

I have worked with Python as my primary programming language for over 3 years now and have a strong understanding of it and Pyvista while contributing to SunPy has made me better at it.

I have been involved with contributing towards and understanding SunPy with its underlying libraries for about 4 months now which excites and gives me the confidence that I shall be able to complete the given project successfully and according to the required standards.

  

## Project Roadmap and Deliverables

### Synopsis

SunPy has multiple extensive 2D visualization features for plotting Maps. The ability to have to convert these plots into 3D would enhance the capabilities of SunPy visualization.

This project would include adding a separate python package that extends 3D plotting functionality to SunPy, by using **PyVista**. It would also recreate some of the various existing features and overlays that SunPy's GenericMap has in 3D. 
I shall also maintain a blog based on my open-source journey and this project with SunPy.

The entire project is split into 3 major components which include:-


#### 1) Extending Functionality
- The existing code makes use of PyVista for 3D plotting functionality and all of the code for 3D plotting would make use of PyVista itself. Currently, there exists simple functionality for plotting any given `GenericMap` from SunPy to be plotted using Pyvista and this will be the baseline from where I would pick up on.
- As stated by the requirements, moajority of the functionality of a 2D `GenericMap` from SunPy shall be implemented in 3D. It would include the extensions of all the available plotting mechanisms with the approptiate `AstroPy` units.
- The 3D PFSS field lines from Pfsspy shall also be implemented and tested carefully.
- The underlying packages for 3D plotting would have to be listed out and this has to be carefully tested with different versions of the packages to make sure that this works with SunPy.
- There are no bounds defined for 3D plotting capability and adding extra functionality for plotting Astropy's coordinates shall also be implemented.

#### 2) Extensive documentation
- As per SunPy standards, documentation is extremely important. The entire documentation process shall be written using **Sphinx** as SunPy uses it and I've worked with it extensively before.
- Required documentation is a general order from writing the Index file followed by
	- Introduction
	- Installation
	- Description of the package
	- Reference API which includes the class inheritance diagrams and function description required for the code that shall be written
	- Example Gallery
	- Contribution and release history.
- Sphinx's **Autodoc** allows the extensive documentation of classes and functions which makes use of the well-written docstrings in Python to create the required documentation. Therefore relevant docstrings are to be written that highlight the usage of every class and method with its required parameters and function.
- Gallery Examples shall also be written according to the added code depending on how Sphinx interacts with Pyvista.

  

#### 3) Testing and Integration with SunPy and PfssPy

- The entire project shall be tested efficiently wherever necessary.
- Testing shall mainly be performed with **Tox** integrated with Pytest. The project shall be set up using tox according to SunPy's requirements.
- The appropriate 3D testing methodology shall also be researched and decided on.
- Once tested, benchmark tests shall also be performed to understand the computation required for visualization.

  
  

### Timeline and Weekly Deliverables

![image](https://github.com/jeffreypaul15/Sunpy3D/blob/master/screenshots/112889241-03321a80-90f3-11eb-8f16-ad2f54b12b8d.png)

### Further understanding of the deliverables
#### Community Bonding Period

___

#### Week 1  
- I shall get familiar with the working of Sphinx and producing doctest with Sphinx.
- Understand the extent of PyVista's capabilities.
- Rendering of the 3D plots correctly for generating 2D images.
#### Week 2
- Spend time exploring the capabilities of 3D plotting and continuously add functionality such as the extension of plotting to `LASCO maps` and work on the exploration of magnetic field lines from `PfssPy`.
- I shall also get familiar with the possibility of extending most of the 2D plotting functionality to 3D from SunPy.
	
___

#### Coding Period Begins

___

  

#### Week 3

- Get started on working with the code documentation of the existing code. I have already gotten started on writing the docstrings and examples for plotting here.
- Begin with the setting up of documentation via Sphinx and gain information regarding the types of testing that are required.
- Gain insight on the level of `PfssPy` extension to 3D and state deliverables with suggestions from mentors.

#### Week 4

- From here on, I shall focus on the extension of the various 2D plotting functionalities into 3D from SunPy.
- I have extended `draw_quadrangle` from SunPy's `GenericMap` to 3D as I had worked on implementing this in 2D for SunPy itself. An example of correctly rendered 2D plot with the right `cpos` :

![image](https://user-images.githubusercontent.com/50923538/112890316-5bb5e780-90f4-11eb-9a07-2aa418232669.png)

- Research on transformation of coordinate frames to correctly implement `GenericMaps` in 3D.
- Decide on what classes to be vectored into this package from SunPy, AstroPy and PfssPy.
  
#### Week 5

- First few days of this week shall go into implementing the tox environment with the set up of PyTest and Tox for unit testing.
- I shall also dedicate some time to research more on the 3D figure testing methodology.
- Next, I shall work on structuring the appropriate classes for the package as plots from SunPy as well as PfssPy. 
- The new classes have to be recreated for 3D and this would require vectoring existing code into the new package.
- Begin 2D figure testing by rendering the 3D image in 2D and use `pytest-mpl` for figure testing 3D images in 2D. This will either be done by hashing or image comparison from PyTest-mpl.

#### Week 6

- Continue working towards adding the existing methods of SunPy's `GenericMap` to 3D.
- I have implemented a few 2D plotting functionalities such as `draw_grid` and `draw_limb`.
![image](https://github.com/jeffreypaul15/Sunpy3D/blob/master/screenshots/112277482-cce63c80-8ca7-11eb-8163-35adaa2b8830.png)
- Ensuring the extensions are done appropriately with careful comparison from the 2D plots and appropriate tests.
- Research on grid plotting with `WCS axes` in 3D and also research on `clip_interval` of for `vmin/vmax` set-up of the required 3D plots.
- Implementation the plotting coordinates of various `Astropy` units and also drawing of `Great Arc` and `heliographic longitude and latitude lines` in 3D.

 ___

#### Phase 1 Evaluation

___

#### Week 7
- This entire week shall be used as a buffer week, to ensure that the above listed deliverables from week 1-6 are correctly set up.
- Continue working on the extension `MapSequenceAnimator` to `3D gifs`.
- Begin the writing the documentation of the correctly implemented methods according to the evaluation. 
- The examples of all the created methods shall be loaded into a gallery for Sphinx to create a `minigallery` for display in the documentation.
- The required 3D testing methodology would have been extensively researched upon and a solid conclusion would be reached.
- Allot some time for bug-fixes of any major bugs that may arise during the implementation of the 3D plotting as well as the testing and documentation structure.
- The number of tests to be run shall be decided after discussing with the mentors.


#### Week 8
- Re-write any tests (if required) with the appropriate 3D testing method.
- Over-plotting and aligning maps using transparency from `PyVista`.
- Work on rotating the initial 3D plot with understanding of `cpos` with `GenericMap` rotation.
- Begin work on adding code for plotting AstroPy coordinate objects.
- If other tests have to be performed, I shall implement this during this time.
- Recreate `MapSequenceAnimator` as `gifs` with `PyVista` 

#### Week 9
- The `Tox` environment shall be completely set up and all the tests shall be integrated accordingly.
- Conduct a manual test of the documentation of the package so far and continue working on the documentation alongside the code ensuring accurate documentation.
- Major bugs (if any) would be resolved by now and a considerable amount of time shall be devoted to testing all of the small implementations.
- If any new requirements are requested by the mentors, they shall be implemented during these weeks and the testing of the new code as well.
- I have already implemented some starter code for plotting field lines from a given `gong_map`.
![image](https://github.com/jeffreypaul15/Sunpy3D/blob/master/screenshots/112165572-dffbfc80-8c14-11eb-9dd9-9eb3937607fa.png)

#### Week 10
- Cross-check if all the implemented functionalities are what is required for the project. 
- By now all of the required coordinate objects from AstroPy and 2D functionality from SunPy shall be properly implemented with the appropriate tests.
- This will ensure I have worked towards implementing all of required the `sources` from SunPy and over-plotting them with the required `field lines` from PfssPy.
- The documentation and docstrings shall again be tested with the complete implementation of all the `.rst` files and indexed according to what is required.
- The entire package would have been set up in PyPi and a few demo examples would also be listed out here.
___

#### Final Evaluation
Add finishing touches to the aforementioned deliverables and deliver the entire package ready to be used with SunPy.
___

  

## Personal Info
- Time zone: IST (GMT + 5:30)
- Email ID: [jeffrey.paul2000@gmail.com](jeffrey.paul2000@gmail.com)
- GitHub handle: [jeffreypaul15](https://github.com/jeffreypaul15)
- Riot-ID: @jeffreypaul15:matrix.org
- Blog: [jeffrey.paul2000](https://jeffrey-paul2000.medium.com/)
- Location: Bangalore, India.

### Education
- University: Dayananda Sagar College of Engineering, Bangalore, India.
- Major: Computer Science, 3rd year.

### Open Source background and Programming experience

- Programming Languages: Python, Java, C, JavaScript, Dart (Basic)
-  As of writing this proposal, my contributions to SunPy include 11 merged and 3 WIP PRs. I have mainly worked with writing various tests and visualization for SunPy. I also spent quite a bit of time understanding the coordinate systems from a gallery example [PR](https://github.com/sunpy/sunpy/pull/5121).  Besides that, some important PRs are :
-  [Added draw_quadrangle method](https://github.com/sunpy/sunpy/pull/4809) [visualization]
-  [Added STEREO/SECCHI client](https://github.com/sunpy/sunpy/pull/4869)
-  [Added dynamic z axis option](https://github.com/sunpy/sunpy/pull/5025) [visualization]
-  [Added tests for map sequence animator](https://github.com/sunpy/sunpy/pull/5041) [visualization]
-  [Added conversion of map data to float64 in GenericMap.rotate()](https://github.com/sunpy/sunpy/pull/5051) [visualization]

I have enjoyed contributing to SunPy and will continue to do so regardless of GSoC. 
I have worked with Python as a primary programming language as I have spent over 2 years working, researching, and developing in the field of Artificial Intelligence.
I have quite a bit of experience with Hackathons and won [Smart India Hackathon](https://www.sih.gov.in/sih2020) 2020 for Student Innovation  category, where I focused predominantly on AI and the efficient use of Python. Besides this, I also was part of a team that placed top 4 in SAP Semicolon Nationals in 2019 and 2020.
I have worked as a full-time intern at 3 separate AI-based companies.
Solar Physics has gained my interest from my contributions to SunPy and from then on I have explored the visualization of SunPy with AstroPy.

## GSoC

### Have you participated previously in GSoC? When? Under which project?
No, This is my first time participating in GSoC.


### Are you also applying to other projects?
No, I will only be applying to SunPy.

  

### Commitments

I study at university which takes about 7-8 hours of my day and my academic load is very less.
I am open to working full time **~18-20 hours per week** and can work more if required.
I don't have any plans for the Summer and I will be fully focusing on contribution and GSoC with SunPy.

 
### Eligibility

Yes, I am eligible to receive payments from Google. For any queries or further explanations, feel free to contact me at jeffrey.paul2000@gmail.com
