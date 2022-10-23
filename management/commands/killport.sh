
echo 'Which Port you want to check status ? '

read portnumber

sudo lsof -i tcp:"$portnumber"
#or
sudo lsof -t -i tcp:"$portnumber" | sudo xargs kill

echo 'PORT DELETED SUCCESSFULLY '