(function(document, window, $, moment) {
  $(document).ready(function() {
    var cache = {};

    var calendar = $('#calendar');

    function mapCalendarData(data) {
      return $.map(data, function(item){
        return {
          title: item.fields.title,
          end: item.fields.end_time,
          start: item.fields.start_time,
          id: item.pk
        };
      });
    }
    function updateCalendar(date) {
      var cacheKey = date.format('MM-YYYY');
      var cacheItem = cache[cacheKey];
      if (!cacheItem) {
        cache[cacheKey] = [];
        $.getJSON('json/', {
          year: date.format('YYYY'),
          month: date.format('MM')
        }).done(function(fullCalendarData) {
          var mapped = mapCalendarData(fullCalendarData);
          cache[cacheKey] = mapped;
          calendar.fullCalendar('addEventSource', mapped);
        });
      }
    }

    function initCalendar() {
      var currentDate = moment();
      var cacheKey = currentDate.format('MM-YYYY');
      calendar.fullCalendar({
        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,basicWeek,basicDay'
        },
        defaultDate: currentDate,
        timezone: 'local',
        timeFormat: 'H:mm',
        editable: true,
        eventLimit: true,
        eventClick: function(eventObj) {
          document.location = window.location + eventObj._id;
        },
        viewRender: function(view) {
          updateCalendar(view.intervalStart);
        }
      });
    }
    initCalendar();
  });
})(document, window, jQuery, moment);
