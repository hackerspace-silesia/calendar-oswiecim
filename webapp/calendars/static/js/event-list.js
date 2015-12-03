(function(document, window, $, moment) {
  $(document).ready(function() {
    var cache = {};

    var calendar = $('#calendar');

    function mapCalendarData(data) {
      return $.map(data, function(item){
        var on = moment.parseZone(item.fields.start_time); // start moment
        var off = moment.parseZone(item.fields.end_time); // stop moment
        var diff = moment.duration(moment(off).diff(on)); // event duration
        return {
          title: item.fields.title,
          end: item.fields.end_time,
          start: item.fields.start_time,
          id: item.pk,
          allDay: diff.asHours() > 23 ? true : false // if > 23 assume it's allDay event
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
          left: 'today',
          center: 'prev, title, next',
          right: 'month, basicWeek, agendaDay'
        },
        defaultDate: currentDate,
        timezone: 'local',
        timeFormat: 'H:mm',
        editable: false,
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
