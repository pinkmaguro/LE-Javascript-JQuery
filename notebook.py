@D 2017-0924
Learning 자바 스크립트 & JQuery
웹 애플리케이션을 만들려면 html, css, javascript 만으로는 부족하다고 느꼈다.

반나절에 걸처서 JQuery 학습 동영상을 보고 조금 친숙해졌다.

마우스 액션으로 객체의 클래스를 추가/제거 해서 스타일을 조정하는 방법을 배웠다.

@Goal 같은 숫자 카드 맞추기 게임 만들기
@T 블록 행력
숫자를 두 번 뒤집어서 같은 숫자를 맞추는 게임을 만들어 볼려고 한다.
JQuery 를 코딩해본 경험이 없어서 흐릿한 아이디만 있다.
N 을 입력 받으면 N x N 의 div 박스를 만들어야 하는데 열의 갯수를 어떻게 조절해야하는지 모른다.
우선 보드의 크기는 5x5 로 고정하자.

@T 카드 뒤집기
뒤집어서 숫자가 보여야 한다. card 라는 클래스의 하위에 front / back 이라는 클래스를 만들어서 구분하면 될 것 같다.
뒤집는 애니메이션은 css 쪽에서 처리해야 할 것 같다.  
자료를 찾아봐야겠다.

@T 게임 데이터 저장
게임 데이터는 js 파일에 javascript 변수로 저장하면 될 것 같다.


@PM- 그리드 형태의 박스 만들기
<div></div> 를 연속해서 사용했는데
@Fix 실패의 원인을 찾았다. <div class='board'></div> 사이에 카드 div 가 와야하는데 append 또는 after 는 </div> 뒤에
태그를 추가하기 때문에 부적절했다.


@PM-F toggleClass(...) 명령이 실행되기 전에 시간 지연을 두기. 어떻게 해야하나?
검색결과 setTimeout / delay  를 사용하라고 되어 있지만 작동하지 않았다.
@Fix 이 문제를 우회적으로 해결했다. delay 를 주어야하는 시점 이후의 액션이 이루어진 이후에 
delay 에서 처리해야 하는 액션을 하게 했다.
delay(300) -> A -> event -> B 이어야 하는 것을
event -> A -> B 로 바꿨다.
A -> B 순서만 유지되면 치명적인 문제는 아니다.