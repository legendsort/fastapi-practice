`pyenv`macOS에서 Homebrew로 설치 고려

```
brew update
brew install pyenv
```

**또는** 저장소를 복제하여 최신 버전의`pyenv`

```
 git clone https://github.com/pyenv/pyenv.git ~/.pyenv

```

환경 변수 정의

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
```

경로 변경 사항이 적용되도록 셸을 다시 시작합니다.

```
exec "$SHELL"

```

설치 확인 및 사용 가능한 `python`버전 확인

```
pyenv install --list

```

필요한 `python`버전 설치

```
pyenv install 3.7

```

설치 후 글로벌 버전으로 설정

```
pyenv global 3.7

```

`python`시스템에서 사용 중인 현재 버전 확인

```
python3 --version
```

그럼에도 안되는경우

새로운 Homebrew pyenv 릴리스를 기다리거나 직접 릴리스를 만들어 Homebrew로 가져오거나 pyenv의 마스터 브랜치를 설치해야 합니다.

pyenv 및 3.8.3의 마스터 브랜치를 설치하려면:

```
brew unlink pyenv
brew install pyenv --head
pyenv install 3.8.3
```

c컴파일 문제시 xcode-select —install

- 그럼에도 안될때
    
    ### 2. 설치된 위치를 확인하기
    
    ```
    ls -l /usr/local/bin/python*
    ```
    
    그러면 이런 식으로 어디에 어떤 python이 설치되어 있는지 나오게 됩니다.
    
    이제 여기서 하나를 골라서 어떤 버전으로 사용할지 결정해주면 됩니다.
    
    ### 3. 파이썬 버전 변경하기
    
    ```
    ln -s -f /usr/local/bin/python3.9 /usr/local/bin/python
    ```
    
    여기서 만약 버전 3.7로 바꾸고 싶다면 python3.7로, 버전 3으로 바꾸고싶다면 python3으로 바꾸면 됩니다.
    
    저는 제일 최신 버전인 3.9로 바꿔보았어요  ~
    

## **가상환경 생성하는 법**

예를 들어 바탕화면에 “my_project”라는 폴더를 만들어 작업을 한다면, 그 폴더 안에서 `python -m venv 가상환경이름`이라고 쳐주면 된다.

`pip install fastapi
pip install uvicorn[standard]`

`pip install pymongo`