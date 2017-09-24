
var n_grid = 4
var num_list = Array.from(new Array(n_grid * n_grid), (x,i) => Math.floor((i + 1)/2))

num_list = shuffle(num_list)
console.log(num_list)  // checked!

var cards = manydiv('card', num_list)
console.log(cards)


// parameters for game information
var click = 0
var first_card = null
var second_card = null

$('.board').html(cards)

$('.card').click(function(){
    var clicked = $(this)
    var chosen_number = clicked.text()
    console.log('Card ' +  chosen_number + ' clicked!.')

    if (!clicked.hasClass('opened')) {

        if (second_card != null) {
            first_card.toggleClass('front')
            second_card.toggleClass('front')
            first_card = null
            second_card = null
        }

        if (first_card == null) {
            clicked.toggleClass('front')
            first_card = clicked
            click++
    
        } else if (second_card == null && this != first_card ) {
            console.log('You chose second card!')
            clicked.toggleClass('front')
            second_card = clicked
            click++

            var num1 = first_card.text()
            var num2 = second_card.text()

            if (num1 == num2) {
                first_card.addClass('opened')
                second_card.addClass('opened')
            } 

        }

        $('span').text(click)

    }

});

function shuffle(array) {
    for (var i = 1; i < array.length; i++) {
        var j = Math.floor(Math.random() * (i+1));
        [array[i], array[j]] = [array[j], array[i]]
    }
    return array;
}

function manydiv(class_name, array) {
    var div_str = ''
    var head = '<div class="' + class_name + '">'
    var tail = '</div>'
    for (var i = 0; i < array.length; i++) {
        div_str += head + array[i] + tail
    }
    return div_str
}
