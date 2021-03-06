@T HTML 주석
<!-- comment here -->

@T JQuery 사용 선언하는 법
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script> << 높은 버전

@PM JQuery 다운받은 파일을 사용할 떄 작동하지 않는다.
<script src="jquery-3.2.1.min.js"></script> << 작동 안함
<script type="text/javascript" src="js/jquery-1.10.2.min.js"></script> << 작동함

@Code 마우스 클릭한 DOM 객체의 클래스를 변경해서 배경색 바꾸기
----
    <script type="text/javascript">
        (function($) {
            $('#navigation li').live('click', function(event) {
                console.log('Clicked - #navigation li - ' + $(this).text())
            $('#navigation li').removeClass('selected');
            $(this).addClass('selected');
        })})(jQuery)
    </script>
----
- 클릭 이벤트는  .live('click', function(){}) 로 잡는다.  .live(events, handler)
- 다른 이벤트로는 'mouseover, mouseout' 이 있다.
- 선택된 객체는 this 로 호출할 수 있다.
- 
- 객체를 선택하면 그 객체의 text 를 콘솔로 출력해서 알린다.
- JQuery 구문을 wrapper 를 사용해서 선언했다. 보통은 $.('#navigation li') 와 같이 사용해도 무방하다.
- 클래스 제거에는 'removeClass('class1 class2')' 를 사용한다. 클래스 이름을 지정하지 않으면 모든 클래스가 제거된다.
- 클래스 추가에는 'addClass('class1 class2')' 를 사용한다.
----

@Code 여러 live 이벤트 를 한 번에 딕셔너리 형태로 지정하기
----
    $( "p" ).live({
    click: function() {
        $( this ).after( "<p>Another paragraph!</p>" );
    },
    mouseover: function() {
        $( this ).addClass( "over" );
    },
    mouseout: function() {
        $( this ).removeClass( "over" );
    }
    });
----

@Code 여러 live 이벤트 를 한 번에 딕셔너리 형태로 지정하기 예
----
    <script type="text/javascript">
        $('#navigation li').live(
            {'click': function(event) {
                console.log('Clicked - #navigation li - ' + $(this).text())
                $('#navigation li').removeClass('selected hover');
                $(this).addClass('selected');
            },
            'mouseover': function(event) {
                console.log('Mouse over - ' + $(this).text())
                $('#navigation li').removeClass('hover');
                if (!$(this).hasClass('selected')) {
                    $(this).addClass('hover')
                }
            },
            'mouseout': function(event) {
                console.log('Mouse out - ' + $(this).text())
                $(this).removeClass('hover');
            }
        }
    );
----
- 마우스를 올려놓은 객체가 selected 상태가 아니면 hover 상태로 만든다.
- 즉 selected 상태의 객체는 클릭 이벤트로만 클래스가 변경되고 그 외의 객체는 마우스의 over/out 이벤트로 상태가 바뀐다.
----

@Code JQuery 구문에서 CSS 속성을 직접 지정하기
----
    $('ul.foo').click( function() {
        $('li', this).css('background-color','red');
    });
----

@T 선택자
- $('*').removeClass('selected');   모든 객체?
- id 선택자   #id
- class 선택자 .class
- 엘리먼트 선택자  li
- 다중 선택자 #jquery, #MYSQL
- 일치하는 인덱스로 선택  #list li:eq(2)   인덱스를 상요할 때는 콜론(:)을 사용함
- 인덱스 크기로 선택 #list li:gt(1) / lt(2)    
- 인덱스 홀짝으로 선택 #list li:even / odd
- 인덱스 순서로 선택 #list li:first / second / last
- 속성으로 선택 ^ 포함 : [attr *='BC']
- 속성으로 선택 ^ 일치 : [attr ='ABCD']
- 속성으로 선택 ^ 불일치 : [attr !='ABCD']
- 속성으로 선택 ^ 시작 일치 : [attr ^='ABCD']
- 속성으로 선택 ^ 마지막 일치 : [attr $='ABCD']
- 속성으로 선택 ^ 속성 유무 : [attr] / [attr1][attr2]

@T 체인 규칙 | chain rule
@Code 
----
    <script type='text/javascript'>
        $('ul.first').find('.foo').css('background-color','red').end()
        .find('.bar,').css('background-color', 'blue').css('color','white')
    </script>
----
- end() 로 이전 선택으로 돌아감
- 이렇게 복잡하게 사용할 이유는 없다.
- 순서에 따른 로직을 적용시키고 싶으면 이 로직에 대한 책임을 다른 곳(선택자, 자바스크립트)에 부담시켜야 한다.
----

@T 이벤트 바인딩
@Code 
----
    $(document).bind('ready', function(){
            $('#click_me').bind('click', clickHandler);
            $('#remove_event').bind('click', function(e){
                $('#click_me').unbind('click', clickHandler);
            });
            
            $('#trigger_event').bind('click', function(e){
                $('#click_me').trigger('click');
            });
        })
----
$(document).bind('ready', function(){...})
- HTML 문서가 로딩되면 다음 함수를 수행하라는 의미인 것 같다.
- bind 는 event 와 handler 를 연결시켜 준다.
- unbind 는 연결을 해제시킨다.
- trigger 는 이벤틀르 발생시킨다.
----
@T 엘리먼튼 이후에 HTML 태그 추가, HTML 태그로 감싸기
@Code
----
    $("p:eq(0)").append("<strong> - Okarina </strong>");
    $("p:eq(1)").after("<strong> - Muzura </strong>");
    $("strong").wrap("<I></I>");
----
- before 도 있겠지
- wrap 은 되도록 사용하지 말자.  wrap 으로 지정하는 것은 스타일인데 addClass 로 충분히 다룰 수 있다.
----

@T 클래스 추가/제거 하는 또 다른 방법 토글 (toggleClass(...))
@Code 
----
    <div>
        <p class='blue'>item 1</p>
        <p class='blue'>item 2</p>
        <p class='blue'>item 3</p>
        <p class='blue'>item 4</p>
        <script>$('div p').click(function(){$(this).toggleClass('highlight')});</script>
    </div>
----

@T Keyup 이벤트
@Code
----
    $("#typehere").keyup( function () {
        var value = $(this).val();
        $("p:last").text(value);
    }).keyup();
----

@T form 다루기
@Code
----
    $("form").submit( function() {
        if ($("input:first").val() == "correct") {
            $("span").text("Validated...").show();
            return true;
        }
        $("span").text("Not valid!").show().fadeOut(1000);
        return false;
    });
----
- form 객체에 대해서는 submit 함수를 호출한다.  
- submit handler ?  는 boolean 값을 리턴한다.
- text(...) 로 HTML 에 텍스트를 추가하면 show() 를 추가 호출해야지 제대로 동작한다.
- faddOut(1000) 은 애니메이션 이벤트로 1초 동안 천천히 내용이 사라진다.
----

@T input 이벤트
@Code
----
    $("input").focus( function () {
        $(this).next("span").html('focus');
    }).blur( function() {
        $(this).next("span").html('blur');
    }).change(function(e){
        alert('change!! '+$(e.target).val());
    }).select(function(){
        $(this).next('span').html('select');
    });
----
- input 에 대해서는 foccus / blur / change / select 이벤트 핸들러를 지정할 수 있다
- 각각의 함수의 리턴 값은 객체이므로 체인 연결 방식으로 코드를 작성할 수 있다.
- (선택자).next(...) 는 선택자 이후에 오는 객체를 선택한다.
- event.target 으로 이벤트가 발생한 객체를 선택할 수 있다.
- 객체에 텍스트 내용이 저장되어 있다면 val() 함수로 그 내용을 불러올 수 있다.
----

@T 애니메이션
@Code
----
                $("#go").click( function() {
                    $("#block").animate({
                        width: "300px",
                        opacity: 0.4,
                        marginLeft: "50px",
                        fontSize: "30px",
                        borderWidth: "10px"
                    }, 3000);
----

@Cdoe
----
        <script>$('input[type="button"]').click( function(e) {
                var $this = $(e.target);
                switch($this.attr('id')) {
                    case 'fadeout':
                        $('#target').fadeOut('slow');
                        break;
                    case 'fadein':
                        $('#target').fadeIn('slow');
                        break;
                    case 'hide':
                        $('#target').hide();
                        break;
                    case 'show':
                        $('#target').show();
                        break;
                    case 'slidedown':
                        $('#target').hide().slideDown('slow');
                        break;
                    case 'slideup':
                        $('#target').slideUp('slow');
                        break;
                    case 'mix':
                        $('#target').fadeOut('slow').fadeIn('slow').delay(1000).slideUp().slideDown('slow', function(){alert('end')});
                        break;
                }
            }) 
        </script>
----
- 'input[type="button"]' 에서 바깥 따옴표와 안쪽 따옴표는 다른 종류를 사용해야하며 그러면 type 을 지정할 떄 어떤 따옴표를 사용해도 선택할 수 있다.
- 이벹트가 발생한 객체를 가져와서 변수에 저장한다.
- swtich 문에서의 인자는 스트링이다.
- 애니메이션 액션은 hide() 와 show() 면 충분하다.

----

@T Ajax
@Code
----
  $.ajax({
    url: '/_predict',
    type: 'POST',
    data: JSON.stringify(sendData),
    dataType:'json',
    contentType: 'application/json; charset=UTF-8',
    success: function(data){
      console.log("result!!!!!");
      console.log(data)
      $('#result').html("<H1>"+data+"</H1>").css("color","red");
    },
    error: function(error_msg){
    }
  })
----

@T grid 만드는 법 중의 하나
@Code
----
        .broard {
            width: 600px;
            display: grid;
            grid-gap: 10px;
            grid-template-columns: repeat(5, 100px);
            grid-template-rows: repeat(5, 100px);
            grid-auto-flow: row;
            }
----

@T 이벤트의 종류
@T- 마우스 이벤트
- 클릭  click()
- 더블클릭  dbclick()  
- 움직임 mousemove()
- 겹침 hover()
- 벗어남 mouseleave()

- mouseout()  ?

@T <a> 태그의 액션을 막는 방법
- 클릭 이벤트 함수가 false 를 리턴하게 한다.
- 클릭 이벤트에 대해서 preventDefaut() 함수를 호출한다.

@T 왠만한 이벤트 메쏘드는 두 가지 기능이 있는 것 같다.
mouseover() 는 선택한 요소에 마우스를 올릴 때 이벤트를 발생시키기도 하고,
선택한 요소에 마우스를 올려놓는 이벤트를 발생시키기도 한다.

@Code
----
        $('#btn2').hover(function (){
            console.log('button2 hover event')
            
            $('P').css('background-color', 'green')
        }, function(){
            $('P').css('background-color', 'aqua')
        });
----
- hover 의 경우에는 mouseover 와 mouseout 이벤트에 대한 함수를 연속해서 써줄 수 있다.
- live 와 bind 의 차이점은 무엇일까? 이벤트 동작에 대해서는 바꿔써줘도 변화가 없다.
----

@T mouseover, mouseout 과 mouseenter, mouseleaver 의 차이점
전자는 선택 요소를 기준 후자는 선택 요소의 경계를 기준으로 이벤트를 발생시킨다.
예를들어 ul 안에 li 가 있을 떄 mouseleave 는 리스트 전체의 범위를 벗어나야지 이벤트를 발생시키지만
mouseout은 ul 에서 li 로 마우스가 이동했을 때도 이벤트를 발생시킨다.

@T 사용자 편의를 위해서 키보드와 마우스 이벤트를 같이 처리하는 것이 좋다고 한다.

@T 키보드 이벤트 : keydown, keyup, keypress
- keydown 이벤트에서는 눌러진 자판에 대한 고유 키코드 값을 받아올 수 있지만
keypress 이벤트에서는 할 수 없다.
- 고유키 값이라면.. a 를 입력하면 키보드 이벤트는 A 이고 입력된 문자는 a 이다.
shift 키를 누는 것은 keydown 으로 키보드 값을 얻을 수 있지만 실제 어떤 문자가 입력되는 것은 아니므로 
keypress 이벤트로는 shift 키에 대한 이벤트를 받아올 수 없다.

@T 그룹 이벤트 등록 및 삭제하기
- on() : 선택한 요소에 한 개 이상의 이벤트를 등록. 제이쿼리 1.7 이상부터 지원
        동적으로 생성된 이벤트를 등록한 요소와 동일한 새 요소에도 이벤트가 등록됨
- live() : on()과 비슷함 제이쿼리 1.9 부터는 지원하지 않음
- bind() : 이역시 한 개 이상으 ㅣ이벤트를 등록할 수 있음.
- delegate() : 선택한 요소에 지정한 하위 요소에 이벤트를 등록.

@T on 함수는 1.7 부터 지원함

@T Ajax 관련 메쏘드
- load()
- $.ajax()  데이터를 서버에 전송 가능. HTML, XML, JSON, 텍스트 유형의데이터를 요청할 수 있는 메쏘드,  
$.post(), $.get(), $getJSON() 기능을 합쳐놓은 것
- serialize() 'name1=value1&name2=value2...' 쿼리 스트링 형식의 데이터로 전송
- serializeArray() key1:val1,key2:val2... JSON 데이터로 변환하여 액션 페이지에 전송
- .ajaxSuccess(func(){}) ajax 요청이 성공적으로 완료되면 함수를 실행함

@T $.ajax()
----
$.ajax({
url : '전송 페이지'
type: '전송 방식'
data: '전송할 데이터'
dataType: '요청한 데이터 타입' (html, xml, json, text, jsonp)
success: function(result) { }  # result 는 요청한 데이터
});
----

@T ajax 테스트
https://jsonplaceholder.typicode.com/


