<template>
  <div id="app">
    <div class="navbar">
      <img src="@/assets/logo.png" alt="Logo" class="logo"/>
      <input type="text" placeholder="Search..." :class="['search', isLoggedIn ? 'search-logged-in' : 'search-logged-out']"/>
      <div class="buttons" v-if="!isLoggedIn">
        <button class="btn login" @click="showLoginModel">Log In</button>
        <button class="btn join" @click="handleJoin">Join</button>
      </div>
      <div class="user-section" v-else>
        <button class="btn create-event" @click="showCreateEventModal">Create Event</button>
        <img class="user-profile" src="@/assets/owners/uspcodelab.png" alt="User Profile">
      </div>
      <LoginModel ref="LoginModel" @login-success="handleLoginSuccess" />
      <CreateEventModal ref="CreateEventModal" />
    </div>
    
    <h1 class="title">Event Feed</h1>
    <div class="event-feed">
      <EventPost v-for="event in sortedEvents" :key="event.id" :event="event" />
    </div>
  </div>
</template>

<script>
import EventPost from './components/EventPost.vue';
import LoginModel from './components/LoginModel.vue';
import CreateEventModal from './components/CreateEventModal.vue';

export default {
  name: 'App',
  components: {
    EventPost,
    LoginModel,
    CreateEventModal,
  },
  data() {
    return {
      events: [],
      isLoggedIn: false
    }
  },
  created() {
    this.fetchEvents()
  },
  methods: {
    handleJoin() {
      // handle join logic here
      console.log('Join button clicked');
    },
    showLoginModel() {
      this.$refs.LoginModel.showLoginModel();
    },
    handleLoginSuccess() {
      this.isLoggedIn = true;
    },
    showCreateEventModal() {
      this.$refs.CreateEventModal.showCreateEventModal();
    },
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
  margin: 0 1em;
  padding: 0.5em;
  border: none;
  border-radius: 4px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search-logged-out {
  flex-grow: 1;
}

.search-logged-in {
  flex-grow: 0.95; /* adjust this as needed */
}

.buttons {
  display: flex;
  align-items: center;
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
.btn.create-event {
  background-color: #54bb00;
}
body {
  padding-top: 50px;  /* Height of the navbar, adjust as needed */
}

.user-profile {
  width: 40px;   /* Adjust the size as needed */
  height: 40px;  /* Adjust the size as needed */
  border-radius: 50%;  /* Makes the image circular */
  object-fit: cover;   /* Makes the image cover the entire element without distortion */
  margin-left: 10px;   /* Optional: Add some space between the button and the image */
}

.user-section {
  display: flex;
  align-items: center;  /* This will vertically align the contents within the user-section */
  gap: 1em;
}


</style>
