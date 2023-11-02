// a JavaScript script that fetches and prints how to say “Hello” depending on the language
// uses this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when
//      the focus is on INPUT#language_code
// The translation of “Hello” must be displayed in the HTML tag DIV#hello

function setTranslation () {
  const url = 'https://hellosalut.stefanbohacek.dev/';
  const langInput = $('input#language_code').val();
  const reqData = { lang: langInput };
  $.get(url, reqData, (data) => {
    $('DIV#hello').text(data.hello);
  });
}

function myfunc () {
  $('INPUT#btn_translate').on('click', setTranslation);

  $('INPUT#language_code').on('keydown', function (event) {
    if (event.key === 'Enter') setTranslation();
  });
}

window.onload = myfunc;
