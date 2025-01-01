# five_in_a_row
Gomoku, or "Five in a Row," is a classic strategy game playable 1v1 or against a computer. Players can choose the board size. The goal is to align five pieces consecutively—horizontally, vertically, or diagonally. This game challenges strategic thinking and planning, offering a fun, intellectually stimulating experience.


# Install Dependensies
sudo yum update -y
sudo yum install python3 -y
sudo yum install python3-pip -y
sudo pip3 install --upgrade pip
sudo pip3 install flask gunicorn

# Edit Inbound Rules
sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
OR
Edit them on EC2 Dashboard

# Clone your repo to EC2
Connect to your instance
git clone < your git repo url >

# Run the Application on EC2 
sudo gunicorn --bind 0.0.0.0:80 gomukuflask:app
python3 gomukoflask .py

# Test Aplication

- Start Game
curl -X POST http://<ec2-public-ip>:5000/start_game \
-H "Content-Type: application/json" \
-d '{"size": 9, "player_mode": 1}'

- Place Stone
curl -X POST http://<ec2-public-ip>:5000/place_stone \
-H "Content-Type: application/json" \
-d '{"stone": "●", "position": [2, "B"]}'

- Print Board
curl -X GET http://<ec2-public-ip>:5000/get_board

