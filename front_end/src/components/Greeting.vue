<template>
  <!-- This is what the user sees. Anything in {{ }} is dynamic data from the script. -->
  <div class="greeting">
    <h2>Hello, {{ name }}!</h2>
    <p>You've clicked the button {{ clickCount }} time(s).</p>

    <!-- @click is a Vue shortcut for v-on:click. It calls a method when clicked. -->
    <button @click="sayHi">Click me</button>

    <!-- v-model creates a two-way binding between the input and the `name` data. -->
    <input v-model="name" placeholder="Type your name" />
  </div>
</template>

<script>
// Options API: you export an object with named "options" (data, methods, etc.).
// This is often easier to learn than the Composition API (<script setup>) because
// every piece of the component has a clear, named home.
export default {
  name: 'Greeting',

  // `data` must be a function that returns an object.
  // Everything in here becomes reactive: change it, and the template updates.
  data() {
    return {
      name: 'world',
      clickCount: 0,
    }
  },

  // `methods` are functions you can call from the template or other methods.
  // Inside them, `this` refers to the component, so `this.name` reads the data above.
  methods: {
    sayHi() {
      this.clickCount++
      console.log(`Hi, ${this.name}!`)
    },
  },
}
</script>

<style scoped>
/* `scoped` means these styles only apply to this component — they won't leak out. */
.greeting {
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  max-width: 320px;
  margin: 1rem auto;
  text-align: center;
}

button {
  margin: 0.5rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

input {
  padding: 0.5rem;
  width: 80%;
}
</style>
