(function(document, window, $, moment) {
  $(document).ready(function() {
    var currentDate = moment();

    var calendar = $('#calendar');
    calendar.fullCalendar({
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,basicWeek,basicDay'
      },
      defaultDate: currentDate,
      editable: true,
      eventLimit: true,
      eventClick: function(eventObj) {
        console.log(event);
        document.location = window.location + eventObj._id;
      }
    });

    $.getJSON('json', {
      year: currentDate.format('YYYY'),
      month: currentDate.format('MM')
    }).done(function(fullCalendarData) {
      var mappedCollection = [];
      for (var i = 0; i < fullCalendarData.length; i++) {
        mappedCollection.push({
          title: fullCalendarData[i].fields.title,
          end: fullCalendarData[i].fields.end_time,
          start: fullCalendarData[i].fields.start_time,
          id : fullCalendarData[i].pk
        });
      }
      // calendar.fullCalendar('renderEvent', mappedCollection);
      for (var y = 0; y < mappedCollection.length; y++) {
        calendar.fullCalendar('renderEvent', mappedCollection[y]);
      }
    });
  });
})(document, window, jQuery, moment);
