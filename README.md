# Automate_Daily_Text

I always end up forgetting to read the Daily Text. So I made this script to play it outload, and automated it to run on startup.

## Setup

After Cloning this Repo, from the root of the project create a Virtual Environment. `python -m venv env`

Activate your venv with `source ~/PATH_TO_ROOT_OF_PROJECT/env/bin/activate`

Now that you are inside the venv go ahead and download and install the dependencies using `pip install -r requirements.txt`

That's it! You should be all set to run the program. Depending on your IDE you should be able to hit start or run. The command to run should be along the linds of `PATH_TO_ROOT_OF_PROJECT/env/bin/python PATH_TO_ROOT_OF_PROJECT/main.py`

## Automating on Startup

### macOS

1.Start **Automator.app**

2.Select **Application**

3.Click **Show library** in the toolbar (if hidden)

4.Add **Run shell script** (from the **Actions/Utilities**)

5.Copy & paste the script into the window (`PATH_TO_ROOT_OF_PROJECT/env/bin/python PATH_TO_ROOT_OF_PROJECT/main.py`)

6.Test it

7.Save somewhere (for example you can make an **Applications** folder in your HOME, you will get an **ProgramName.app**)

8.Go to **System Preferences** -> **Users & Groups** -> **Login items**

9.Add this app
