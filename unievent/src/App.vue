<template>
  <div id="app">
    <div class="navbar">
      <img src="@/assets/logo.png" alt="Logo" class="logo"/>
      <input type="text" placeholder="Search..." class="search"/>
      <div class="buttons">
        <button class="btn login" @click="handleLogin">Log In</button>
        <button class="btn join" @click="handleJoin">Join</button>
    </div>
  </div>

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

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.2em 1em;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: fixed;
  width: 100%;
  max-width: 97%; /* Adjust this to set a max width for the navbar */
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.navbar-right {
  display: flex;
  gap: 1em; /* add gap between buttons */
  margin-right: 2em; /* adjust right margin as needed */
}
.logo {
  width: 100px;
  height: auto;
}

.search {
  flex-grow: 1;
  margin: 0 1em;
  padding: 0.5em;
  border: none;
  border-radius: 4px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.buttons {
  display: flex;
  gap: 1em;
}

.btn {
  padding: 0.5em 1em;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}

.btn.login {
  background-color: #6c757d;
}

.btn.login:hover {
  background-color: #5a6268;
}

body {
  padding-top: 50px;  /* Height of the navbar, adjust as needed */
}

</style>
