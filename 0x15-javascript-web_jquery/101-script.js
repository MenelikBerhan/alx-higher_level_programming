/* a JavaScript script that adds, removes and clears LI elements from
a list when the user clicks:
    - The new element must be: <li>Item</li>
    - The new element must be added to UL.my_list
    - When the user clicks on DIV#add_item: a new element is added to the list
    - When the user clicks on DIV#remove_item: the last element is removed from the list
    - When the user clicks on DIV#clear_list: all elements of the list are removed */

function myfunc () {
  const item = '<li>Item</li>';
  $('div#add_item').on('click', () => $('ul.my_list').append(item));

  $('div#remove_item').on('click', () => $('ul.my_list > li').last().remove());

  $('div#clear_list').on('click', () => $('ul.my_list').empty());
}

window.onload = myfunc;
