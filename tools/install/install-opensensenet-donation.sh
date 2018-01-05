#! /bin/sh

INSTALL_DIR=/opt/opensensenet
GIT_URL="git://github.com/maroulb/data-donation.git#envirophat_agent"
#GIT_URL="https://github.com/opensense-network/data-donation.git"
LOG_FILE=$INSTALL_DIR/log/opensensenet-donation.log
CONFIG_FILE=$INSTALL_DIR/config/opensensenet-donation.config.json
USER=opensense


echo "Installing git"
sudo apt-get install -y git
sudo adduser --system --no-create-home --group --disabled-password --disabled-login $USER
echo "Installing Opensensenet Donation Environment to $INSTALL_DIR..."
sudo mkdir $INSTALL_DIR
sudo chown $USER:$USER $INSTALL_DIR
#cd $INSTALL_DIR
echo "Cloning git from $GIT_URL ..."
sudo -u $USER git clone $GIT_URL $INSTALL_DIR
# this should in the future not be downloaded at all:
echo "Installing Service..."
sudo cp $INSTALL_DIR/tools/init.d-script/opensensenet-donation /etc/init.d
sudo chmod 755 /etc/init.d/opensensenet-donation
sudo update-rc.d opensensenet-donation defaults
echo "Starting Service and waiting some seconds..."
sudo /etc/init.d/opensensenet-donation start
sleep 5
echo "Here are the last 20 lines of the logfile ($LOG_FILE):"
tail -n 20 $LOG_FILE
echo " "
echo "Installation Done. You may now want to activate donation agents in $CONFIG_FILE - And don't forget to restart the service via \"sudo /etc/init.d/opensensenet-donation restart\" afterwards :-)"
