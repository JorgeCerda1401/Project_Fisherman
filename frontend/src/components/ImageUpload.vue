<template>
  <section class="upload-section">
    <h2>Sube tus imágenes</h2>
    <div class="upload-box">
      <input type="file" accept="image/*" multiple />
      <p>Arrastra y suelta tus imágenes aquí o haz clic para seleccionar archivos.</p>
    </div>
  </section>
</template>

<style scoped>
.upload-section {
  max-width: 500px;
  margin: 2rem auto;
  background: #f8fafc;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(30,41,59,0.07);
  padding: 2rem;
  text-align: center;
}
.upload-section h2 {
  margin-bottom: 1.5rem;
  color: #1e293b;
}
.upload-box {
  border: 2px dashed #38bdf8;
  border-radius: 8px;
  padding: 2rem 1rem;
  background: #e0f2fe;
  cursor: pointer;
  transition: border-color 0.2s;
}
.upload-box:hover {
  border-color: #0ea5e9;
}
.upload-box input[type="file"] {
  display: block;
  margin: 0 auto 1rem;
}
</style>
