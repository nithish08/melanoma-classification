sudo yum install htop
export PATH=/home/ec2-user/anaconda3/bin:$PATH
source ~/.bashrc
conda activate python3
pip install --upgrade pip
pip install fastai2
pip install --upgrade kaggle
mkdir ~/.kaggle
echo "{"username":"nithish007","key":"3f8c1f608fe1ed3f217cc1ca3d857134"}" > ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
export KAGGLE_USERNAME=nithish007
export KAGGLE_KEY="3f8c1f608fe1ed3f217cc1ca3d857134"
git config --global user.name "nithish08"
git config --global user.email "nithishreddy777@gmail.com"