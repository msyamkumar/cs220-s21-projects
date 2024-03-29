# Project 1 (P1)

# WARNING: Unless you took a time portal to become my student in the past, this is not the correct repository :) Please go to the correct github repository for the current semester. If you are a Spring'21 semester student though, you are in the right place.

## Clarifications/Corrections

None yet.

**Find any issues?** Report to us: 

- YUCHEN ZENG <yzeng58@wisc.edu>
- ZACHARY JOHN BAKLUND <baklund@wisc.edu>

## Learning Objectives

In this project, you will walk through how to

* Download project files
* Create a python notebook
* Run tests
* Turn in your project

## Step 0: Setting up your environment

**Important:** Before proceeding, install Anaconda3 on your laptop: [MAC
OS installation guidance video](https://www.youtube.com/watch?v=BI4J4-3nWhQ) 
and [Windows OS installation guidance
video](https://www.youtube.com/watch?v=fUohsnkuiKQ)

Much of challenge of programming involves setting up your computer
properly and learning how to use various tools.  This project (worth
1% of your course grade) is designed to walk you through how to
download project files, create a Python notebook, run tests, and turn
in your project.

In subsequent projects, you'll need to very carefully follow [course
policy](https://www.msyamkumar.com/cs220/s21/syllabus.html) to
avoid academic misconduct, but for this project, we just want to walk
everybody through the process.  So feel free to get any kind of help
from anybody (fellow students or otherwise) for P1. **It is important for you to go through the corresponding lab closely before starting with your project. Therefore, please walk through lab-p1 first and learn some techniques to help you complete p1.

## Step 1: Download Project Files

The first thing you're going to need to decide is where to keep your
project work this semester.  If you don't have a preference, we
recommend creating a folder named `cs220` under `Documents`.  How to
find the Documents folder may vary from computer to computer.  On a
Windows machine, you might find it like this in File Explorer:

<img src="windows-documents.png" width="400">

On a Mac, you might find it in Finder here:

<img src="mac-documents.png" width="200">

Inside the new `cs220` folder you created under `Documents`, we
recommend you create a sub-folder called `p1` and use it for all your
files related to this project.  This way, you can keep files for
different projects separate (you'll create a `p2` sub-folder for the
next project and so on).  Of course, computers crash and files get
accidentally deleted, so you should make sure you backup your work
regularly (at a minimum, consider emailing yourself relevant files on
occasion).

Next, you will need to download the files we specify to your project
folder.  In this case, you will just download `test.py` to your `p1`
folder.  First, locate the file you want (test.py) at the top of the
project document.  You'll see a list of files, something like this:

<img src="github.png" width="800">

Downloading files from GitHub (the site hosting this document) is a
little tricky for those new to it.  Follow these steps carefully:

1. left-click on `test.py`
2. right-click on the "Raw" button
3. Choose "Save Link As..." (or similar)
4. Save the file in your `p1` folder

We recommend you use the Chrome browser (other browsers will work too,
but sometimes we've seen Safari automatically renaming files when
downloaded, which is usually problematic).  In Chrome, right-clicking
the "Raw" button looks like this:

<img src="raw.png" width="300">

## Step 2: Create a Python Notebook

Now it gets a little tricky.  You need to figure out the path of your
`p1` folder.  You can think of a "path" as just a more complete name
for a file or folder.  This is useful: if you have more than one `p1`
folder on your computer, how do you distinguish between them?  You
need a full pathname, something like
`/Users/meena/Documents/cs220/p1` (Mac) or
`C:\Users\meena\Documents\cs220\p1` (Windows).  The pathname of `p1`
may be slightly different on your computer, but you can figure it out
with these steps:

1. open your `Documents` in either File Explorer or Finder
2. copy the pathname of `p1` using either these [Windows directions](https://www.pcworld.com/article/251406/windows_tips_copy_a_file_path_show_or_hide_extensions.html) or [Mac directions](http://osxdaily.com/2015/11/05/copy-file-path-name-text-mac-os-x-finder/)
3. paste the pathname of `p1` in your notes somewhere

Now we want to create something called a "notebook" in your `p1`
folder.  To do so, you'll need to open something called a "terminal
emulator".

**Mac**:
1. open Finder
2. click "Applications"
3. open "Utilities"
4. double-click Terminal.app

**Windows**:
1. hit the Windows logo key on your keyboard
2. type `powershell`
3. open "Windows PowerShell" (be careful, DO NOT choose the ones that say "ISE" or "x86")

OK, now the directions are the same for Mac and Windows again.  Type
this in the terminal (replace `P1-PATH` with the pathname of `p1`, as
you determined above; keep the quotes around the pathname, though) and
hit enter:

```
cd "P1-PATH"
```

Type `ls` and hit enter (that's the letter, not a one).  If you've done everything correctly so far,
you should see the `test.py` file that you downloaded in step 1
listed.

Now, type `jupyter notebook` and hit enter.  This should open up
Jupyter as a web page in your web browser.  If it doesn't, and you've
already carefully followed our video install instructions (links at
the top of this page), please bring your laptop to someone's office
hours for help -- there are probably some tricky configuration issues
remaining.

**Note:** even though we'll be working in the web browser now, NEVER
  close the terminal window where you typed `jupyter notebook` until
  your done -- if you do, you'll probably lose any unsaved work.

If everything works properly, you'll see something like this (notice
you can still see the test.py file in Jupyter):

<img src="jupyter.png" width="600">

Click "New", then "Python 3".  A new tab like this should open:

<img src="nb.png" width="600">

Notice how it says "Untitled" at the top?  Click that word, type a new
name for the notebook, then click "Rename".  We recommend you name
your notebook "main".  Now, if you go back to File Explorer or Finder
and open the `p1` folder, you should see a file named `main.ipynb`
(though the extension of ".ipynb" may be hidden depending on your
computer).  This is the file you'll hand in at the end.

## Step 3: Copy/Paste Code

Now you're going to run some Python code.  We don't expect you to
write your own code for this project yet, so you'll just copy/paste
what we provide.

In the box adjacent to `In [ ]`, paste the following:

```
#q1
name = "World"
"Hello " + name + "!"
```

Then hit SHIFT-ENTER on the keyboard (this means you should first
press and hold down the SHIFT key, then press the ENTER key at the
same time).  There should now be an `Out [1]` area saying this:

```
'Hello World!'
```

A new input box (called a "cell") will also have been created
automatically for you.  Let's paste this in that cell:

```
#q2
432*65
```

Hit SHIFT-ENTER again to run it, and you'll see an output of `28080`.

At this point, your notebook should look like this:

<img src="p1.png" width="600">

Let's paste and run one more cell:

```
"oops"
```

What if you want to delete that last cell?  Try clicking in the cell
where you typed "oops".  Then hit the ESCAPE key on your keyboard.
Notice how the cell border changes from green to blue?  That means the
notebook is in command mode, so whatever you type will trigger
commands (instead of adding text to the box).  Hit the "d" key twice,
and see how the cell gets deleted.  This will be handy whenever you
make a mistake or want to delete your scratch work.

## Step 4: Run the Tests

Remember the test.py file we asked you to download?  That file is a
Python program that you can run to check whether your notebook looks
correct before you turn it in.  Here are the steps to use it:

1. in your notebook, click "Kernel" from the menu, then click "Restart & Run All"
2. confirm "Restart & Run All Cells"
3. click "File" from the menu (beneath the Jupyter logo), then click "Save and Checkpoint"
4. open a new terminal window, as you did in step 2 of this document (**important: leave the previously opened one undisturbed**)
5. type the same `cd "P1-PATH"` command in the terminal as before, again replacing `P1-PATH` with the pathname of `p1` in your notes, and hit ENTER
6. type `python test.py` and hit ENTER; if that doesn't work, try `python3 test.py`; if that still doesn't work, please get help during office hours.

If everything is setup properly and your notebook is correct, you'll see something like this:

```
[NbConvertApp] Converting notebook main.ipynb to notebook
[NbConvertApp] Executing notebook with kernel: python3
[NbConvertApp] Writing 1214 bytes to cs-220-test.ipynb
Checking 1
Checking 2
{
  "score": 100.0,
  "tests": [
    {
      "test": 1,
      "result": "PASS",
      "weight": 1
    },
    {
      "test": 2,
      "result": "PASS",
      "weight": 1
    }
  ]
}
TOTAL SCORE: 100.00
```

The only thing you need to care about for now is that last line:
`100.00` means you're passing 100% of the tests.

In general, for tests to be helpful, make sure you alway do the
"Restart & Run All Cells" and "Save and Checkpoint" steps described
above.

## Step 5: Hand in the Project

Before you can hand in the project, you need to add a few more
details.  Paste the following in a new cell:

```python
# project: p1
# submitter: NETID1
# partner: NETID2
# hours: ????
```

Replace `NETID1` with your Net ID (usually the part before "@wisc.edu"
in your student email address).  If you worked with a partner, replace
`NETID2` with your partner's Net ID; otherwise, replace NETID2 with
"none". For `hours`, estimate how many hours you spent on this project, eg. 1.5 for one and half hours, 0.17 for 10 minutes.

If you worked with with a partner, there should only be one submission
between you (please don't both submit), and make sure that `submitter`
refers to the one actually submitting the code (not the other
partner).

To hand in the notebook, complete the following steps:

1. save and run through the tests one last time (after you added your Net ID info)
2. go to [https://www.msyamkumar.com/cs220/s21/submission.html](https://www.msyamkumar.com/cs220/s21/submission.html)
3. select "Project 1"
4. click "Choose File" and find your main.ipynb file
5. click "Submit"
6. check the "Submission Status" below; it is normal to see some "info:" messages, but make sure you correct any "error:" messages
7. click "View Submissions" to make sure your submission looks correct

#### Please remember to `Kernel->Restart and Run All` to check for errors, save your notebook, then run the test.py script one more time before submitting the project. 

Congrats on finishing your first CS 220 project!
