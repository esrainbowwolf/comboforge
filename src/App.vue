<template>
<div class="app">
    <SideBar />
      <router-view />
</div>
</template>

<script setup>
import SideBar from './components/SideBar'
</script>

<style>
:root{
  --primary: #ff0000;
  --grey: #64748b;
  --dark: #570404;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --gold: #FFD700;
  --sidebar-width: 300px
}

.app {
  display: flex;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: dark;
  margin-top: 60px;
  margin: 0;
  padding: 2rem;
  box-sizing: border-box;
  flex: 1 1 0;
  @media (max-width: 768px){
    padding-left: 6rem
  }
}

body{
  background: var(--light)
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}
</style>
