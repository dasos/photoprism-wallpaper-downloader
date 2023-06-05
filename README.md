# photoprism-wallpaper-downloader
A Python script that connects to a Photoprism server, and downloads a few random files. 

This is useful if, like me, you want to use some of these photos as a wallpaper. I call this script from a cron job, so that a few files get downloaded. Then Windows or Mac OS or whatever then picks a few photos from this directory to set as wallpaper.
## How to get going
This is what I recommend you do
 - Clone the directory using git: `git clone https://github.com/dasos/photoprism-wallpaper-downloader` (or just grab the script)
 - Add config. See what is needed with `python3 wallpaper.py -h`
   - [ConfigArgParse](https://github.com/bw2/ConfigArgParse) is used. So you can create your own config file, or use environment variables, or use command line options.
   - I create a config file in my home directory, then pass it to the script with `python3 wallpaper.py -c ~/photoprism-wallpaper-downloader.conf`
 - Set up a cron job, or Windows Task Scheduler or whatever to run the script
 - Set up Windows and Mac OS to look in the folder you've chosen in the config.
 - Enjoy your photos!