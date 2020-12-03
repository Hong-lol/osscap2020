# 개요
본 프로그램은 자동 수액 투액기의 투액 속도를 시각화해주는 포로그램입니다.\n 원하시는 속도를 설정하시고, 장치를 설정하시면, 설정값과 실시간 투액 속도가 화면에 출력됩니다. \n또한, 왼쪽에는 수액이 떨어지는 화면을 속도에 맞게 출력하여, 수액이 떨어지는 것을 led를 통해 한눈에 볼 수 있게 됩니다.

# 준비물

본 프로그램을 이용하기 위해서는, 조도 센서와 레이저 포인터가 필요합니다. \n 
이때, 레이저 포인터는 rasberry pi 에 연결 하실 필요는 없으시며, 조도선서와 rasberry pi에 link해주는 작업이 필요합니다. \n
또한, 본 프로그램의 정확도를 높이기 위해서, 원통형 수액 투액기에, 180도인 정확히 반대편에서, 조도센서의 센서부분에 레이저 포인터를 비추며, 물방울이 레이저 포인터를 지나가도록 장치해두어야 합니다.

# 실행방법

$ sudo apt-get update \n
$ sudo apt-get install rpi.gpio \n
$ mkdir program_name \n
$ cd program_name \n
$ git clone https://github.com/Hong-lol/osscap2020.git \n
$ cd osscap2020\n
$ sudo python3 file.py\n

