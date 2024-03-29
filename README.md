# MyHours-App
A minimalistic and quick solution for individuals to start MyHours time tracking.

![MyHoursApp Main Screen example 1](assets/images/ms_ex1.PNG)

## Setup

### 1. Account Configuration
In order for a seamless experience, there are a few things you need to configure in your account on the MyHours website.
1. Automatically Added To All New Projects
    - On Desktop:
        1. Log into your account at https://app.myhours.com
        2. On the left side of the window, click on the 'Team' tab, or click on 'Team members' under the 'Team tab'.
        3. Click on your name to open the member's settings.
        4. At the bottom of the settings page, enable the toggle for 'Automatically add this team member to all new projects'.
        5. Click the 'Save' button.

### 2. Modify The Config File
1. Locate the "config.ini" file in the "config/" folder and open it. You can use an IDE or Notepad works fine.
2. Enter your account login information as `name@email.com` not `"name@email.com"` (omitting the quotation marks).
3. Save the file.

## Usage
- Desktop App
    - [ ] Not Started
    - Instructions coming soon...
- BASH
    - [ ] Not Started
    - Instructions coming soon...
- Python CLI (crossplatform)
    - [x] Completed
    1. Launch myhoursapp.exe
    
## Frequently Asked Questions

### Can I have multiple timers running simultaneously?
No. I've tested it using the website's timer too. It would be cool, though..

### Program .exe automatically closes when launching it.
This is usually caused when the config.ini file isn't modified with your MyHours account credentials. Once you enter your credentials and save the config.ini file, it should launch fine. You can edit and save the file with an IDE or Notepad works just as well.

### How do I remove or delete a project?
As of right now, you can remove a project by logging into your MyHours account online.
1. Click on "Projects" tab on the left hand side.
2. Click on the project you wish to delete.
3. Click on the "..." button on the top right hand side of the page.
4. Delete or Archive project.

### How can I edit a timelog?
The ability to edit a timelog is constrained to those who are **subscribed** to a Pro Plan. You can access the website to edit the timelog.
If you are, you would successfully navigate "Retrieve Recent Logs">"E) Edit" and be able to save your edits.
**As of 3/27/24**, the only log variable to edit is its "note". 

## References

### Libraries
- pytz
- requests

### API Reference
My Hours API v1.1: https://documenter.getpostman.com/view/8879268/TVmV4YYU

### Github
Visit https://github.com/JermyNeutron/myhours-app