// a JavaScript script that adds a <li> element to a list
// when the user clicks on the tag DIV#add_item
// The new element will be: <li>Item</li>
// The new element will be added to UL.my_list
$('DIV#add_item').on('click', () => {
  $('UL.my_list').append('<li>Item</li>');
});
