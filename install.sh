#/bin/bash
sudo cp fan_control.service /etc/systemd/system/fan_control.service
sudo systemctl daemon-reload
sudo systemctl enable fan_control.service
sudo systemctl start fan_control.service