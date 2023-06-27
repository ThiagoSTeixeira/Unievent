<template>
  <div class="event-post">
    <h2>{{ event.description }}</h2>
    <p>Date: {{ event.date.toLocaleDateString() }}</p>
    <img :src="`${event.imageURL}`" alt="Event image" />
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
  background: white;
  border-radius: 15px;
  margin: 10px 0;
  padding: 20px;
  box-shadow: 0 4px 6px 0 hsla(0, 0%, 0%, 0.07);
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.event-post h2 {
  margin: 10px 0;
  color: #444;
}

.event-post p {
  margin: 5px 0;
  color: #666;
}

.event-post img {
  max-width: 100%;
  height: auto;
  margin-top: 10px;
  border-radius: 10px;
}
</style>
