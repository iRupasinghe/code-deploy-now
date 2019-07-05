git clone https://github.com/AnushkaYohan/code-deploy-now.git
cd ./code-deploy-now/
python3 setup.py install
echo "Invoke deploynow module by running:\t python3 -m deploynow -h"
cd ..
rm -rf ./code-deploy-now/