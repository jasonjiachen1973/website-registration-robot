Create Website Registration Robot

Steps:

1. 创建 Python 虚拟环境

查看当前系统中的python版本
pyenv versions

安装不同的python版本
pyenv install -v 3.8.1

删除一个版本
pyenv uninstall 3.11.0rc2

切换python 版本
pyenv global 3.8.1

创建虚拟环境
pyenv virtualenv 3.11.5 booking_app

查看虚拟环境
pyenv virtualenvs

激活虚拟环境
pyenv activate booking_app

退出虚拟环境
pyenv deactivate

删除虚拟环境

pyenv virtualenv-delete booking_app




2. 创建 Python 虚拟环境
 
 pip install -r requirements.txt  if you have the requirements.txt

 or  pip install streamlit selenium

对于 M1/M2/M3 Mac，需要安装 chromedriver，否则 selenium 不能运行：

brew install chromedriver

3. 运行 Streamlit 应用
确保 虚拟环境激活 后，运行：

streamlit run main.py
