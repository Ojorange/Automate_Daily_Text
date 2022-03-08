# Automate_Daily_Text

#### Video Demo: <URL HERE>

#### Description:

I always end up forgetting to read the Daily Text. So I made this script to play it out loud, and automated it to run on startup.

## Setup

After Cloning this Repo, from the root of the project create a Virtual Environment. `python -m venv env`

Activate your venv with `source ~/PATH_TO_ROOT_OF_PROJECT/env/bin/activate`

Now that you are inside the venv go ahead and download and install the dependencies using `pip install -r requirements.txt`

That's it! You should be all set to run the program. Depending on your IDE you should be able to hit start or run. The command to run should be along the lines of `PATH_TO_ROOT_OF_PROJECT/env/bin/python PATH_TO_ROOT_OF_PROJECT/main.py`

## Automating on Startup

### macOS

1. Start **Automator.app**

2. Select **Application**

3. Click **Show library** in the toolbar (if hidden)

4. Add **Run shell script** (from the **Actions/Utilities**)

5. Copy & paste the script into the window (`PATH_TO_ROOT_OF_PROJECT/env/bin/python PATH_TO_ROOT_OF_PROJECT/main.py`)

6. Test it

7. Save it somewhere (for example you can make an **Applications** folder in your HOME, you will get a **ProgramName.app**)

8. Go to **System Preferences** -> **Users & Groups** -> **Login items**

9. Add this app

### Windows

1. Create a **.bat** file that has the following code: `PATH_TO_ROOT_OF_PROJECT/env/bin/python && PATH_TO_ROOT_OF_PROJECT/main.py`

2. Click on **start** and type **“ask Scheduler** and hit enter

3. Click on **Task Scheduler Library**

4. Click on **Create Task** on the right hand side of the screen and set the parameters a **Name** and optionally Set a **Description**
5. Click on **Triggers** tab and then click on **New…** Choose **At log on** from the drop down menu, Under Advanced Settings I like to Delay it for 30 seconds for my preference, click **Enabled** and hit **OK**

6. Click on the **Actions tab** and then click on **New…**

   1. For **Action** set it to **Start a program**
   2. For **Program/script** Select your batch file

7. Click on **OK** then on **OK** on the create task panel and it will now be scheduled.

#### Thank You! - Ojesh Bisht
