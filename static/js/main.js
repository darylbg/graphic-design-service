const options = {
  type: 'carousel',
  perView: 1.5,
  gap: 130,
  autoplay: 5000 | true,
  breakpoints: {
    1500: {
      gap: 70,
      perView: 1.3
    },
    1200: {
      gap: 100,
      perView: 1.1
    }
  }
}

new Glide('.glide', options).mount()

$(document).ready(function() {
  $('.option').select(function() {

    var total = 0;

    $('.option:selected').each(function() {

        total += parseInt($(this).val());

    });

    $('#total').html('£' + total);

  });
});
