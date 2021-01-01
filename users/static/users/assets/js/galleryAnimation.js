
    const gridify = new Gridify();

const container = document.querySelector('.grid');

container.addEventListener('gridify:init', (ev) => {
  console.log('Init handler');
}, false);

container.addEventListener('gridify:resized', (ev) => {
  console.log('Resized handler');
}, false);

 $(document).ready(function () {
    $('#img1').animate({
      opacity: 1,

    }, "fast");
    setTimeout(function(){

      $('#img2').animate({
      opacity: 1,

    }, "fast");

    }, 50)
    setTimeout(function(){
    $('#img3').animate({
      opacity: 1,

    }, "fast");
  }, 50);
  setTimeout(function(){
    $('#img4').animate({
      opacity: 1,

    }, "fast");
  }, 50);
  setTimeout(function(){
    $('#img5').animate({
      opacity: 1,

    }, "fast");
  }, 50);
  setTimeout(function(){
    $('#img6').animate({
      opacity: 1,

    }, "fast");
  }, 50);
  setTimeout(function(){
    $('#img7').animate({
      opacity: 1,

    }, "fast");
  }, 50);
  setTimeout(function(){
    $('#img8').animate({
      opacity: 1,

    }, "fast");
  }, 50);
    
  });