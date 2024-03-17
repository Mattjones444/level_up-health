$(document).ready(function(){
    $('select').formSelect();
  });
    

$( "a" ).on( "click", function() {
  $('#edit{{ Exercise_intentions.id}}').modal();
  $('.datepicker').datepicker();
});