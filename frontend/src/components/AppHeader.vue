<template>
  <header class="app-header">
    <div class="logo-title">
      <img src="../assets/fishing-man.svg" alt="Logo" class="logo" />
      <h1>Guardian Fisherman</h1>
    </div>
    <nav>
      <a href="#" class="nav-link">Inicio</a>
      <a href="#" class="nav-link">Galería</a>
      <a href="#" class="nav-link">Contacto</a>
    </nav>
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1.5rem 2rem;
  background: #ffffff;
  color: #eb7c45;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  left: 0;
  column-gap: 55%;
}
.logo-title {
  display: flex;
  align-items: center;
}
.logo {
  width: 48px;
  height: 48px;
  margin-right: 1rem;
}
nav {
  display: flex;
  gap: 1.5rem;
}
.nav-link {
  color: #eb7c45;
  text-decoration: none;
  font-weight: 500;
  font-size: 20px;
  transition: color 0.2s;
}
.nav-link:hover {
  color: #38bdf8;
}

</style>
