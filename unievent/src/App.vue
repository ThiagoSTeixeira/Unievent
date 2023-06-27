<template>
  <div id="app">
    <h1 class="title">Event Feed</h1>
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
        date: new Date(Date.parse(event.date || event.datetime)),
        imageURL: require('@/assets/events/' + event.imageURL) // Import the image using require
      }));
    })
    .catch(error => {
      console.error('Error fetching events:', error);
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

<style scoped>
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f8f9fa;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 2rem;
}

h1 {
  color: #343a40;
}

.event-post {
  width: 80%;
  max-width: 600px;
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background-color: white;
  margin-bottom: 1rem;
  padding: 1rem;
  overflow: hidden;
}

.event-post img {
  width: 100%;
  object-fit: cover;
  border-radius: 15px;
}

.event-post .date {
  font-size: 0.9rem;
  color: #6c757d;
  margin-bottom: 0.5rem;
}

.event-post .description {
  font-size: 1.1rem;
  color: #343a40;
}
</style>

