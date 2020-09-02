if [ -f "ngrok" ];
then echo "Checking ngrok"
else echo "Please download ngrok https://ngrok.com/download", exit 0
fi 
# x-terminal-emulator -e bash ngrok.shss #for linux
osascript -e 'tell application "Terminal"
 do script "cd Desktop/ciscobot/webex ;bash ngrok.sh"
 end tell'
sleep 5
source venv/bin/activate
pip install apscheduler==2.1.2
pip install webexteamsbot
python webexBot.py