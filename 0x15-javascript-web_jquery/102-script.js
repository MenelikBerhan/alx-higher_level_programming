// a JavaScript script that fetches and prints how to say “Hello” depending on the language

// Uses this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation will be fetched when the user clicks on INPUT#btn_translate
// The translation of “Hello” must be displayed in the HTML tag DIV#hello

function myfunc () {
  $('INPUT#btn_translate').on('click', () => {
    const url = 'https://hellosalut.stefanbohacek.dev/';
    const langInput = $('input#language_code').val();
    const reqData = { lang: langInput };
    $.get(url, reqData, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
}

window.onload = myfunc;
