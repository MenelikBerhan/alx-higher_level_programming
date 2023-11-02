// a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(function () {
// Handler for .ready() called.
  $.get(url, (data) => {
    $('div#hello').text(data.hello);
  });
});
