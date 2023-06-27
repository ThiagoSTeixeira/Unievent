<template>
  <div id="app">
    <h1>Event Feed</h1>
    <div class="event-feed">
      <EventPost v-for="event in sortedEvents" :key="event.id" :event="event" />
    </div>
  </div>
</template>

<script>
import EventPost from './components/EventPost.vue';

export default {
  name: 'App',
  components: {
    EventPost
  },
  data() {
    return {
      events: []
    }
  },
  created() {
    this.fetchEvents()
  },
  methods: {
    fetchEvents() {
      fetch('http://localhost:5000/api/events') // replace with your API endpoint
        .then(response => response.json())
        .then(data => {
          this.events = data.map(event => ({
            ...event,
            date: new Date(Date.parse(event.date || event.datetime))
          }));
        });
    }
  },
  computed: {
    sortedEvents() {
      return this.events.slice().sort((a, b) => b.date - a.date);
    }
  }
}
</script>
