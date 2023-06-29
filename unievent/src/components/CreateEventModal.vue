<template>
    <div class="create-event-modal" v-if="isCreateEventModalShown">
      <div class="create-event-modal-content">
        <h2>Create Event</h2>
        <label for="event-title">Event Title:</label>
        <input id="event-title" type="text" v-model="event.title">
        
        <label for="event-datetime">Event Date & Time:</label>
        <input id="event-datetime" type="datetime-local" v-model="event.datetime">
        
        <label for="event-description">Event Description:</label>
        <textarea id="event-description" v-model="event.description"></textarea>
        
        <label for="event-image">Event Image:</label>
        <input id="event-image" type="file" @change="handleFileChange">
        
        <button @click="handleCreateEvent">Submit</button>
        <button @click="isCreateEventModalShown = false">Close</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isCreateEventModalShown: false,
        event: {
          title: '',
          datetime: '',
          description: '',
          imageFile: null
        }
      };
    },
    methods: {
      showCreateEventModal() {
        this.isCreateEventModalShown = true;
      },
      handleFileChange(event) {
        this.event.imageFile = event.target.files[0];
      },
      handleCreateEvent() {
        // handle your event creation logic here
        // remember to set isCreateEventModalShown = false when event creation is successful to close the modal.
        // and also reset the event object to clear the form inputs
        console.log(this.event);
      }
    }
  }
  </script>
  
  <style scoped>
.create-event-modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1000;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* semi-transparent background */
  transition: all 0.3s ease-in-out; /* makes modal appearance smooth */
}

.create-event-modal-content {
  background-color: #fff;
  padding: 2em;
  max-width: 500px;
  width: 80%;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); /* shadow for 3D effect */
  text-align: center; /* centers the text */
  animation: slide 0.3s ease-in-out; /* for a smooth sliding effect */
}

@keyframes slide {
  0% {
    transform: translateY(-50%);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

.create-event-modal-content label {
  display: block;
  margin-top: 1em;
}

.create-event-modal-content input,
.create-event-modal-content textarea {
  width: 100%;
  margin-top: 0.5em;
  padding: 0.5em;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.create-event-modal-content button {
  margin-top: 1em;
  padding: 0.5em 1em;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.create-event-modal-content button:hover {
  background-color: #0056b3;
}
</style>  