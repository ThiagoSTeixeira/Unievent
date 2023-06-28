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
        imageURL: require('@/assets/events/' + event.imageURL), 
        ownerImageURL: require('@/assets/owners/' + event.ownerImageURL) 
      }));
    })
    .catch(error => {
      console.error('Error fetching events:', error);
    });
}

  },
  computed: {
  sortedEvents() {
    return this.events.slice().sort((a, b) => a.date - b.date);
  }
}
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0 auto;
}

h1 {
  text-align: center;
}

.event-card {
  /* ...other styles... */
  display: flex;
  flex-direction: column;
  align-items: center;
}

.event-card img {
  width: 80%; /* Adjust this to make the image smaller or larger */
  height: auto; /* This will keep the aspect ratio of the image */
  object-fit: cover;
  border-radius: 15px;
  max-height: 200px; /* Adjust this to set a maximum height */
}

.event-card .date {
  font-size: 0.9rem;
  color: #6c757d;
  margin-bottom: 0.5rem;
}

.event-card .description {
  font-size: 1.1rem;
  color: #343a40;
}
</style>
