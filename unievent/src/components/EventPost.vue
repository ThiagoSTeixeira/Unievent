<template>
    <div class="event-post">
      <h2>{{ event.description }}</h2>
      <p>Date: {{ event.date.toLocaleDateString() }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EventPost',
    props: {
      event: {
        type: Object,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .event-post {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 20px;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
  }
  </style>
  